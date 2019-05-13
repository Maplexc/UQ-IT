"""
Simple inheritance exercise to demonstrate overriding a method from a superclass.
"""

__copyright__ = "Copyright 2018, University of Queensland"


class Student(object) :
    """Simple model of a university student"""
    def __init__(self, name, student_num):
        """
        Parameters:
            name (str): The student's name in "first_name last_name" format.
            student_num (str): The student's unique student id number.
        """
        self._name = name
        self._student_num = student_num
        self._enrolments = []  # list of tuples (course code, tuition fee)

    def get_name(self) :
        """(str) Returns the name of the student "first_name last_name"."""
        return self._name

    def get_student_num(self) :
        """(str) Returns the students student number."""
        return self._student_num

    def enrol(self, course_code, fee) :
        """Enrol in a course, at a given fee.

        Parameters:
            course_code (str): Unique course code in which Student is enrolling.
            fee (int): The fee for taking this course (in whole dollar amount).

        Preconditions:
            fee > 0
        """
        self._enrolments.append((course_code, fee))

    def get_enrolments(self) :
        """list<(str, in)> Return a list of courses the student is enrolled in."""
        return self._enrolments

    def calculate_fees(self) :
        """Compute the total tuition fees for the student.
        
        Return:
            int: Total tuition fees for this Student.
        """
        total = 0
        for course_code, fee in self._enrolments :
            total += fee
        return total


# Define your CollegeStudent class here
class CollegeStudent(Student):
    def __init__(self, name, student_num, college_name, c_fee):
        super().__init__(name, student_num)
        self._c_name = college_name
        self._c_fee = c_fee

    def get_college(self):
        return self._c_name

    def calculate_fees(self):
        return super().calculate_fees() + self._c_fee
#        tuition_fees = super().calculate_fees()
#        return tuition_fees + self._c_fee
    

    
