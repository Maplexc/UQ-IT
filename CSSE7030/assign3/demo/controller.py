#!/usr/bin/env python3
# coding:utf-8
from model import QuestionQueueContainer
import time
import my_decorator
from threading import Thread
import copy
import math
from collections import Counter
from statistics import mode, median, mean
DISPLAY_CONTENT = "Individual assessment items must be solely your own work.While students are encouraged to have high-level conversation about problem they are"+\
" trying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically"+\
" detects similarity assignment submissions."


def generate_quick_and_long_question_queue_container():
    return QuestionQueueContainer(
        question_type="short question",
        description="<2 mins with a tutor",
        examples=[
            'Syntax errors', 'Interpreting error output',
            'Assignment/MyPytutor interpretation',
            'MyPyTutor submission issues'
        ]), QuestionQueueContainer(
            question_type="long question",
            description=">2 mins with a tutor",
            examples=[
                'Open ended questions', 'How to start a problem',
                'How to improve code', 'Debugging', 'Assignment help'
            ],
        )


def get_waiting_and_resolve_queue(questioncontainer):
    return questioncontainer.waiting_queue, questioncontainer.history_queue


def remove_entity_from_queue(questioncontainer, id, isCanceled=False):
    waiting_queue, history_queue = get_waiting_and_resolve_queue(
        questioncontainer)
    entity = waiting_queue.get_entity_by_id(id)
    e = history_queue.check_entity_within(entity)
    if e:
        print('in here1...')
        if isCanceled:
            print('in here2...')
            e.question_list.pop()
            e.accepted = False
        else:
            entity.accepted = True
            print('in here3...')
            e.accepted = True
        waiting_queue.remove(id)


def get_columns_and_content_from_queue(queue):
    column_names = ['#', "Name", "Question Asked", "Time"]
    contents = []
    for entity in queue.queue:
        temp = []
        temp.append(entity.id)
        temp.append(entity.student_name)
        temp.append(entity.question_asked)
        temp.append(display_time(entity.timestamp))
        contents.append(temp)
    return column_names, contents


def get_queue_length_and_average_waiting_time(queue):
    time_list = []
    for entity in queue.queue:
        time_list.append(entity.timestamp)
    return len(time_list), time.time() - sum(time_list) / len(time_list)


def submit_request(questioncontainer, student_name, question_content):
    questioncontainer.submit_question(student_name, question_content)


def display_time(timestamp):
    interval = time.time() - timestamp
    if interval < 1 * 60:
        return "a few seconds ago"
    elif interval < 2 * 60:
        return "a minute ago"
    elif interval < 60 * 60:
        return "{} minutes ago".format(int(interval / 60))
    elif interval < 2 * 60 * 60:
        return "1 hour ago"
    else:
        return "{} hours ago".format(int(interval / 60 * 60))


@my_decorator.singleton
class Scheduler:
    def __init__(self):
        self._schedule_map = {}

    def schedule_task(self, name, func, interval):
        if name in self._schedule_map:
            self.cancel_task(name)
        p = MyThread(target=self.wrap_schedule_task, args=(func, interval))
        self._schedule_map[name] = p
        p.start()

    def cancel_task(self, task_name):
        if task_name in self._schedule_map:
            self._schedule_map[task_name].stop()
            del self._schedule_map[task_name]

    def cancel_all_tasks(self):
        for task_name in self._schedule_map:
            self.cancel_task(task_name)

    def wrap_schedule_task(self, func, interval):
        while True:
            func()
            time.sleep(interval)


class MyThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_to_stop = False

    def stop(self):
        self._is_to_stop = True

    def run(self):
        while not self._is_to_stop:
            super().run()
            time.sleep(5)


def get_scheduler():
    return Scheduler()


def get_statistics_information_about_history_queue(questioncontainer):
    history_queue = copy.deepcopy(questioncontainer.history_queue.queue)
    history_queue.sort()
    students_list = [(entity.student_name, entity.question_asked)
                     for entity in history_queue[-10:]]
    students_list.reverse()
    waiting_time_list = [entity.timestamp for entity in history_queue]
    mean_waiting_time = display_time(mean(waiting_time_list))
    median_waiting_time = display_time(median(waiting_time_list))
    mode_waiting_time = mode(
        [display_time(waiting) for waiting in waiting_time_list])
    return students_list, mean_waiting_time, median_waiting_time, mode_waiting_time
