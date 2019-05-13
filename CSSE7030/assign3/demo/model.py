#!/usr/bin/env python3
# coding:utf-8
import time
import copy


class QuestionQueueContainer:
    def __init__(self, question_type, description, examples):
        self._question_type = question_type
        self._description = description
        self._examples = examples
        self._waiting_queue = QuestionQueue()
        self._history_queue = copy.deepcopy(self._waiting_queue)

    @property
    def waiting_queue(self):
        return self._waiting_queue

    @property
    def history_queue(self):
        return self._history_queue

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
    def examples(self):
        return self._examples

    @examples.setter
    def examples(self, q_examples):
        self._examples = q_examples

    def __repr__(self):
        return ' '.join(
            [word.capitalize() for word in self.question_type.split()])

    def __str__(self):
        return self.__repr__()

    def submit_question(self, student_name, question_content):
        entity = QuestionEntity(
            student_name=student_name, question_content=question_content)
        self.waiting_queue.append(entity)
        self.history_queue.append(copy.deepcopy(entity))


class QuestionQueue:
    def __init__(self):
        self._queue = []

    @property
    def queue(self):
        return self._queue

    def check_entity_within(self, question_entity):
        for e in self._queue:
            if question_entity.student_name == e.student_name:
                return e
        return None

    def append(self, question_entity):
        entity = self.check_entity_within(question_entity)
        if entity:
            entity.timestamp = time.time()
            for content in question_entity.question_list:
                entity.append(content)
        else:
            self._queue.append(question_entity)
        self.sort()

    def sort(self):
        self._queue.sort()
        for i, entity in enumerate(self._queue):
            entity._id = i + 1

    def get_entity_by_id(self, id):
        return self._queue[id - 1]

    def remove(self, id):
        result = self.get_entity_by_id(id)
        self._queue.remove(result)
        self.sort()

    def __repr__(self):
        if self._queue:
            return '\n'.join([e.__str__() for e in self._queue])
        else:
            return "No students in the queue"

    def __str__(self):
        return self.__repr__()


class QuestionEntity:
    def __init__(self, student_name, id=-1, question_content=None):
        self._student_name = student_name
        self._id = id
        self._timestamp = time.time()
        self._question_list = []
        self._request_accept = False
        if question_content and question_content.strip():
            self._question_list.append(question_content.strip())

    @property
    def accepted(self):
        return self._request_accept

    @accepted.setter
    def accepted(self, accepted):
        self._request_accept = accepted

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, student_name):
        self._student_name = student_name

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def question_list(self):
        return self._question_list

    @property
    def question_asked(self):
        if len(self._question_list) == 0:
            return 0
        if self.accepted:
            return len(self._question_list)
        else:
            return len(self._question_list) - 1

    def __lt__(self, value):
        return self.question_asked < value.question_asked

    def __gt__(self, value):
        return not self.__lt__(value)

    def __repr__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(
            self.id, self.student_name, self.question_asked, self.timestamp,
            self.question_list)

    def __str__(self):
        return self.__repr__()

    def append(self, question):
        if question not in self._question_list and question:
            self._question_list.append(question)

    def remove(self, question):
        if question in self._question_list:
            self._question_list.remove(question)
