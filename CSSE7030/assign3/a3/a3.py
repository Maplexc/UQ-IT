import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import time
from Model import *
from controller import *
from tkinter import ttk
import webbrowser
from game_view import *

__author__ = "Xin Chen 45189915"

class App(tk.Frame):
    """ App for student queue"""
    def __init__(self, master):
        """ Constract a student queue header"""
        super().__init__(master)
        master.config(bg='white')
        self._master=master
        self._master.title("CSSE1001/CSSE7030 Queue")
        self._master.geometry("1000x650")
        self.important()
        self.quick_description()
        self.long_description()
        self.queuetop1_quick()
        self.queuetop1_long()
        self.queuetop2(self._frame_quick)
        self.queuetop2(self._frame_long)
        self.long_history = History()
        self.quick_history = History()
        self.quick_queue = Queue(self.quick_history)
        self.long_queue = Queue(self.long_history)
        self._frame_quick_queue = tk.Frame(self._frame_quick, bg = 'white')
        self._frame_quick_queue.pack(fill=tk.X,padx = 20)
        self._frame_long_queue = tk.Frame(self._frame_long, bg = 'white')
        self._frame_long_queue.pack(fill=tk.X,padx = 20)
        self.add_menu()

    def add_statistics(self):
        """ create a top level window to display statistics about the history of questions that have been asked"""
        self.toplevel = tk.Toplevel()
        self.toplevel.title('Statistics about the history data')
        self.statistics = Statistics(self.toplevel, self.quick_history, self.long_history, self)
        self.statistics.pack(fill = tk.X)
        self.statistics.add_summary()
        self.statistics.add_checkbox()
        button = tk.Button(self.statistics, text = 'Close', command = self.toplevel.destroy)
        button.pack(side = tk.BOTTOM, pady = 15)
        self.statistics.add_buttons()      


    def clear_history(self):
        """ clear the history """
        self.long_history = History()
        self.quick_history = History()
        self.quick_queue = Queue(self.quick_history)
        self.long_queue = Queue(self.long_history)
        self._frame_quick_queue.destroy()
        self._frame_long_queue.destroy()
        self._frame_quick_queue = tk.Frame(self._frame_quick, bg = 'white')
        self._frame_quick_queue.pack(fill=tk.X,padx = 20)
        self._frame_long_queue = tk.Frame(self._frame_long, bg = 'white')
        self._frame_long_queue.pack(fill=tk.X,padx = 20)        
        try:
            self.statistics.destroy()
            self.statistics = Statistics(self.toplevel, self.quick_history, self.long_history, self)
            self.statistics.pack(fill = tk.X)
            self.statistics.add_summary()
            self.statistics.add_checkbox()
            button = tk.Button(self.statistics, text = 'Close', command = self.toplevel.destroy)
            button.pack(side = tk.BOTTOM, pady = 15)
            self.statistics.add_buttons()      
        except:
            pass
    
    def add_menu(self):
        """ create a menu"""
        menu = tk.Menu(self._master)
        file = tk.Menu(menu)
        file.add_separator()
        file.add_command(label = 'Course profile', command = self.get_courseprofile)
        file.add_command(label = 'Statistics', command = self.add_statistics)
        subclear = tk.Menu(file, tearoff = 0)
        subclear.add_command(label = 'Quick queue', command = self.clear_quick_queue)
        subclear.add_command(label = 'Long queue', command = self.clear_long_queue)
        subclear.add_command(label = 'All queue', command = self.clear_queue)
        subclear.add_command(label = 'History', command = self.clear_history)
        file.add_cascade(label = 'Clear', menu = subclear)
        file.add_command(label = 'Exit', command = self._master.destroy)
        menu.add_cascade(label = 'File', menu = file)
        helpmenu = tk.Menu(menu)
        helpmenu.add_command(label = 'Python Visualization Tool', command = self.get_visual)
        helpmenu.add_command(label = 'Python Documentation', command = self.get_python_doc)
        helpmenu.add_command(label = 'An Introduction to Tkinter', command = self.get_tkinter_doc)
        menu.add_cascade(label = 'Help', menu = helpmenu)
        takeabreakmenu = tk.Menu(menu)
        takeabreakmenu.add_command(label = 'Tower of Hanoi', command = self.get_game)
        menu.add_cascade(label = 'Take a break', menu = takeabreakmenu)
        self._master.config(menu = menu)

    def get_game(self):
        """ open the game """
        game_toplevel = tk.Toplevel()
        game_toplevel.title('Tower of hanoi')
        game = Game(game_toplevel)
    
    def get_courseprofile(self):
        """ open the course profile webpage """
        webbrowser.open('http://www.courses.uq.edu.au/student_section_loader.php?section=1&profileId=92857')

    def get_visual(self):
        """ open the visualization tool webpage """
        webbrowser.open('http://pythontutor.com/visualize.html#mode=edit')

    def get_python_doc(self):
        """ open the python documentation webpage """
        webbrowser.open('https://docs.python.org/3.6/')

    def get_tkinter_doc(self):
        """ open the tkinter documentation webpage """
        webbrowser.open('http://effbot.org/tkinterbook/')
        
    def clear_queue(self):
        """ clear all the queue"""
        self._frame_quick_queue.destroy()
        self._frame_long_queue.destroy()
        self._frame_quick_queue = tk.Frame(self._frame_quick, bg = 'white')
        self._frame_quick_queue.pack(fill=tk.X,padx = 20)
        self._frame_long_queue = tk.Frame(self._frame_long, bg = 'white')
        self._frame_long_queue.pack(fill=tk.X,padx = 20)
        self.quick_queue = Queue(self.quick_history)
        self.long_queue = Queue(self.long_history)
    
    def clear_quick_queue(self):
        """ clear the quick queue"""
        self._frame_quick_queue.destroy()
        self._frame_quick_queue = tk.Frame(self._frame_quick, bg = 'white')
        self._frame_quick_queue.pack(fill=tk.X,padx = 20)
        self.quick_queue = Queue(self.quick_history)

    def clear_long_queue(self):
        """ clear the long queue"""
        self._frame_long_queue.destroy()
        self._frame_long_queue = tk.Frame(self._frame_long, bg = 'white')
        self._frame_long_queue.pack(fill=tk.X,padx = 20)
        self.long_queue = Queue(self.long_history)
    
    def get_quick_queue(self):
        """ return the quick queue frame"""
        return self._frame_quick_queue

    def get_long_queue(self):
        """ return the long queue frame"""
        return self._frame_long_queue

    ### queue header
    def important(self):
        """Constract a important notice"""
        self._frame_important = tk.Frame(self._master, bg = '#fefbed')
        self._frame_important.pack(side=tk.TOP, fill = tk.X)
        self._label_important_title = tk.Label(self._frame_important, text='Important',
                                               font=('Helvetica', 12, 'bold'), fg = '#c09853',
                                               bg = '#fefbed')
        self._label_important_title.pack(anchor = tk.NW, padx = 20, pady =(20,0))
        self._message_important = tk.Message(self._frame_important,text = "Individual assessment items must be solely your own work. While students are encouragd to have high-level conversations about the problems they are trying to solve, you must not look at another student's code or copy from it. The university uses sophisticated anti-collusion measures to automatically detect similarity between assignment submissions.", 
                                             font=('Helvetica', 10),
                                             bg = '#fefbed', width = 980)
        self._message_important.pack(side = tk.TOP, anchor = tk.W, padx=20, ipady=10)

    def quick_description(self):
        """Constract the description of quick question"""
        self._frame_quick = tk.Frame(self._master, bg = 'white')
        self._frame_quick.pack(side = tk.LEFT, expand=1, fill=tk.BOTH)
        self._frame_quick_label = tk.Frame(self._frame_quick, bg= '#dff0d8',
                                     borderwidth=1, relief="ridge")
        self._frame_quick_label.pack(padx=20, pady=15, fill=tk.X)
        self._label_quick = tk.Label(self._frame_quick_label, text='Quick Questions',
                                     font=('Helvetica', 16, 'bold'), fg = '#3c763d',
                                     bg = '#dff0d8')
        self._label_quick.pack(pady=15, fill=tk.X)
        self._label_quick_describe = tk.Label(self._frame_quick_label, text = "< 2 mins with a tutor",
                                              font=('Helvetica', 10),
                                              bg = '#dff0d8')
        self._label_quick_describe.pack(pady = (5,10))
        self._message_quick_detail = tk.Message(self._frame_quick,
                                                text = "Some examples of quick questions:\
                                                        · Syntax errors\
                                                        · Interpreting error output\
                                                        · Assignment/MyPyTutor interpretation\
                                                        · MyPyTutor submission issues",
                                                font=('Helvetica', 10), anchor=tk.W,
                                                width = 240, bg = 'white')
        self._message_quick_detail.pack(side = tk.TOP, padx = 20, fill=tk.X)
        self._quick_button = tk.Button(self._frame_quick, text = 'Request Quick Help',
                                       fg = 'White', bg = '#449d44',
                                       borderwidth=2, relief="groove",
                                       command=self.pressQuick)
        self._quick_button.pack(ipadx = 5, ipady = 5, pady = 10)

    def long_description(self):
        """Constract the description of long question"""
        self._frame_long = tk.Frame(self._master, bg = 'white')
        self._frame_long.pack(side = tk.LEFT, expand=1, fill=tk.BOTH)
        self._frame_long_label = tk.Frame(self._frame_long, bg= '#d9edf7',
                                          borderwidth=1, relief="ridge")
        self._frame_long_label.pack(padx=20, pady=15, fill=tk.X)        
        self._label_long = tk.Label(self._frame_long_label, text='Long Questions',
                                    font=('Helvetica', 16, 'bold'), fg = '#31708f',
                                    bg = '#d9edf7')
        self._label_long.pack(pady=15, fill=tk.X)
        self._label_long_describe = tk.Label(self._frame_long_label, text="> 2 mins with a tutor",
                                             font=('Helvetica', 10),
                                             bg = '#d9edf7')
        self._label_long_describe.pack(pady = (5,10))
        self._message_long_detail = tk.Message(self._frame_long,
                                                text = "Some examples of long questions:\
                                                        · Open endeed questions\
                                                        · How to start a problem\
                                                        · How to improve code\
                                                        · Debugging\
                                                        · Assignment help",
                                                font=('Helvetica', 10), anchor=tk.W,
                                                width = 240, bg = 'white')
        self._message_long_detail.pack(side = tk.TOP, padx = 20, fill=tk.X)
        self._long_button = tk.Button(self._frame_long, text = 'Request Long Help',
                                       fg = 'White', bg = '#31b0d5',
                                       borderwidth=2, relief="groove",
                                       command=self.pressLong)
        self._long_button.pack(ipadx = 5, ipady = 5, pady = 10)
    
    def queuetop1_quick(self):
        """Constract the quick queue header"""
        line1 = tk.Canvas(self._frame_quick, bg = 'white', highlightthickness=0, height = 10)
        line1.pack(side=tk.TOP, fill=tk.X, padx = 20)
        line1.create_line(0,0,500,0, fill='grey78')

        self.label_numofstudent_quick = tk.Label(self._frame_quick,text = '{} students in queue.'.format('No'),
                                           bg = 'white')
        self.label_numofstudent_quick.pack(anchor = tk.W, padx = 20)
        self.label_numofstudent_quick.after(100, self.update_quick_total)

    def queuetop1_long(self):
        """Constract the long queue header"""
        line1 = tk.Canvas(self._frame_long, bg = 'white', highlightthickness=0, height = 10)
        line1.pack(side=tk.TOP, fill=tk.X, padx = 20)
        line1.create_line(0,0,500,0, fill='grey78')

        self.label_numofstudent_long = tk.Label(self._frame_long,text = '{} students in queue.'.format('No'),
                                           bg = 'white')
        self.label_numofstudent_long.pack(anchor = tk.W, padx = 20)
        self.label_numofstudent_long.after(100, self.update_long_total)
    
    def queuetop2(self, frame):
        """ Constract a row with queue column name"""
        canvas = tk.Canvas(frame, bg = 'white', highlightthickness=0, height = 40)
        canvas.pack(side=tk.TOP, fill=tk.X, padx = 20)
        canvas.create_line(0,5,500,5, fill='grey78')
        canvas.create_text(160,20, text='#                   Name                   Questions Asked           Time',
                           font=('Helvetica', 9, 'bold'))
        canvas.create_line(0,35,500,35, fill='grey78')
    
    def get_total_long(self):
        """ return the number of students in long queue"""
        if self.long_queue.get_num() == 0:
            return 'No'
        else:
            return self.long_queue.get_num()

    def get_total_quick(self):
        """ return the number of students in quick queue"""
        if self.quick_queue.get_num() == 0:
            return 'No'
        else:
            return self.quick_queue.get_num()
        
    def update_long_total(self):
        """ update the label showing the number of students in long queue"""
        self.label_numofstudent_long.config(text = '{} students in queue.'.format(self.get_total_long()))
        self.label_numofstudent_long.after(100, self.update_long_total)

    def update_quick_total(self):
        """ update the label showing the number of students in quick queue"""
        self.label_numofstudent_quick.config(text = '{} students in queue.'.format(self.get_total_quick()))
        self.label_numofstudent_quick.after(100, self.update_quick_total)
        
    ### command
    def pressQuick(self):
        """ Command of pressing the request quick help button, add student into quick queue"""
        name = simpledialog.askstring('Request Quick Help','Please enter your name:')
        if name is not None:
            if len(name.strip()) == 0:
                messagebox.showinfo("Notice", "Please enter a name!")
            else:
                student = Student(name)
                for h in self.quick_history.get_history():
                    if student.get_name() == h.get_name():
                        student = h
                if self.quick_queue.add_queue(student, self.long_queue):
                    row = Queue_row(App.get_quick_queue(self), self.quick_queue)
                    row.pack()
                    row.set_id()
                    row.add_row(student)    
                    row.after(1, row.update_row_details)
                    row.after(1, row.update_time)
                    notification = tk.Toplevel()
                    notification.title('Notice')
                    average_notice = tk.Label(notification, text = 'Average waiting time for quick queue: {}'.format(self.quick_history.display(self.quick_history.get_mean())))
                    average_notice.pack(anchor = tk.W, padx = 25, pady = (20,5))
                    notice = tk.Message(notification, text = 'Menu --> Help: can find some resources might help you \
                                                              Menu --> Take a break: can play a game to have a rest',width = 400)
                    notice.pack(padx = 20, pady = (0,10))
                    emoji = tk.Label(notification, text = '^v^')
                    emoji.pack(pady = (0,20))
                    notification.after(4500, notification.destroy)
                    
                else:
                    messagebox.showinfo("Notice", "You are already in a queue")   

    def pressLong(self):
        """ Command of pressing the request long help button, add student into long queue"""
        name = simpledialog.askstring('Request Long Help','Please enter your name:')
        if name is not None:
            if len(name.strip()) == 0:
                messagebox.showinfo("Notice", "Please enter a name!")
            else:
                student = Student(name)
                for h in self.long_history.get_history():
                    if student.get_name() == h.get_name():
                        student = h
                if self.long_queue.add_queue(student, self.quick_queue):
                    row = Queue_row(App.get_long_queue(self), self.long_queue)
                    row.pack()
                    row.set_id()
                    row.add_row(student)
                    row.after(1, row.update_row_details)
                    row.after(1, row.update_time)
                    notification = tk.Toplevel()
                    notification.title('Notice')
                    average_notice = tk.Label(notification, text = 'Average waiting time for long queue: {}'.format(self.long_history.display(self.long_history.get_mean())))
                    average_notice.pack(anchor = tk.W, padx = 25, pady = (20,5))
                    notice = tk.Message(notification, text = 'Menu --> Help: can find some resources might help you \
                                                              Menu --> Take a break: can play a game to have a rest',width = 400)
                    notice.pack(padx = 20, pady = (0,10))
                    emoji = tk.Label(notification, text = '^v^')
                    emoji.pack(pady = (0,20))
                    notification.after(4500, notification.destroy)
                else:
                    messagebox.showinfo("Notice", "You are already in a queue")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':   
    main()
