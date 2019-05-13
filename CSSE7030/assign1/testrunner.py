__author__ = 'Steven Summers'
__version__ = ''

import inspect
import io
import json
import re
import sys
import textwrap
import threading
import time
import unittest

from collections import OrderedDict
from enum import Enum, unique
from functools import wraps
from types import FunctionType, ModuleType, TracebackType
from typing import Callable, List, Tuple, Type, Union


# GLOBALS TO EXCLUDE FILES IN TRACEBACK
__TEST_RUNNER = True
setattr(threading, '__THREADING', True)  # Don't like this but otherwise regex

__all__ = ['OrderedTestCase', 'RedirectStdIO', 'TestCase', 'TestMaster',
           'skipIfFailed', 'timeout']

# DEFAULTS
DEFAULT_MAXDIFF = 640
DEFAULT_TIMEOUT = 0
DEFAULT_MIN_PY_VERSION = (3, 6, 0)


# CONSTANTS
DIFF_OMITTED = '\nDiff is {} characters long. Set TestMaster(max_diff=None) to see it.'
DUPLICATE_MSG = 'AS ABOVE'
TAB_SIZE = 4
BLOCK_WIDTH = 80
BLOCK_TEMPLATE = """\
/{0}\\
|{{:^{1}}}|
\\{0}/\
""".format(''.center(BLOCK_WIDTH - 2, '-'), BLOCK_WIDTH - 2)


def skipIfFailed(test_case: Type[unittest.TestCase] = None, test_name: str = None):  # pylint: disable=C0103
    """
    skipIfFail decorator allows you to skip entire TestCases or specific test cases
    if not all tests pass for a TestCase, or if a specifc test case fails.

    At least one test method of TestCase1 needs to fail to skip
    @skipIfFailed(TestCase1)

    Skip if 'test_method' of TestCase1 failed
    @skipIfFailed(TestCase1, 'test_method')

    Skip if 'test_method' failed
    Can only be applied to method with class class containing a method named 'test_method'
    @skipIfFailed(test_name='test_method')
    """
    if test_case is None and test_name is None:
        raise RuntimeError(
            "test_case and test_name for skipIfFailed can't both be None")

    if test_case is not None and test_name is not None and not hasattr(test_case, test_name):
        raise AttributeError('{0} has no method {1}'.format(
            test_case.__name__, test_name))

    def decorator(obj: Union[Type[TestCase], Callable]):
        if hasattr(obj, '__skip_test__'):
            obj.__skip_test__.append((test_case, test_name))
        else:
            obj.__skip_test__ = [(test_case, test_name)]
        if not isinstance(obj, FunctionType):
            return obj

        @wraps(obj)
        def wrapper(*args, **kwargs):
            return obj(*args, **kwargs)
        return wrapper
    return decorator


def _timeout_wrapper(test_func):
    """
    Runs the test function in a killable thread, the seconds value
    is obtained from the __timeout__ attribute which can be set globally
    using TestMaster(timeout=value) or apply to specific classes or functions
    using the timeout decorator, if seconds <= 0 the test is not threaded.
    """
    @wraps(test_func)
    def threaded_wrapper(self):
        secs = getattr(test_func, '__timeout__', 0) or \
            getattr(self.__class__, '__timeout__', 0) or \
            _TimeoutThread.timeout

        if secs <= 0:
            return test_func(self)

        thread = _TimeoutThread(target=test_func, args=(self,))
        thread.start()
        thread.join(secs)
        alive = thread.isAlive()
        thread.kill()

        if thread.exc_info is not None:
            raise thread.exc_info[1].with_traceback(thread.exc_info[2])

        if alive:
            # raise TimeoutError(f'Function ran longer than {secs} second(s)')
            raise unittest.SkipTest(
                f'Function ran longer than {secs} second(s)')
        return None
    return threaded_wrapper


def timeout(seconds: float = 0):
    """ Decorator to apply __timeout__ atrribute to a test method or TestCase """
    def timeout_decorator(test_obj):
        test_obj.__timeout__ = seconds
        return test_obj
    return timeout_decorator


@unique
class TestOutcome(Enum):
    SUCCESS = '+'
    FAIL = '-'
    SKIP = '?'


class RedirectStdIO:
    """
    Content manager to send stdin input and capture stdout and stderr

    Usage:
        with RedirectStdIO(stdin=True, stdout=True) as stdio:
            stdio.set_stdin('World!\n')
            inp = input('Hello')

        stdio.stdout == 'Hello'
        inp == 'World'
    """

    def __init__(self, stdin: bool = False, stdout: bool = False, stderr: bool = False):
        self._sys_stdin = sys.stdin
        self._sys_stdout = sys.stdout
        self._sys_stderr = sys.stderr

        self._stdin_stream = io.StringIO() if stdin else None
        self._stdout_stream = io.StringIO() if stdout else None
        self._stderr_stream = io.StringIO() if stderr else None

    def __enter__(self):
        if self._stdin_stream is not None:
            sys.stdin = self._stdin_stream

        if self._stdout_stream is not None:
            sys.stdout = self._stdout_stream

        if self._stderr_stream is not None:
            sys.stderr = self._stderr_stream

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdin = self._sys_stdin
        sys.stdout = self._sys_stdout
        sys.stderr = self._sys_stderr

    @staticmethod
    def _read_stream(stream: io.StringIO) -> str:
        if stream is None:
            raise RuntimeError(
                'Attempt to read from a stream that has not been enabled')
        stream.seek(0)
        return stream.read()

    def set_stdin(self, string: str):
        if self._stdin_stream is None:
            raise RuntimeError(
                f'stdin has not been set in {self.__class__.__name__}.__init__')

        char_count = self._stdin_stream.write(string)
        self._stdin_stream.seek(0)
        return char_count

    @property
    def stdout(self) -> str:
        return self._read_stream(self._stdout_stream)

    @property
    def stderr(self) -> str:
        return self._read_stream(self._stderr_stream)


class TestLoader(unittest.TestLoader):
    """ Custom loader class to specify TestCase case order """

    def getTestCaseNames(self, testCaseClass: Type[unittest.TestCase]):
        """
        Override for unittest.TestLoad.getTestCaseNames
        Return a sorted sequence of method names found within testCaseClass
        """
        if issubclass(testCaseClass, OrderedTestCase):
            return testCaseClass.member_names
        return super().getTestCaseNames(testCaseClass)


class _TestCaseMeta(type):
    """
    MetaClass to decorate all test methods with _timeout_wrapper and 
    track test method definition order.
    """
    def __new__(cls, name, bases, classdict):
        member_names = []
        for key, value in classdict.items():
            if key.startswith(TestLoader.testMethodPrefix) and callable(value):
                member_names.append(key)
                classdict[key] = _timeout_wrapper(value)

        result = super().__new__(cls, name, bases, classdict)
        result.member_names = member_names
        return result


class _TimeoutThread(threading.Thread):
    """
    Killable thread using a global debug tracing function set with sys.settrace
    """
    timeout = DEFAULT_TIMEOUT

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False
        self.exc_info = None

    def run(self):
        """
        Set the trace function and run the thread catching and storing
        any exceptions that occur. 
        """
        sys.settrace(self.global_trace)
        try:
            super().run()
        except Exception:  # pylint: disable=W0703
            self.exc_info = sys.exc_info()

    def global_trace(self, _frame, event, _arg):
        """ Global trace function for sys.settrace which retuns a local trace function """
        if event == 'call':
            return self.local_trace
        return None

    def local_trace(self, _frame, event, _arg):
        """
        Local trace function which kills the thread should it still be running and
        and the 'killed' attribute is set to True.
        """
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.local_trace

    def kill(self):
        self.killed = True


class TestCase(unittest.TestCase, metaclass=_TestCaseMeta):
    """
    Extends the unittest.TestCase defining additional assert methods.
    """
    # pylint: disable=C0103
    member_names: List[str]

    def assertDefined(self, obj: Union[ModuleType, Type], name: str):
        self.assertIs(hasattr(obj, name), True,
                      "'{}' is not defined correctly, check spelling".format(name))

    def assertFunctionDefined(self, obj: Union[ModuleType, Type], function_name: str, params: int):
        self.assertDefined(obj, function_name)
        func = getattr(obj, function_name)
        self.assertIs(inspect.isfunction(func), True)
        sig = inspect.signature(func)
        self.assertEqual(len(sig.parameters), params,
                         "'{}' does not have the correct number of parameters, expected"
                         " {} found {}".format(function_name, params, len(sig.parameters)))

    def assertClassDefined(self, module: ModuleType, class_name: str):
        self.assertDefined(module, class_name)
        class_ = getattr(module, class_name)
        self.assertIs(inspect.isclass(class_), True)

    def assertIsSubclass(self, sub_class: Type, parent_class: Type):
        self.assertIs(issubclass(sub_class, parent_class), True,
                      "'{}' is not a subclass of '{}'".format(sub_class, parent_class))

    def assertDocString(self, obj: Union[Type, Callable]):
        doc = inspect.getdoc(obj)
        msg = "Documentation string is required for '{}'".format(
            obj.__qualname__)
        self.assertIsNot(doc, None, msg)
        self.assertNotEqual(doc, '', msg)

    def _truncateMessage(self, message, diff):
        """ override unittest.TestCase._truncateMessage to use our DIFF_OMITTED message """
        max_diff = self.maxDiff
        if max_diff is None or len(diff) <= max_diff:
            return message + diff
        return message + DIFF_OMITTED.format(len(diff))

    @property
    def name(self) -> str:
        return self._testMethodName

    @property
    def description(self) -> str:
        short_desc = self.shortDescription()
        return short_desc if short_desc else self.name


class OrderedTestCase(TestCase):
    """ TestCase with the description property reflecting the test number """
    @property
    def description(self):
        return '{}. {}'.format(self.member_names.index(self.name) + 1,
                               super().description)


class TestResult(unittest.TestResult):
    """
    TestResult stores the result of each test in the order they were executed
    """

    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self._start = 0
        self._stop = 0
        self.results = OrderedDict()

    def startTestRun(self):
        self._start = time.time()
        super().startTestRun()

    def stopTestRun(self):
        self._stop = time.time()
        super().stopTestRun()

    @property
    def run_time(self):
        return self._stop - self._start

    def startTest(self, test: TestCase):
        test_cls_name = test.__class__.__name__
        if test_cls_name not in self.results:
            self.results[test_cls_name] = OrderedDict()

        test_method = getattr(test.__class__, test.name)
        self._apply_skip(test, test.__class__)
        self._apply_skip(test, test_method)

        super().startTest(test)

    def _apply_skip(self, test: TestCase, test_item: Union[Type[TestCase], FunctionType]):
        """
        Applies the unittest attributes used for skipping tests if the __skip_test__
        attribute has been applied to either the test class or method using the
        skipIfFailed decorator.
        """
        skip_test = getattr(test_item, '__skip_test__', None)
        if skip_test is None:
            return

        for test_cls, test_name in skip_test:
            if test_cls is None:
                test_cls = test.__class__
                if not hasattr(test_cls, test_name):
                    raise AttributeError('{0} has no method {1}'.format(
                        test_cls.__name__, test_name))

            test_cls_name = test_cls.__name__

            if test_cls_name not in self.results:
                raise RuntimeError("Can't check to skip {}.{} if {} hasn't run".format(
                    test.__class__.__name__, test.name, test_cls_name))

            test_results = self.results[test_cls_name]
            if test_name is not None and test_name not in test_results:
                raise RuntimeError("Can't check to skip {}.{} if {}.{} hasn't run".format(
                    test.__class__.__name__, test.name, test_cls_name, test_name))

            if test_name is not None and test_results[test_name][1] != TestOutcome.SUCCESS:
                # set attributes unittest looks for if a test is marked to skip
                test_item.__unittest_skip__ = True
                test_item.__unittest_skip_why__ = 'Skipped due to failing {}.{}'.format(
                    test_cls_name, test_name)
                break

            elif test_name is None and any(tup[1] != TestOutcome.SUCCESS
                                           for tup in test_results.values()):
                test_item.__unittest_skip__ = True
                test_item.__unittest_skip_why__ = \
                    'Skipped due to failing a test from {}'.format(
                        test_cls_name)
                break
        # delete custom attribute since __unittest_skip__ has been applied
        del test_item.__skip_test__

    def add_outcome(self, test: TestCase, outcome: TestOutcome):
        self.results[test.__class__.__name__][test.name] = (test, outcome)

    def addSuccess(self, test: TestCase):
        self.add_outcome(test, TestOutcome.SUCCESS)
        super().addSuccess(test)

    def addFailure(self, test: TestCase, err: Tuple[Type, Exception, TracebackType]):
        self.add_outcome(test, TestOutcome.FAIL)
        super().addFailure(test, err)

    def addError(self, test: TestCase, err: Tuple[Type, Exception, TracebackType]):
        self.add_outcome(test, TestOutcome.FAIL)
        super().addError(test, err)

    def addSkip(self, test: TestCase, reason: str):
        self.add_outcome(test, TestOutcome.SKIP)
        super().addSkip(test, reason)

    def _is_relevant_tb_level(self, tb):
        """
        Override which is used with unittest.TestResult._exc_info_to_string
        to determine what levels of a traceback to skip when formatting the error.
        """
        return '__TEST_RUNNER' in tb.tb_frame.f_globals or \
            '__THREADING' in tb.tb_frame.f_globals or \
            super()._is_relevant_tb_level(tb)


class TestMaster:
    """
    Core driving class which creates the TestSuite from the provided TestCases

    Parameters:
        max_diff: This attribute controls the maximum length of diffs output
            by assert methods that report diffs on failure. Set to None for no max
        timeout: global timeout value in seconds, if a timeout > 0 is specified then
            the tests are run in killable threads.
        output_json: outputs a text summary if True else json from the result.
        hide_paths: if True file paths in tracebacks for failures are removed to
            only contain the filename.
    """
    separator1 = '=' * BLOCK_WIDTH
    separator2 = '-' * BLOCK_WIDTH
    indent = ' ' * TAB_SIZE
    _remove_path = re.compile(r'File ".*[\\/]([^\\/]+.py)"')
    # _remove_threading = re.compile(
    #     r'(^\s*File \".*threading.py\".+?(?=\s*File \"))', flags=re.DOTALL | re.MULTILINE)

    def __init__(self,
                 max_diff: int = DEFAULT_MAXDIFF,
                 timeout: int = DEFAULT_TIMEOUT,  # pylint: disable=W0621
                 #  min_py_version: Tuple[int, int, int] = DEFAULT_MIN_PY_VERSION,
                 output_json: bool = False,
                 hide_paths: bool = True):

        # self.min_py_version = min_py_version
        self.output_json = output_json
        self.hide_paths = hide_paths

        TestCase.maxDiff = max_diff
        _TimeoutThread.timeout = timeout

    @staticmethod
    def _load_tests(test_cases: List[Union[TestCase, Type[TestCase]]]) -> unittest.TestSuite:
        loader = TestLoader()
        suite = unittest.TestSuite()

        for test_case in test_cases:
            if isinstance(test_case, unittest.TestCase):
                suite.addTest(test_case)
            else:
                suite.addTests(loader.loadTestsFromTestCase(test_case))
        return suite

    @staticmethod
    def _add_flavour(flavour: str, test_results: List[Tuple[TestCase, str]]):
        return [(flavour, test, msg) for test, msg in test_results]

    def print_results(self, all_tests: List[TestCase], result: TestResult):
        # Join the lists sorted by the test order
        failed_tests = sorted(
            self._add_flavour('FAIL', result.failures) +
            self._add_flavour('ERROR', result.errors) +
            self._add_flavour('SKIP', result.skipped),
            key=lambda t: all_tests.index(t[1]))

        # print summary
        print(BLOCK_TEMPLATE.format('Summary of Results'))
        for test_cls, test_cases in result.results.items():
            print(test_cls)
            for _test_name, (test, outcome) in test_cases.items():
                print(f'{self.indent}{outcome.value} {test.description}')

        # print fails
        if failed_tests:
            print(self.separator2)
            print(BLOCK_TEMPLATE.format('Failed Tests'))
            prev = None
            for flavour, test, msg in failed_tests:
                self.print_error(
                    flavour, test, DUPLICATE_MSG if msg == prev else msg.strip())
                prev = msg

    def print_stats(self, result: TestCase):
        runtime = result.run_time
        total = result.testsRun
        fails, skips, errors = map(
            len, (result.failures, result.skipped, result.errors))
        passed = total - fails - skips - errors

        print(self.separator2)
        print(f'Ran {total} tests in {runtime:.3f} seconds with {passed} passed'
              f'/{skips} skipped/{fails} failed.')

    def print_error(self, flavour: str, test: TestCase, msg: str):
        print(self.separator1)
        print(f'{flavour}: {test.__class__.__name__} {test.description}')
        print(self.separator2)
        if self.hide_paths:
            msg = self._remove_path.sub(r'File "\1"', msg)
        # msg = self._remove_threading.sub('', msg)
        print(textwrap.indent(msg, self.indent))
        print()

    def run(self, test_cases: List[Union[TestCase, Type[TestCase]]]) -> TestResult:
        # ensure python version
        # assert sys.version_info >= self.min_py_version, (
        #     f"Your Python version is {sys.version_info[:3]} which does not meet the "
        #     f"minimun required version of {self.min_py_version}")

        suite = self._load_tests(test_cases)

        # hide unittest stderr output
        with RedirectStdIO(stderr=True):
            runner = unittest.TextTestRunner(verbosity=0,
                                             resultclass=TestResult)

        all_tests = list(suite)
        result = runner.run(suite)

        if self.output_json:
            results = {test_cls: {name: outcome.value for name, (test, outcome) in res.items()}
                       for test_cls, res in result.results.items()}

            json.dump(results, sys.stdout, indent=4)
        else:
            self.print_results(all_tests, result)
            self.print_stats(result)

        return result
