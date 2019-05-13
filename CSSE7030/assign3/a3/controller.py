import tkinter as tk
from tkinter import messagebox

class Queue_row(tk.Frame):
    """ row of queue"""
    def __init__(self, master, queue):
        super().__init__(master)
        self._master = master
        self._queue = queue
        self._id = 0

    def get_id(self):
        """ return row id """
        return self._id

    def set_id(self):
        """ set row id"""
        self._id = self._queue.get_num()
        
    def add_row(self, student):
        """ add one row to queue, 
            Parameter:
                student (Student)"""
        self._student = student
        self._num = tk.Label(self, text=self.get_id(), font=('Helvetica', 10), width = 2, bg = 'white')
        self._num.pack(side = tk.LEFT, anchor = tk.W)            
        self._name = tk.Label(self, text = self._student.get_name(), font=('Helvetica', 10), width = 15, bg = 'white')
        self._name.pack(side = tk.LEFT, anchor = tk.W)
        self._questions_asked = tk.Label(self, text = self._student.get_num(),
                                         font=('Helvetica', 10), width = 13, bg = 'white')
        self._questions_asked.pack(side = tk.LEFT, anchor = tk.W)
        self._time = tk.Label(self, text = self._student.display_wait_time(),
                              font=('Helvetica', 10), width = 15, bg = 'white')
        self._time.pack(side = tk.LEFT, anchor = tk.W)
        self._accept_button = tk.Button(self, bg = 'PaleGreen3', relief="groove",
                                        text='    ', font=('arial', 7), command=self.press_accept)
        self._accept_button.pack(side = tk.LEFT, anchor = tk.W, expand = 1)
        self._cancel_button = tk.Button(self, bg = 'red',relief="groove",
                                        text='    ', font=('arial', 7), command=self.press_cancel)
        self._cancel_button.pack(side = tk.LEFT, anchor = tk.W, expand = 1)

    def press_accept(self):
        """ accept the question, remove the row, return the student who accept the question"""
        self._queue.accept_queue(self._student)
        self.destroy()
        return self._student

    def press_cancel(self):
        """ accept the question, remove the row, return the student who cancel the question"""
        self._queue.cancel_queue(self._student)
        self.destroy()
        return self._student
        
    def update_row_details(self):
        """ update the row number, student name, questions asked"""
        if self._queue.get_state():
            s = self._queue.get_queue()[self.get_id()-1]
            if s.get_name() != self._student.get_name():
                self._student = s
                self._num.config(text = self._id)
                self._name.config(text = self._student.get_name())
                self._questions_asked.config(text = self._student.get_num())
        else:            
            for s in self._queue.get_queue():
                if s.get_name() == self._student.get_name():
                    if self._id == self._queue.get_queue().index(s):
                        self._id += 1
                    else:
                        self._id = self._queue.get_queue().index(s) + 1
                    self._student = s
                    self._num.config(text = self._id)
                    self._name.config(text = self._student.get_name())
                    self._questions_asked.config(text = self._student.get_num())
        self.after(10, self.update_row_details)
            
    def update_time(self):
        """ update time """
        for s in self._queue.get_queue():
            if s.get_name() == self._student.get_name():
                if self._time.winfo_exists() == True:
                    self._time.config(text = s.display_wait_time())
        self.after(1000, self.update_time)


class Statistics(tk.Frame):
    """ Statistics about the history of questions that have been asked """
    def __init__(self, master, quick_history, long_history, app):
        super().__init__(master)
        self._master = master
        self._app = app

        self._quick_history = quick_history
        self._long_history = long_history
        self.table_frame = tk.Frame(self)

    def add_summary(self):
        """ create a summary table about the mean, median, mode of each type of questions"""
        self.summary_frame = tk.Frame(self)
        self.summary_frame.pack(fill = tk.X, padx = 20)
        
        summary_label = tk.Label(self.summary_frame, text = 'Summary:', font=('Helvetica', 12))
        summary_label.pack(side = tk.TOP, anchor = tk.W, pady = (10,5))

        summary_title_frame = tk.Frame(self.summary_frame)
        summary_title_frame.pack(fill = tk.X)
        student_name_label = tk.Label(summary_title_frame, width = 14, font=('Helvetica', 12, 'bold'), bg = 'black', fg = 'white')
        student_name_label.pack(side = tk.LEFT, anchor = tk.W)
        quick_questions_label = tk.Label(summary_title_frame, text='Quick questions', width = 15, font=('Helvetica', 12, 'bold'), bg = 'black', fg = 'white')
        quick_questions_label.pack(side = tk.LEFT, anchor = tk.W)
        long_questions_label = tk.Label(summary_title_frame, text='Long questions', width = 15, font=('Helvetica', 12, 'bold'), bg = 'black', fg = 'white')
        long_questions_label.pack(side = tk.LEFT, anchor = tk.W)        
        title = ['Mean', 'Median', 'Mode']
        quick_statistics = [self._quick_history.display(self._quick_history.get_mean()),
                            self._quick_history.display(self._quick_history.get_median()),
                            self._quick_history.get_mode()]
        long_statistics = [self._long_history.display(self._long_history.get_mean()),
                           self._long_history.display(self._long_history.get_median()),
                           self._long_history.get_mode()]
        color = ['gray85', 'white', 'gray85']        
        for i in range(0,3):
            row_frame = tk.Frame(self.summary_frame)
            row_frame.pack(fill = tk.X)
            row_label = tk.Label(row_frame,text = '{} wait time'.format(title[i]),
                                 width = 15, font=('Helvetica', 10, 'bold'), bg = color[i], fg = 'black')
            row_label.pack(side = tk.LEFT, anchor = tk.W)
            quick_questions_label = tk.Label(row_frame, text= quick_statistics[i],
                                             width = 25, font=('Helvetica', 10), bg = color[i], fg = 'black')
            quick_questions_label.pack(side = tk.LEFT, anchor = tk.W)
            long_questions_label = tk.Label(row_frame, text= long_statistics[i],
                                            width = 15, font=('Helvetica', 10), bg = color[i], fg = 'black')
            long_questions_label.pack(side = tk.LEFT, anchor = tk.W)
            
    def add_checkbox(self):
        """ add a checkbox of question type
            return 1 if choose, return 0 if not choose"""
        label = tk.Label(self, text = 'The students who have asked the most questions:', font=('Helvetica', 12))
        label.pack(side = tk.TOP, anchor = tk.W, padx = 20, pady = (15,5))
        question_type = tk.Label(self, text = 'Question type:', font=('Helvetica', 11))
        question_type.pack(side = tk.TOP, anchor = tk.W, padx = 40)
        checkboxes = tk.Frame(self)
        checkboxes.pack(fill = tk.X)
        self.quickcheck = tk.IntVar()
        quick_check = tk.Checkbutton(checkboxes, text = 'Quick questions', font=('Helvetica', 10), variable = self.quickcheck)
        quick_check.pack(side = tk.LEFT, anchor = tk.W, padx = 40, pady = (0,5))
        self.longcheck = tk.IntVar()
        long_check = tk.Checkbutton(checkboxes, text = 'Long questions', font=('Helvetica', 10), variable = self.longcheck)
        long_check.pack(side = tk.LEFT, anchor = tk.W, padx = (30,10), pady = (0,5))
        get_button = tk.Button(checkboxes, text = 'Get', font = ('Helvetica', 10), command = self.get_table)
        get_button.pack(side = tk.LEFT, padx = 10)
        return (self.quickcheck.get(), self.longcheck.get())

    def get_quick_check(self):
        """ return True if quick questions checkbox is chosen"""
        return self.quickcheck.get() == 1

    def get_long_check(self):
        """ return True if long questions checkbox is chosen"""
        return self.longcheck.get() == 1

    def get_table(self):
        """ get the table """
        if self.table_frame.winfo_exists() == True:
            self.table_frame.destroy()
            self.table_frame = tk.Frame(self)
            self.table_frame.pack(fill = tk.X, padx = 20)
            self.table1 = tk.Frame(self.table_frame)
            self.table1.pack(side = tk.LEFT)
            if self.get_quick_check() == False and self.get_long_check() == False:
                notice = tk.Toplevel()
                notice.title('Notice')
                notice_label = tk.Label(notice, text = "Please choose at least one type of question")
                notice_label.pack(padx = 20, pady = (20,10))
                button = tk.Button(notice, text = 'ok', command = notice.destroy)
                button.pack(pady = 10, ipadx = 10)
            else:
                if self.get_quick_check() == True and self.get_long_check() == False:
                    if len(self._quick_history.get_history()) == 0:
                        nolabel = tk.Label(self.table1, text = 'There is no history of quick question')
                        nolabel.pack(padx = 20)
                    else:
                        self.add_column_names(self.table1)
                        self.add_row_table(self.table1, self._quick_history)
                ## add quick history table
                elif self.get_quick_check() == False and self.get_long_check() == True:
                    if len(self._long_history.get_history()) == 0:
                        nolabel = tk.Label(self.table1, text = 'There is no history of long question')
                        nolabel.pack(padx = 20)
                    else:
                        self.add_column_names(self.table1)
                        self.add_row_table(self.table1, self._long_history)
                ## add long history table
                elif self.get_quick_check() and self.get_long_check():
                    if len(self._quick_history.get_history()) == 0:
                        nolabel = tk.Label(self.table1, text = 'There is no history of quick question')
                        nolabel.pack(padx = 20)
                    else:
                        quick_label = tk.Label(self.table1, text = 'Quick question')
                        quick_label.pack()
                        self.add_column_names(self.table1)
                        self.add_row_table(self.table1, self._quick_history)

                    self.table2 = tk.Frame(self.table_frame)
                    self.table2.pack(side = tk.LEFT)
                    if len(self._long_history.get_history()) == 0:
                        nolabel = tk.Label(self.table2, text = 'There is no history of long question')
                        nolabel.pack(padx = 20)
                    else:
                        long_label = tk.Label(self.table2, text = 'Long question')
                        long_label.pack()
                        self.add_column_names(self.table2)
                        self.add_row_table(self.table2, self._long_history)
    
    def add_column_names(self, frame):
        """ add a row of column names"""
        column_title_row = tk.Frame(frame)
        column_title_row.pack()
        student_name_label = tk.Label(column_title_row, text='Student name', width = 20, font=('Helvetica', 11, 'bold'), bg = 'black', fg = 'white')
        student_name_label.pack(side = tk.LEFT, anchor = tk.W)
        num_questions_label = tk.Label(column_title_row, text='Number of Questions asked', width = 25, font=('Helvetica', 11, 'bold'), bg = 'black', fg = 'white')
        num_questions_label.pack(side = tk.LEFT, anchor = tk.W)

    def add_row_table(self, frame, history):
        """ add a row to table"""
        color = ['gray85','white']        
        if len(history.get_history()) >= 10:
            end = 10
        else:
            end = len(history.get_history())
        history_list = history.get_history()[::-1]
        for i in range(0,end):
            row_frame = tk.Frame(frame)
            row_frame.pack(fill = tk.X, padx = 20)
            student = history_list[i]
            student_name_label = tk.Label(row_frame, text= student.get_name(),
                                          width = 20, font=('Helvetica', 11), bg = color[i%2], fg = 'black')
            student_name_label.pack(side = tk.LEFT, anchor = tk.W)
            num_questions_label = tk.Label(row_frame, text= student.get_num(),
                                           width = 25, font=('Helvetica', 11), bg = color[i%2], fg = 'black')
            num_questions_label.pack(side = tk.LEFT, anchor = tk.W)

    def add_buttons(self):
        """ add the clear history button """
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(side = tk.BOTTOM)
        clear_button = tk.Button(buttons_frame, text = 'Clear history', command = self._app.clear_history)
        clear_button.pack(side = tk.LEFT, padx = 30, pady = (20,0))

