#!/usr/bin/env python3
# coding:utf-8
from model import QuestionQueueContainer, QuestionEntity
import time
from threading import Thread
import copy
import math
from collections import Counter
from statistics import mode, median, mean
from view import QuestionContainerFrame, DEFAULT_KWARGS, HeaderFrame, PAD_X
from functools import partial
import tkinter as tk
import json
import pprint
import requests

SERVER_URL_PREFIX = 'http://localhost:8888/{}'


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
    if not time_list:
        return None, None
    return len(time_list), display_time(sum(time_list) / len(time_list))


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
        return "{} hours ago".format(int(interval / (60 * 60)))


def get_statistics_information_about_history_queue(*questioncontainers):
    result = []
    for questioncontainer in questioncontainers:
        history_queue = copy.deepcopy(questioncontainer.history_queue.queue)
        history_queue.sort()
        students_list = [{
            "name": entity.student_name,
            "question_ask": entity.question_asked
        } for entity in history_queue[-10:]]
        students_list.reverse()
        waiting_time_list = [entity.timestamp for entity in history_queue]
        mean_waiting_time = display_time(mean(waiting_time_list))
        median_waiting_time = display_time(median(waiting_time_list))
        mode_waiting_time = mode(
            [display_time(waiting) for waiting in waiting_time_list])
        result.append({
            'type': questioncontainer.question_type.split()[0],
            'ranks': students_list,
            'mean': mean_waiting_time,
            'median': median_waiting_time,
            'mode': mode_waiting_time
        })
    pprint.pprint(result)
    return result


def generate_func_dict(question_container):
    return {
            'data':partial(lambda queue: (get_columns_and_content_from_queue(queue), get_queue_length_and_average_waiting_time(
                queue)), question_container.waiting_queue),
            'submit': partial(submit_request, question_container),
            'delete': partial(remove_entity_from_queue, question_container)
    }


def show_statistics_information_in_toplevel(*questioncontainers, ):
    results = get_statistics_information_about_history_queue(
        *questioncontainers)
    top = tk.Toplevel()
    text = tk.Text(
        master=top,
        font=('Lucida', 18, 'bold'),
        bg='light yellow',
        foreground='purple')
    text.pack()
    text.insert(tk.END, pprint.pformat(results).strip('[]'))
    top.title('Statistics')


def load_data(questioncontainer):
    resp = requests.get(url="http://localhost:8888/{}".format(
        questioncontainer.question_type.split()[0]))
    contents = json.loads(resp.content)
    for content in contents:
        questioncontainer.submit_question(
            student_name=content['name'],
            question_content=content['question'],
            timestamp=content['time'])


class App:
    def __init__(self, master):
        quick, long = generate_quick_and_long_question_queue_container()
        load_data(quick)
        load_data(long)
        self._master = master
        menu = tk.Menu(self._master)
        menu.add_command(
            label='summary',
            command=partial(show_statistics_information_in_toplevel, quick,
                            long))
        self._master.config(menu=menu)
        self._master.grid_columnconfigure(index=0, weight=1)
        self._master.geometry("{width}x{height}+0+0".format(
            width=self._master.winfo_screenwidth(),
            height=self._master.winfo_screenheight()))
        self._header_frame = HeaderFrame(self._master)
        self._header_frame.grid(row=0, column=0, sticky='wens')
        container_frame = tk.Frame(master=self._master)
        container_frame.grid(row=1, column=0, sticky='nwse')
        container_frame.grid_columnconfigure(index=0, weight=1)
        container_frame.grid_columnconfigure(index=1, weight=1)
        func_dict_quick = generate_func_dict(question_container=quick)
        self._quick_container = QuestionContainerFrame(
            master=container_frame,
            questioncontainer=quick,
            external_func_dict=func_dict_quick)
        func_dict_long = generate_func_dict(question_container=long)
        self._long_container = QuestionContainerFrame(
            master=container_frame,
            questioncontainer=long,
            foreground="blue",
            external_func_dict=func_dict_long)
        self._quick_container.grid(row=0, column=0, sticky='nwse', padx=PAD_X)
        self._long_container.grid(row=0, column=1, sticky='nwse', padx=PAD_X)

    def start(self):
        self._master.mainloop()


def main():
    App(master=tk.Tk()).start()


if __name__ == "__main__":
    main()
