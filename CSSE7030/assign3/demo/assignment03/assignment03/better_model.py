#!/usr/bin/env python3
#coding:utf-8
import time
import json
import requests


class QuestionEntity:
    def __init__(self,
                 question_content,
                 submit_time=None,
                 requesting=True,
                 accepted=False):
        self._question_content = question_content
        if submit_time:
            self._submit_time = submit_time
        else:
            self._submit_time = time.time()
        self._requesting = requesting
        self._accepted = accepted

    @property
    def time(self):
        return self._submit_time

    @time.setter
    def time(self, timestamp):
        self._submit_time = timestamp

    @property
    def requesting(self):
        return self._requesting

    @requesting.setter
    def requesting(self, requesting):
        self._requesting = requesting

    @property
    def accepted(self):
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        self._accepted = accepted

    def __lt__(self, other):
        return self.time < other.time


class Student:
    def __init__(self, name, questions_count=0, timestamp=None):
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
        if self.questions_count < other.questions_count:
            return True
        elif self.questions_count == other.questions_count:
            return self.timestamp < other.timestamp
        else:
            return False


class StudentQueue:
    def __init__(self):
        self._queue = []

    @property
    def queue(self):
        return self._queue

    def append(self, name, questions_count, timestamp=None):
        self._queue.append(
            Student(
                name=name,
                questions_count=questions_count,
                timestamp=timestamp))

    def sort(self):
        self._queue.sort()

    def clear(self):
        self._queue.clear()


class QuestionQueueContainer:
    SESSION = requests.session()
    URL_PREFIX = 'http://10.89.87.102:8888/{}'

    @staticmethod
    def format_exception(e):
        return json.dumps({'status': 'ERROR', 'error': str(e)})

    def __init__(self, question_type, description):
        self._question_type = question_type
        self._description = description
        self._waiting_queue = StudentQueue()

    def clear_queue(self):
        self._waiting_queue.clear()

    def sort_queue(self):
        self._waiting_queue.sort()

    def feed_records_into_queue(self, records):
        for record in records:
            name = record['name']
            questions_count = record['question_count']
            timestamp = record['timestamp']
            self._waiting_queue.append(
                name=name,
                questions_count=questions_count,
                timestamp=timestamp)

    def request_for_json_data(self):
        resp = self.SESSION.get(
            url=self.URL_PREFIX.format('data'),
            params={'question_type': self.question_type})
        return resp.content

    def submit_question(self, name, question_content):
        resp = self.SESSION.post(
            url=self.URL_PREFIX.format('submit'),
            data={
                'name': name,
                'content': question_content,
                'question_type': self.question_type
            })
        return json.loads(resp.text)['status'] == "OK"

    def cancel_question_request(self, name):
        resp = requests.post(
            url=self.URL_PREFIX.format('cancel'),
            data={
                'name': name,
                'question_type': self.question_type
            })
        return json.loads(resp.text)['status'] == "OK"

    def question_accepted_request(self, name):
        resp = requests.post(
            url=self.URL_PREFIX.format('accept'),
            data={
                'name': name,
                'question_type': self.question_type
            })
        return json.loads(resp.text)['status'] == "OK"

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
        try:
            resp = self.SESSION.get(
                url=self.URL_PREFIX.format('statistics'),
                params={'question_type': self.question_type})
            return resp.content
        except Exception as e:
            return self.format_exception(e)
