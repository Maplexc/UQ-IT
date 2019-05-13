#!/usr/bin/env python3
# coding:utf-8
import json
import time

import requests

import helper


class Student:
    """
    class to store the Student information including the name, question count and submit timestamp
    """

    def __init__(self, name, questions_count=0, timestamp=None):
        """
        :param name: str student name
        :param questions_count: int questions count
        :param timestamp: double, the timestamp when student submit a question
        """
        self._name = name
        self._questions_count = questions_count
        if timestamp:
            self._timestamp = timestamp
        else:
            self._timestamp = time.time()

    @property
    def name(self):
        return self._name

    @property
    def questions_count(self):
        return self._questions_count

    @questions_count.setter
    def questions_count(self, num):
        self._questions_count = num

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    def __lt__(self, other):
        """
        :param other: other Student
        :return: bool
        override this method to make it sortable in queue
        """
        if self.questions_count < other.questions_count:
            return True
        elif self.questions_count == other.questions_count:
            return self.timestamp < other.timestamp
        else:
            return False


class StudentQueue:
    """
    class to store active students who are requesting for question resolution
    """

    def __init__(self):
        """
        _queue: list(Student)
        """
        self._queue = []

    @property
    def queue(self):
        return self._queue

    @property
    def names_in_queue(self):
        return [student.name for student in self.queue]

    def append(self, name, questions_count, timestamp=None):
        """
        :param name:str student name
        :param questions_count: int
        :param timestamp: double
        :return: None
        append the student to the queue
        """
        self._queue.append(
            Student(
                name=name,
                questions_count=questions_count,
                timestamp=timestamp))

    def sort(self):
        """
        Sort the Student in the Queue
        :return: None
        """
        self._queue.sort()

    def clear(self):
        """
        clear the Queue
        :return: None
        """
        self._queue.clear()


class QuestionQueueContainer:
    """
    class to handle the Student Queue and as a handler to request data from the server
    SESSION: a general session for html request, make it as static attribute
    URL_PREFIX: contains the server host ip and port information
    """

    SESSION = requests.session()
    URL_PREFIX = 'http://localhost:8080/{}'

    def __init__(self, question_type, description):
        """
        :param question_type: quick or long
        :param description: str
        """
        self._question_type = question_type
        self._description = description
        self._waiting_queue = StudentQueue()

    def clear_queue(self):
        """
        method to clear the queue in the container
        :return: None
        """
        self._waiting_queue.clear()

    def sort_queue(self):
        """
        method to sort the queue in the container
        :return: None
        """
        self._waiting_queue.sort()

    def feed_records_into_queue(self, records):
        """
        :param records: list of dict {name: str, question_count:int, timestamp:float}
        :return: None
        """
        for record in records:
            name = record['name']
            questions_count = record['question_count']
            timestamp = record['timestamp']
            self._waiting_queue.append(
                name=name,
                questions_count=questions_count,
                timestamp=timestamp)

    def request_for_json_data(self):
        """
        :return: json data, the active students in quick or long queue who are requesting for resolution
        including name, question_count and waiting time
        """
        try:
            resp = self.SESSION.get(
                url=self.URL_PREFIX.format('data'),
                params={'question_type': self.question_type})
            return resp.content
        except Exception as e:
            return json.dumps(helper.format_error(reason=str(e)))

    def submit_question(self, name, question_content):
        """
        :param name:str student name
        :param question_content:int
        :return: dict indicates whether the question successfully submited or the reason the submit fail
        """
        try:
            resp = self.SESSION.post(
                url=self.URL_PREFIX.format('submit'),
                data={
                    'name': name,
                    'content': question_content,
                    'question_type': self.question_type
                })
            return json.loads(resp.text)
        except Exception as e:
            return helper.format_error(reason=str(e))

    def cancel_question_request(self, name):
        """
        :param name: student name
        :return: dict indicates whether the question successfully cancel or the reason the cancel fail
        """
        try:
            resp = requests.post(
                url=self.URL_PREFIX.format('cancel'),
                data={
                    'name': name,
                    'question_type': self.question_type
                })
            return json.loads(resp.text)
        except Exception as e:
            return helper.format_error(reason=str(e))

    def question_accepted_request(self, name):
        """
        :param name: student name
        :return: bool indicates whether the question has been successfully accept
        """
        try:
            resp = requests.post(
                url=self.URL_PREFIX.format('accept'),
                data={
                    'name': name,
                    'question_type': self.question_type
                })
            return json.loads(resp.text)
        except Exception as e:
            return helper.format_error(reason=str(e))

    @property
    def waiting_queue(self):
        return self._waiting_queue

    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, q_type):
        self._question_type = q_type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, q_description):
        self._description = q_description

    @property
    def queue_content(self):
        return self.waiting_queue.queue

    def get_statistics_information(self):
        """
        :return: json data about the historical summary about mean, median, mode waiting time
        and top 10 students who request for the most questions
        or the exeception cause the query fail
        """
        try:
            resp = self.SESSION.get(
                url=self.URL_PREFIX.format('statistics'),
                params={'question_type': self.question_type})
            return resp.content
        except Exception as e:
            return helper.format_error(reason=str(e))
