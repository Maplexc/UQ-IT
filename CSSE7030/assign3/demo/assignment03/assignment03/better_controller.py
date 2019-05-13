#!/usr/bin/env python3
# coding:utf-8
from better_model import QuestionQueueContainer
import time
import copy
import math
from statistics import mode, median, mean
from functools import partial
import json
from better_view import HeaderFrame, QuestionContainerFrame
import tkinter as tk
import pprint
import helper


class Controller:
    @staticmethod
    def display_time(submit_time, finished_time=None):
        if finished_time:
            interval = finished_time - submit_time
        else:
            interval = time.time() - submit_time
        return helper.display_time(interval)

    def __init__(self, master):
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
        top = tk.Toplevel()
        top.title('Statistics Information')
        text = tk.Text(
            master=top,
            font=('Lucida', '14', 'bold'),
            bg='light blue',
        )
        color_and_font_config = {
            'question_type': {
                'foreground': 'purple',
                'font': ('Lucida', '16', 'bold')
            },
            'mean': {
                'foreground': 'blue',
                'font': ('Lucida', '14', 'bold')
            },
            'median': {
                'foreground': 'red',
                'font': ('Lucida', '14', 'bold')
            },
            'mode': {
                'foreground': 'green',
                'font': ('Lucida', '14', 'bold')
            },
            'ranks': {
                'foreground': 'black',
                'font': ('Lucida', '12', 'italic')
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
                    '\tmedian:{}\n'.format(result['mode']),
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
                    master=top, font=('Lucida', '18', 'Italic'), bg='yellow')
                text.insert(tk.END,
                            "sorry, no summary for {}".format(question_type))

    def initiate_the_views(self):
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
        container = self._container_dict[question_type]
        if real_time:
            json_data = container.request_for_json_data()
            data_dict = json.loads(json_data)
            container.clear_queue()
            container.feed_records_into_queue(data_dict['records'])
            container.sort_queue()
        column_names = ["Name", "Question Asked", "Time"]
        contents = []
        for student in container.queue_content:
            temp = []
            temp.append(student.name)
            temp.append(student.questions_count)
            temp.append(self.display_time(student.timestamp))
            contents.append(temp)
        return column_names, contents, data_dict['count'], data_dict[
            'avg_time']

    def get_statistics_information(self, question_type):
        return self._container_dict[question_type].get_statistics_information()

    def submit_request(self, question_type, student_name, question_content):
        return self._container_dict[question_type].submit_question(
            student_name, question_content)

    def accept(self, question_type, name):
        return self._container_dict[question_type].question_accepted_request(
            name)

    def cancel(self, question_type, name):
        return self._container_dict[question_type].cancel_question_request(
            name)

    def generate_func_dict(self, question_type):
        return {
            'data': partial(self.get_columns_and_content, question_type),
            'submit': partial(self.submit_request, question_type),
            'accept': partial(self.accept, question_type),
            'cancel': partial(self.cancel, question_type),
            'time': self.display_time,
        }

    def start(self):
        self._master.mainloop()


def main():
    app = tk.Tk()
    controller = Controller(master=app)
    controller.start()


if __name__ == "__main__":
    main()