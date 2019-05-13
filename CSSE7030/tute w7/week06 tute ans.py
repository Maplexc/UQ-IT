"""
CSSE1001 -- Class Design Tutorial Sample Solution
"""

__author__ = "Richard Thomas"
__date__ = "13/03/2018"
__copyright__ = "The University of Queensland, 2018"


class Student(object) :
    """Simple representation of a university student."""
    def __init__(self, name, student_num, degree) :
        """Create a student with a name and degree programme.

        Parameters:
            name (str): The student's name "first_name last_name".
            student_num (int): The student's id number.
            degree (str): Degree in which student is enrolled.
        """
        self._name = name
        # We need to store the values on this instance otherwise they will
        # get "forgotten" once the init methods is done.
        self._student_num = student_num
        self._degree = degree
        self._grades = {}

    def get_name(self) :
        """(str) Returns the name of this Student."""
        return self._name

    def get_student_num(self) :
        """(int) Returns the student number of this Student."""
        return self._student_num

    def get_degree(self) :
        """(str) Returns the degree in which this Student is currently enrolled."""
        return self._degree

    def set_degree(self, degree) :
        """Sets the degree programme in which this Student is now enrolled.

        Parameters:
            degree (str): The new degree programme.
        """
        self._degree = degree

    def get_first_name(self) :
        """(str) Returns the first name of this Student."""
        return self._name.split()[0]

    def get_last_name(self) :
        """(str) Returns the last name of this Student."""
        return self._name.split()[1]

    def get_email(self) :
        """(str) Returns the email address of this Student."""
        return '{0}.{1}@uq.net.au'.format(self.get_first_name().lower(),
                                          self.get_last_name().lower())

    def __str__(self) :
        """(str) Returns a textual representation of this Student as:
            Name (email, student number, degree)
        """
        return '{0} ({1}, {2}, {3})'.format(self._name, self.get_email(),
                                            self._student_num, self._degree)

    def __repr__(self) :
        """(str) Returns a technical representation of this Student."""
        return 'Student({0!r}, {1!r}, {2!r})'.format(self._name,
                                                     self._student_num,
                                                     self._degree)

    def add_grade(self, course, grade) :
        """Adds a grade for the given course to this Student.

        Parameters:
            course (str): The course code of the course.
            grade (int): Grade achieved in the course.
        """
        self._grades[course] = grade

    def gpa(self) :
        """(float) Calculates the GPA of this Student."""
        if not self._grades :
            return 0.0
        else :
            return sum(self._grades.values()) / len(self._grades)
            # To get a decimal value, we need to convert one of the operands
            # to a float first, not just the result of the division.
            # i.e. the following would not give the correct answer if the
            # expected gpa has a non-zero decimal component.
            # return float( sum(self._grades.values()) / len(self._grades) )
            # The position of the brackets matters!


def test_student() :
    """Simple tests, with output, of the Student class."""
    student = Student('Michael Palin', 43215678, 'BInfTech')
    print("Name:   ", student.get_name())
    print("Stud. #:", student.get_student_num())
    print("Degree: ", student.get_degree())
    print("set_degree...")
    student.set_degree('BE')
    print("Degree: ", student.get_degree())
    print("First:  ", student.get_first_name())
    print("Last:   ", student.get_last_name())
    print("Email:  ", student.get_email())
    print("str:    ", str(student))
    print("repr:   ", repr(student))



#############################################################################
# Following is some code to check that the Student class generally works
# as expected.


def check_students(students) :
    """Check that all students in a list of Students have unique student numbers.

    Return:
        bool: True if all students have unique student numbers; False otherwise.
    """
    seen = []
    for student in students :
        student_number = student.get_student_num()
        if student_number in seen :
            return False
        seen.append(student_number)
    return True


def check_students(students) :
    """Check that all students in a list of Students have unique student numbers.

    Return:
        bool: True if all students have unique student numbers; False otherwise.
    """
    # Lazier, but more computationally expensive
    for student in students :
        for other_student in students :
            if (student is not other_student and
                student.get_student_num() == other_student.get_student_num()) :
                return False
    return True


def check_students2(students) :
    """Check that all students in a list of Students have unique student numbers.
       A variant where you raise a ValueError when invalid.
       (Note this is an example of using exceptions to report an error.
       Not an example of a good design choice. The example above where you
       return True or False is a better design choice.)

    Return:
        bool: True if all students have unique student numbers.

    Raise:
        ValueError: If two students have the same student number.
    """
    seen = {}
    for student in students :
        student_number = student.get_student_num()
        if student_number in seen :
            raise ValueError(seen[student_number].get_name() + ' and '
                             + student.get_name() 
                             + ' have the same student number')
        seen[student_number] = student
    return True


def test_check_students() :
    """Simple test of the check_students() functions.
       Will only output messages if an error is encountered.
    """
    students1 = [Student('Alice A', 1, 'BE'), Student('Bob B', 2, 'BA'),
                 Student('Carol C', 4, 'BA')]
    # assert raises an exception if the condition is not True
    assert check_students(students1) is True

    students2 = [Student('Alice A', 1, 'BE'), Student('Bob B', 2, 'BA'),
                 Student('Carol C', 4, 'BA'), Student('Dan D', 2, 'BInfTech')]
    assert check_students(students2) is False

    try:
        check_students2(students2)
    except ValueError as e:
        pass
    else:
        raise RuntimeError("That can't be right... tutors never make mistakes :)")



###############################################################################



class Course(object) :
    """Simple representation of a university course."""
    def __init__(self, code, name) :
        """
        Parameters:
            code (str): Unique course code for this Course.
            name (str): The full name of this Course.
        """
        self._code = code
        self._name = name

    def get_code(self) :
        """(str) Returns the course code."""
        return self._code

    def get_name(self) :
        """(str) Returns the name of the course."""
        return self._name


def test_gpa() :
    """Simple test of the calculate GPA functionality.
       Will only output messages if an error is encountered.
    """
    student = Student('Hillary Trump', 43215678, 'BInfTech')
    csse1001 = Course('CSSE1001', 'Intro to Software Engineering')
    deco1800 = Course('DECO1800', 'Design Computing Studio I')

    assert student.gpa() == 0
    student.add_grade(csse1001, 4)
    assert student.gpa() == 4.0
    student.add_grade(deco1800, 5)
    assert student.gpa() == 4.5
    student.add_grade(csse1001, 6)
    assert student.gpa() == 5.5
    

def test_driver() :
    test_student()
    test_check_students()
    test_gpa()


if __name__ == '__main__' :
    test_driver()
