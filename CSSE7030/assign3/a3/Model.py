import time
import math
import statistics


class Student(object):
    """ List of start time of the questions asked by a person"""
    def __init__(self, name):
        """ Construct a list of time when questions asked by a person

            Parameter:
                name (str): name of the person asks the questions
                time (Time): time of the questions been asked"""
        self._name = name
        self._questions_asked = []
        self._num = 0
        self._waited_time = []

    def get_name(self):
        """ Return the name of student asking questions"""
        return self._name
   
    def ask_question(self):
        """Add a time of new asked question to the list"""
        t = time.time()
        self._questions_asked.append(t)

    def get_num(self):
        """Return the number of questions have been asked by the person"""
        return self._num

    def get_time(self):
        """Return the lastest of times that student ask the questions"""
        return self._questions_asked[-1]

    def accept_question(self):
        """ the number of question asked increased by 1"""
        self._num += 1
        self._waited_time.append(self.wait_time()[0])
        
    def cancel_question(self):
        """ Remove the time of the question wanted to be cancel from list"""
        self._questions_asked.pop()

    def wait_time(self):
        """ the time a student wait"""
        end = time.time()
        self._wait_time = math.floor(end - self.get_time())
        mins = math.floor(self._wait_time/60)
        hours = math.floor(mins/60)
        if mins == 0 and hours == 0:
            self._display_wait_time = 'a few seconds ago'
        elif hours == 0:
            if mins == 1:
                self._display_wait_time = 'a minute ago'
            else:
                self._display_wait_time = '{} minutes ago'.format(mins)
        elif hours == 1:
            self._display_wait_time = '1 hour ago'
        else:
            self._display_wait_time = '{} hours ago'.format(hours)
        return (self._wait_time, self._display_wait_time)

    def display_wait_time(self):
        """ Display the wait time"""
        return self.wait_time()[1]

    def get_waited_time(self):
        """ return the waited time (in second) of each of the accepted question"""
        return self._waited_time

    def __str__(self):
        """ return the string representation of the student """
        return '{}'.format(self.get_name())

    def __repr__(self):
        """ return the string representation of the student """
        return self.__str__()


class History(object):
    """ History data """
    def __init__(self):
        self._history = []
        self.mean = 0
        self.median = 0
        self.mode = 0

    def get_history(self):
        """ return the list of history """
        return self._history

    def add_history(self, s):
        """ add a student into history

            Parameter:
                s (Student)"""
        position = 0
        if len(self._history) == 0:
            self._history.append(s)
            return
        else:
            for h in self._history:
                if h.get_name() == s.get_name():
                    self._history.remove(h)
            for h in self._history:
                if s.get_num() < h.get_num():
                    self._history.insert(position,s)
                    return
                else:
                    position += 1
            self._history.append(s)
            return

    def get_mean(self):
        """ return the mean wait time """
        wait_times = []
        if len(self._history) == 0:
            return 0
        else:
            for h in self._history:
                wait_times.extend(h.get_waited_time())
            average = sum(wait_times)//len(wait_times)
            return average
                      
    def get_median(self):
        """ return the median wait time """
        wait_times = []
        if len(self._history) == 0:
            return 0
        else:
            for h in self._history:
                wait_times.extend(h.get_waited_time())
            median = statistics.median_low(wait_times)
            return median

    def get_mode(self):
        """ return the mode wait time """
        wait_times = []
        if len(self._history) == 0:
            return 'None'
        else:
            for h in self._history:
                wait_times.extend(h.get_waited_time())
            wait_mins = [t//60 for t in wait_times]
            try:
                mode = statistics.mode(wait_mins)
                if mode == 0:
                    return 'Within a minute'
                elif mode == 1:
                    return '1 minute'
                elif mode < 60:
                    return '{} minutes'.format(mode)
                else:
                    wait_hrs = [t//60//60 for t in wait_times]
                    try:
                        mode = statistics.mode(wait_hrs)
                        if mode == 0:
                            return 'Within an hour'
                        elif mode == 1:
                            return 'Around 1 hour'
                        else:
                            return 'Around {} hours'.format(mode)
                    except statistics.StatisticsError:
                        return 'None'
            except statistics.StatisticsError:
                return 'None'

    def display(self, time):
        """ display the time

            Parameter:
                time (int)"""
        if time == 0:
            return 'None'
        if time == 1:
            return '1 second'
        elif time < 60:
            return '{} seconds'.format(time)
        elif time//60 == 1:
            return '1 min'
        elif time//60 < 60:
            return '{} mins'.format(time//60)
        elif time//60//60 >= 1:
            if time%60%60 == 0:
                if time//60//60 == 1:
                    return '{} hour'.format(time//60//60)
                else:
                    return '{} hours'.format(time//60//60)
            else:
                if time//60//60 == 1:
                    if time%60%60 == 1:
                        return '{} hour {} min'.format(time//60//60, time%60%60)
                    else:
                        return '{} hour {} mins'.format(time//60//60, time%60%60)
                else:
                    if time%60%60 == 1:
                        return '{} hours {} min'.format(time//60//60, time%60%60)
                    else:
                        return '{} hours {} mins'.format(time//60//60, time%60%60)

    
class Queue(object):
    """ list of queue"""
    def __init__(self, history): 
        """ Construct a queue list with student

            Parameter:
                student (Student) """
        self._queue = []
        self._history = history
        self._queue_state = True
        
    def get_state(self):
        """ return True if there is student add into queue
            return False if there is student remove from queue """
        return self._queue_state

    def add_queue(self, student, queue):
        """ add a student to a order queue list
                order the queue first by "Questions Asked" then by "Time"

            Parameter:
                student(Student)
                queue (Queue)
                
            return False if the student is already in the queue
            return True if the student can be added in the queue"""
        self._queue_state = True
        position = 0
        for s in queue.get_queue():         ### check whether having the same student in another queue
                if s.get_name() == student.get_name():
                    return False
        if len(self._queue) == 0:
            student.ask_question()
            self._queue.append(student)
            return True
        else:
            for s in self._queue:           ### check whether having the same student in the queue going to add into
                if s.get_name() == student.get_name():
                    return False            
            for s in self._queue:
                if student.get_num() < s.get_num():
                    student.ask_question()
                    self._queue.insert(position,student)
                    return True
                else:
                    position += 1
            student.ask_question()
            self._queue.append(student)
            return True
        
    def accept_queue(self, student):
        """ accept a student question, remove student from the queue list and add that student to the history list
            student asked a question"""
        self._queue_state = False
        for s in self._queue:
            if student.get_name() == s.get_name():
                s.accept_question()
                self._queue.remove(s)
                self._history.add_history(s)
    
    def cancel_queue(self, student):
        """ cancel a student question, remove student from the queue list
            student does not ask a question"""
        self._queue_state = False
        student.cancel_question()
        for s in self._queue:
            if student.get_name() == s.get_name():
                self._queue.remove(s)

    def get_num(self):
        """ return the number of students queue in the queue"""
        return len(self._queue)
        
    def get_queue(self):
        """ return the queue list"""
        return self._queue

