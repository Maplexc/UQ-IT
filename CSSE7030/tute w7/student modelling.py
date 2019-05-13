
class Student(object):
    """Simple representation of a university student."""
    
    def __init__(self, name, student_num, degree):
        """Create a student with a name.
        
        Parameters:
            name (str): The student's name.
            student_num (int): the student number
            degree (str): the student's degree
        """
        self._name = name
        self._student_num = student_num
        self._degree = degree
        self._first_name, self._last_name = self._name.split()
        # split() V.S. partition()
        # split - e.g. 'you are beautiful'.split() → will get ['you', 'are', 'beautiful']
        self._course_grade = {}
        self._current_courses = []

    def get_name(self):
        """(str) Returns the name of the student."""
        return self._name

    def get_student_num(self):
        """(int) Returns the student number of the student."""
        return self._student_num

    def get_degree(self):
        """(str) Returns the degree of the student."""
        return self._degree

    def set_degree(self,new_degree):
        """ Change degree of student"""
        self._degree = new_degree

    def get_first_name(self):
        """ (str) Returns the first name of student"""
        return self._first_name

    def get_last_name(self):
        """ (str) Returns the last name of student"""
        return self._last_name

    def get_email(self):
        """ (str) Returns the student’s email address derived from their name
            in the format of firstname.lastname@uq.net.au
        """
        fname = self.get_first_name().lower()
        lname = self.get_last_name().lower()
        return "{0}.{1}@uq.net.au".format(fname,lname)
        # "{}.{}@uq.net.au".format(fname,lname) will also work

    def __str__(self):
        return "{0}({1}, {2}, {3})".format(self.get_name(),
                                           self.get_email(),
                                           self.get_student_num(),
                                           self.get_degree())
        # when using print()
    def __repr__(self):
        return "Student({0}, {1}, {2},{3})".format(self.get_name(),
                                                   self.get_student_num(),
                                                   self.get_degree(),
                                                   self._course_grade)
        # when return a value

    def add_grade(self,course,grade):
        course_code = course.get_course_code()
        self._course_grade[course_code] = grade
        
    def gpa(self):
        num_of_courses = len(self._course_grade)
        total_gpa = 0
        for key in self._course_grade:
            grade = self._course_grade[key]
            total_gpa += grade
        gpa = total_gpa/num_of_courses
        return gpa

    def current_courses(self, list_of_current_courses):
        for i in range(0,len(list_of_current_courses)):
            
        course_name = course.get_course_name()
        self._current_courses.append(course_name)
        

class Course(object):
    def __init__(self, course_code, course_name):
        self._course_code = course_code
        self._course_name = course_name

    def get_course_code(self):
        return self._course_code

    def get_course_name(self):
        return self._course_name
    
        
def check_student(list_of_students):
    """
    Return True if all students have different student numbers, if not return False

    Parameter:
        list_of_student (list): a list of Student objects
    """
    valid = True
    for i in range(0, len(list_of_students)):
        check_num = list_of_students[i].get_student_num()
        for k in range(i+1,len(list_of_students)):
            if list_of_students[k].get_student_num() == check_num:
                valid = False
                break
    return valid
    



    
    
