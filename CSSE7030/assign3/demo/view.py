#!/usr/bin/env python3
# coding:utf-8
import tkinter as tk
from tkinter import ttk
import controller
from functools import partial
from tkinter import simpledialog
quick, long = controller.generate_quick_and_long_question_queue_container()
scheduler = controller.get_scheduler()
quick.submit_question("leslie", "what the fuck")
quick.submit_question("binbin", "how are you")
quick.submit_question("leslie", "so what")

HEADER_FRAME_WIDTH = 950
BACK_GROUND_TEMPLATE = "light {}"
PAD_X = 12
DEFAULT_KWARGS = {'side': tk.TOP, 'expand': True, 'fill': tk.X}
REQUEST_HELP_TEMPLATE = "Request {} Help"


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
            master=self,
            text=controller.DISPLAY_CONTENT,
            width=HEADER_FRAME_WIDTH)
        self._important.pack(side=tk.TOP, anchor=tk.W)
        self._important_content.pack(side=tk.TOP, anchor=tk.W)


class QuestionContainerFrame(tk.Frame):
    def __init__(self, master, questioncontainer, foreground="green"):
        super().__init__(
            master=master, bg=BACK_GROUND_TEMPLATE.format(foreground))
        self._question_description_frame = QuestionDescriptionFrame(
            master=self,
            questioncontainer=questioncontainer,
            foreground=foreground)
        self._question_description_frame.pack()
        self._examples_frame = QuestionExampleFrame(
            master=self, questioncontainer=questioncontainer)
        self._examples_frame.pack(**DEFAULT_KWARGS)
        self._request_and_queue_frame = QuestionRequestAndQueenFrame(
            master=self,
            questioncontainer=questioncontainer,
            bg=BACK_GROUND_TEMPLATE.format(foreground))
        self._request_and_queue_frame.pack(**DEFAULT_KWARGS)


class QuestionDescriptionFrame(tk.Frame):
    def __init__(self, master, questioncontainer, foreground="green"):
        super().__init__(
            master=master, bg=BACK_GROUND_TEMPLATE.format(foreground))
        self._question_type = tk.Message(
            master=self,
            text=questioncontainer,
            foreground=foreground,
            width=HEADER_FRAME_WIDTH,
            bg=BACK_GROUND_TEMPLATE.format(foreground),
            font=('times', 36, 'bold'))
        self._question_description = tk.Message(
            master=self,
            width=HEADER_FRAME_WIDTH,
            text=questioncontainer.description,
            bg=BACK_GROUND_TEMPLATE.format(foreground))
        self._question_type.pack(**DEFAULT_KWARGS)
        self._question_description.pack(**DEFAULT_KWARGS)


class QuestionExampleFrame(tk.Frame):
    def __init__(self, master, questioncontainer, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        tk.Label(
            master=self,
            text="Some example of {}".format(
                questioncontainer.question_type)).pack(anchor=tk.W)
        for example in questioncontainer.examples:
            tk.Label(
                master=self, text="@ {}".format(example)).pack(anchor=tk.W)


class QuestionRequestAndQueenFrame(tk.Frame):
    def __init__(self, master, questioncontainer, bg="green", interval=5000):
        super().__init__(master=master)
        self._master = master
        self._questioncontainer = questioncontainer
        self._request_submit_button = tk.Button(
            master=self,
            foreground="white",
            bg=bg,
            command=self.submit_request,
            text=REQUEST_HELP_TEMPLATE.format(
                self._questioncontainer.question_type[0].capitalize()))
        self._request_submit_button.pack()
        self._interval = interval
        self.refresh()

    def refresh(self, is_scheduled=True):
        for child in self.winfo_children():
            if type(child) is not tk.Button:
                child.destroy()
        kwargs = DEFAULT_KWARGS.copy()
        kwargs['fill'] = tk.BOTH
        self._waiting_msg_box = tk.Message(master=self)
        self._waiting_msg_box.pack(**kwargs)
        columns, contents = controller.get_columns_and_content_from_queue(
            self._questioncontainer.waiting_queue)
        if contents:
            queue_length, avg_waiting_time = controller.get_queue_length_and_average_waiting_time(
                queue=self._questioncontainer.waiting_queue)
            self._waiting_msg_box.config(
                text="{} budies waiting, average time:{}".format(
                    queue_length, avg_waiting_time))
        else:
            self._waiting_msg_box.config(text="Nobody is wating...")
        self._waiting_list = ListView(
            master=self, columns_and_contents=(columns, contents), width=300)
        self._waiting_list.pack(**kwargs)
        if is_scheduled:
            self._schedule = self.after(ms=self._interval, func=self.refresh)
            print(self._schedule)

    def submit_request(self):
        self.after_cancel(id=self._schedule)
        student_name = simpledialog.askstring(
            "Input", "What is your name?", parent=self._master)
        question_content = simpledialog.askstring(
            "Input", "What is your question?", parent=self._master)
        controller.submit_request(
            question_content=question_content,
            student_name=student_name,
            questioncontainer=self._questioncontainer)
        self.refresh(is_scheduled=False)
        self._schedule = self.after(ms=self._interval, func=self.refresh)


class ListView(tk.Frame):
    def __init__(self, master, columns_and_contents, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self._master = master
        self.column_frame = tk.Frame(master=self)
        self.column_frame.pack(**DEFAULT_KWARGS)
        self.content_frame = tk.Frame(master=self)
        self.content_frame.pack(**DEFAULT_KWARGS)
        self.columns, self.contents = columns_and_contents
        self.display_content()

    def update_columns_and_contents(self, columns_and_contents):
        self.columns, self.contents = columns_and_contents

    def delete_item(self, id, isCanceled):
        controller.remove_entity_from_queue(
            questioncontainer=self._master._questioncontainer,
            id=id,
            isCanceled=isCanceled)
        print("delete_item executed...")
        self._master.refresh()

    def display_content(self):
        kwargs = DEFAULT_KWARGS.copy()
        kwargs['side'] = tk.LEFT
        for column in self.columns:
            label = tk.Label(master=self.column_frame, width=15, text=column)
            label.pack(side=tk.LEFT)
        #tk.Button(master=self.column_frame, bg="black").pack(side=tk.LEFT)
        #tk.Button(master=self.column_frame, bg="black").pack(side=tk.LEFT)
        for i, row in enumerate(self.contents):
            id = i + 1
            row_frame = tk.Frame(master=self.content_frame)
            row_frame.pack(**DEFAULT_KWARGS)
            for column in row:
                tk.Label(
                    master=row_frame, width=15,
                    text=str(column)).pack(side=tk.LEFT)

            tk.Button(
                master=row_frame,
                bg="orange",
                command=partial(self.delete_item, id, True)).pack(
                    side=tk.LEFT, expand=True, fill=tk.X)
            tk.Button(
                master=row_frame,
                bg=BACK_GROUND_TEMPLATE.format("green"),
                command=partial(self.delete_item, id, False)).pack(
                    side=tk.LEFT, expand=True, fill=tk.X)


class App:
    def __init__(self, master):
        self._master = master
        self._master.geometry("{width}x{height}+0+0".format(
            width=self._master.winfo_screenwidth(),
            height=self._master.winfo_screenheight()))
        self._header_frame = HeaderFrame(self._master)
        self._header_frame.pack(fill=tk.X, side=tk.TOP)
        container_frame = tk.Frame(master=self._master)
        container_frame.pack(fill=tk.X, side=tk.TOP)
        self._quick_container = QuestionContainerFrame(
            master=container_frame, questioncontainer=quick)
        self._long_container = QuestionContainerFrame(
            master=container_frame, questioncontainer=long, foreground="blue")
        kwargs_dict = DEFAULT_KWARGS.copy()
        kwargs_dict['side'] = tk.LEFT
        kwargs_dict['padx'] = PAD_X
        self._quick_container.pack(**kwargs_dict)
        self._long_container.pack(**kwargs_dict)

    def start(self):
        self._master.mainloop()


def main():
    App(master=tk.Tk()).start()


if __name__ == "__main__":
    main()
