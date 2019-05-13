#!/usr/bin/env python3
# coding:utf-8
import json
import time
import tkinter as tk
from functools import partial

import helper
from model import QuestionQueueContainer
from view import HeaderFrame, QuestionContainerFrame

"""
Assignment 3 Queue
CSSE1001/7030
Semester 2, 2018
"""
__author__ = "Zhibin Huang  & 45407422"


class Controller:
    """
    class act as a proxy to handle the communication between the views and models
    """
    """
    format time base on timestamp
    """

    @staticmethod
    def display_time(submit_time, finished_time=None):
        if finished_time:
            interval = finished_time - submit_time
        else:
            interval = time.time() - submit_time
        return helper.display_time(interval)

    def __init__(self, master):
        """
        :param master: tk.TK instance
        :argument _container_dict, a dictionary to hold the quick and short type questions models
                   menu for display historical statistics summary
        """
        self._container_dict = {
            'quick':
            QuestionQueueContainer(
                question_type='quick', description='quick question'),
            'long':
            QuestionQueueContainer(
                question_type='long', description='long question')
        }
        self._master = master
        menu = tk.Menu(self._master)
        menu.add_command(
            label='summary',
            command=partial(self.show_statistics_information_in_toplevel,
                            *self._container_dict.keys()))
        self._master.config(menu=menu)
        self._master.grid_columnconfigure(index=0, weight=1)
        self._master.geometry("{width}x{height}+0+0".format(
            width=self._master.winfo_screenwidth(),
            height=self._master.winfo_screenheight()))
        self.initiate_the_views()

    def show_statistics_information_in_toplevel(self, *question_types):
        """
        :param question_types: quick or long
        :return: None
        to display the statistics information on a top level
        """
        top = tk.Toplevel()
        top.title('Statistics Information')
        text = tk.Text(
            master=top,
            font=('Arial', '14', 'bold'),
            bg='light blue',
        )
        color_and_font_config = {
            'question_type': {
                'foreground': 'purple',
                'font': ('Arial', '16', 'bold')
            },
            'mean': {
                'foreground': 'blue',
                'font': ('Arial', '14', 'bold')
            },
            'median': {
                'foreground': 'red',
                'font': ('Arial', '14', 'bold')
            },
            'mode': {
                'foreground': 'green',
                'font': ('Arial', '14', 'bold')
            },
            'ranks': {
                'foreground': 'black',
                'font': ('Arial', '12', 'italic')
            }
        }
        for k, v in color_and_font_config.items():
            text.tag_config(tagName=k, **v)
        text.pack()
        for question_type in question_types:
            result = json.loads(
                self.get_statistics_information(question_type=question_type))
            if result['status'] == 'OK':
                text.insert(
                    tk.END,
                    'summary type: {} questions\n'.format(question_type),
                    'question_type')
                text.insert(
                    tk.END,
                    '\tmean:{}\n'.format(result['mean']),
                    'mean',
                )
                text.insert(
                    tk.END,
                    '\tmedian:{}\n'.format(result['median']),
                    'median',
                )
                text.insert(
                    tk.END,
                    '\tmode:{}\n'.format(result['mode']),
                    'mode',
                )

                if result['ranks'] == 'Empty':
                    text.insert(tk.END, '\tranks:Empty\n', 'ranks')
                else:
                    text.insert(tk.END, '\tranks:\n', 'ranks')
                    for record in result['ranks']:
                        text.insert(
                            tk.END, '\t\tname:{name}, total:{total}\n'.format(
                                name=record['name'], total=record['total']),
                            'ranks')
            else:
                text = tk.Text(
                    master=top, font=('Arial', '18', 'Italic'), bg='yellow')
                text.insert(tk.END,
                            "sorry, no summary for {}".format(question_type))

    def initiate_the_views(self):
        """
        :return: None
        method to instantiate necessary views
        """
        self._header_frame = HeaderFrame(master=self._master)
        self._header_frame.grid(row=0, column=0, sticky='wens')
        container_frame = tk.Frame(master=self._master)
        container_frame.grid(row=1, column=0, sticky='nwse')
        container_frame.grid_columnconfigure(index=0, weight=1)
        container_frame.grid_columnconfigure(index=1, weight=1)
        self._quick_container = QuestionContainerFrame(
            master=container_frame,
            question_type='short question',
            description='<2 mins with a tutor',
            external_func_dict=self.generate_func_dict(question_type='quick'),
            examples=[
                'Syntax errors', 'Interpreting error output',
                'Assignment/MyPytutor interpretation',
                'MyPyTutor submission issues'
            ])
        self._long_container = QuestionContainerFrame(
            master=container_frame,
            question_type='long question',
            description='>2 mins with a tutor',
            foreground='blue',
            external_func_dict=self.generate_func_dict(question_type='long'),
            examples=[
                'Open ended questions', 'How to start a problem',
                'How to improve code', 'Debugging', 'Assignment help'
            ])
        self._quick_container.grid(row=0, column=0, sticky='nwse', padx=12)
        self._long_container.grid(row=0, column=1, sticky='nwse', padx=12)

    def get_columns_and_content(self, question_type, real_time=True):
        """
        :param question_type: quick or long
        :param real_time: bool if it is True it will send a http request to the server to get active data, otherwise
        just the the data from the container queue
        :return:
        data column names
        data contents 2 dimesion list

        if sending http request and get response successfully the container will clear its queue and
        feed new data into the queue and sort
        otherwise it would just keep the own data
        """
        container = self._container_dict[question_type]
        column_names = ["Name", "Question Asked", "Time"]
        if real_time:
            json_data = container.request_for_json_data()
            data_dict = json.loads(json_data)
            if data_dict['status'] == 'OK':
                container.clear_queue()
                container.feed_records_into_queue(data_dict['records'])
                container.sort_queue()
                count = data_dict['count']
                avg_time = data_dict['avg_time']
            else:
                count = len(container.queue_content)
                if count == 0:
                    avg_time = None
                else:
                    avg_time = sum([
                        student.timestamp
                        for student in container.queue_content
                    ]) / count
        contents = [[
            student.name, student.questions_count,
            self.display_time(student.timestamp)
        ] for student in container.queue_content]
        return column_names, contents, count, avg_time

    def get_statistics_information(self, question_type):
        """
        :param question_type: quick or long
        :return: json data including mean, median, mode waiting time and top 10 student who have asked the most questions
        """
        return self._container_dict[question_type].get_statistics_information()

    def submit_request(self, question_type, student_name, question_content):
        """
        :param question_type: quick or long
        :param student_name: student name
        :param question_content: question content
        :return: dict indicates whether the question has successfully submit or not,if not clarify the failure
        either it is duplicated or server internal error
        """
        names_list = [
            container.waiting_queue.names_in_queue
            for container in self._container_dict.values()
        ]
        for names in names_list:
            if student_name in names:
                return helper.format_error(
                    status='DUPLICATE', reason='duplicate in queues')
        return self._container_dict[question_type].submit_question(
            student_name, question_content)

    def accept(self, question_type, name):
        """
        :param question_type: quick or short
        :param name: student name
        :return: dict indicates whether the question has been sucessfully accepted or not, if not clarify the failure
        """
        return self._container_dict[question_type].question_accepted_request(
            name)

    def cancel(self, question_type, name):
        """
        :param question_type: quick or long
        :param name: student name
        :return: dict indicates whether the question has successfully be canceled or not, if not clarify the failure
        """
        return self._container_dict[question_type].cancel_question_request(
            name)

    def generate_func_dict(self, question_type):
        """
        :param question_type: long or short
        :return: dict {name: func}
        since the http requesting functions are define in models
        however views needs to requests for active data
        based on design pattern, views should never communicate with models directly
        therefore in here the controller wraps up the neccessary functions as dictionary
        and pass them to some views
        """
        return {
            'data': partial(self.get_columns_and_content, question_type),
            'submit': partial(self.submit_request, question_type),
            'accept': partial(self.accept, question_type),
            'cancel': partial(self.cancel, question_type),
            'time': self.display_time,
        }

    def start(self):
        """
        method to start the client
        :return:
        """
        self._master.mainloop()


def main():
    app = tk.Tk()
    controller = Controller(master=app)
    controller.start()


if __name__ == "__main__":
    main()
