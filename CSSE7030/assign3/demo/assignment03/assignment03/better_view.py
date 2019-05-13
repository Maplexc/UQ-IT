#!/usr/bin/env python3
# coding:utf-8
import tkinter as tk
from tkinter import ttk
#import controller
from tkinter import simpledialog
from tkinter import messagebox
from functools import partial
HEADER_FRAME_WIDTH = 950
DEFAULT_KWARGS = {'side': tk.TOP, 'expand': True, 'fill': tk.X}
DISPLAY_CONTENT = "Individual assessment items must be solely your own work.While students are encouraged to have high-level conversation about problem they are"+\
" trying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically"+\
" detects similarity assignment submissions."


class HeaderFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self._important = tk.Message(
            master=self,
            text="Important",
            width=HEADER_FRAME_WIDTH,
            foreground="orange",
            font=('times', 24, 'bold'))
        self._important_content = tk.Message(
            master=self, text=DISPLAY_CONTENT, width=HEADER_FRAME_WIDTH)
        self._important.grid(row=0, column=0, sticky='we')
        self._important.config(anchor=tk.W)
        self._important_content.grid(row=1, column=0)


class QuestionContainerFrame(tk.Frame):
    def __init__(
            self,
            master,
            question_type,
            description,
            examples,
            external_func_dict,
            foreground="green",
    ):
        super().__init__(master=master)
        self._question_description_frame = QuestionDescriptionFrame(
            master=self,
            question_type=question_type,
            question_description=description,
            foreground=foreground)
        self._question_description_frame.grid(row=0, column=0, sticky='nwse')
        self._examples_frame = QuestionExampleFrame(
            master=self,
            question_type=question_type,
            question_examples=examples)
        self._examples_frame.grid(row=1, column=0, sticky='nwse')
        self._request_and_queue_frame = QuestionRequestAndQueenFrame(
            master=self,
            question_type=question_type,
            external_func_dict=external_func_dict,
            bg=f"light {foreground}")
        self._request_and_queue_frame.grid(row=2, column=0, sticky='nwse')


class QuestionDescriptionFrame(tk.Frame):
    def __init__(self,
                 master,
                 question_type,
                 question_description,
                 foreground="green"):
        super().__init__(master=master, bg=f"light {foreground}")
        self._question_type = tk.Message(
            master=self,
            text=question_type,
            foreground=foreground,
            width=HEADER_FRAME_WIDTH,
            bg=f"light {foreground}",
            font=('times', 36, 'bold'))
        self._question_description = tk.Message(
            master=self,
            width=HEADER_FRAME_WIDTH,
            text=question_description,
            bg=f"light {foreground}")
        self._question_type.grid(row=0, column=0, sticky='nwse')
        self._question_description.grid(row=1, column=0, sticky='nwse')


class QuestionExampleFrame(tk.Frame):
    def __init__(self, master, question_type, question_examples, *args,
                 **kwargs):
        super().__init__(master=master, *args, **kwargs)
        label = tk.Label(
            master=self, text="Some example of {}".format(question_type))
        label.grid(row=0, column=0, sticky='we')
        label.config(anchor=tk.W)
        for i, example in enumerate(question_examples):
            label = tk.Label(master=self, text="@ {}".format(example))
            label.grid(row=i + 1, column=0, sticky='we')
            label.config(anchor=tk.W)


class QuestionRequestAndQueenFrame(tk.Frame):
    def __init__(self,
                 master,
                 external_func_dict,
                 question_type,
                 bg="green",
                 interval=10000):
        super().__init__(master=master)
        self._master = master
        self._external_func_dict = external_func_dict
        self._request_submit_button = tk.Button(
            master=self,
            foreground="white",
            bg=bg,
            command=self.submit_request,
            text="Request {} Help".format(
                question_type.split()[0].capitalize()))
        self.grid_columnconfigure(index=0, weight=1)
        self._request_submit_button.grid(row=0, column=0)
        self._interval = interval
        self.refresh()

    def refresh(self, is_scheduled=True):
        for child in self.winfo_children():
            if type(child) is not tk.Button:
                child.destroy()
        self._waiting_msg_label = tk.Label(master=self)
        self._waiting_msg_label.grid(row=1, column=0, sticky='wens')
        columns, contents, queue_length, avg_waiting_time = self._external_func_dict[
            'data']()
        if contents:
            self._waiting_msg_label.config(
                text="An average wait time for {} for {} students".format(
                    self._external_func_dict['time'](avg_waiting_time),
                    queue_length))
            self._names_list = [content[0] for content in contents]
        else:
            self._waiting_msg_label.config(text="No students in the queue.")
            self._names_list = []
        self._waiting_list = ListView(
            master=self,
            columns_and_contents=(columns, contents),
            send_cancel_request=self._external_func_dict['cancel'],
            send_accepted_request=self._external_func_dict['accept'],
            width=300)
        self._waiting_list.grid(row=2, column=0)
        if is_scheduled:
            self._schedule = self.after(ms=self._interval, func=self.refresh)

    def cancel_refresh(self):
        self.after_cancel(id=self._schedule)

    def submit_request(self):
        self.cancel_refresh()
        student_name = simpledialog.askstring(
            "Input", "What is your name?", parent=self._master)
        if student_name not in self._names_list:
            question_content = simpledialog.askstring(
                "Input", "What is your question?", parent=self._master)
            if self._external_func_dict['submit'](
                    question_content=question_content,
                    student_name=student_name):
                print('submit succeed....')
            else:
                print('submit failed.....')
                return
        else:
            messagebox.showinfo(
                'Duplicate',
                'You are already in the queue, Please accept or cancel first.')
        self.refresh(is_scheduled=False)
        self._schedule = self.after(ms=self._interval, func=self.refresh)


class ListView(tk.Frame):
    def __init__(self, master, columns_and_contents, send_cancel_request,
                 send_accepted_request, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self._master = master
        self.columns, self.contents = columns_and_contents
        self.columns.insert(0, '#')
        for i, content in enumerate(self.contents):
            content.insert(0, i + 1)
        self._send_cancel_request = send_cancel_request
        self._send_accepted_request = send_accepted_request
        self.display_content()

    def update_columns_and_contents(self, columns_and_contents):
        self.columns, self.contents = columns_and_contents
        for i in range(len(self.columns) + 2):
            self.grid_columnconfigure(index=i, weight=1)

    def cancel_request(self, name):
        if self._send_cancel_request(name):
            print("cancel succeeded...")
            self._master.refresh()
        else:
            print('cancel failed..')
            self._master.cancel_refresh()

    def accepted_request(self, name):
        if self._send_accepted_request(name):
            print("accepted succeeded...")
            self._master.refresh()
        else:
            print("accepted failed..")
            self._master.cancel_refresh()

    def display_content(self):
        for i, column in enumerate(self.columns):
            label = tk.Label(master=self, text=column, width=15)
            label.grid(row=0, column=i)
        for i, row in enumerate(self.contents):
            name = row[1]
            id = i + 1
            for j, column in enumerate(row):
                tk.Label(master=self, text=str(column)).grid(row=id, column=j)
            tk.Button(
                master=self,
                bg="orange",
                command=partial(self.cancel_request, name)).grid(
                    row=id, column=len(self.columns))
            tk.Button(
                master=self,
                bg="green",
                command=partial(self.accepted_request, name)).grid(
                    row=id, column=len(self.columns) + 1)
