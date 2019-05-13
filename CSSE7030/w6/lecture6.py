class Student(object):
    def __init__(self, name,snum,address): # things in the bracket are arguments # why having self as a argument - object in class can interact with other (self as a identifier)
        """Constructor: Student(str,str)"""
        self._name = name # take a copy
        self._snum = snum
        self._address = address
        self._courses = []
        self._results = {}

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name    

    def get_snum(self):
        return self._snum

    def get_address(self):
        return self._address    

    def add_courses(self, courses):
        self._courses.extend(courses)

    def get_courses(self):
        return self._courses

#problem of add_results and the things after this
    def add_results(self, results):
        self._results.update(results)
        # results is dictionary

    def get_results(self):
        return self._results

    def __add__(self, f):
        return str(self._name) + ' and ' + str(f._name)

    def add_name_and_snum(self,f):
        return str(self._name)+str(self._snum)+' and '+str(f._name)+str(f._snum)


    def __str__(self):
        """ return the ame of the student
        __str__() --> str
        """
        
    
    def __repr__(self):
        return "Student({0},{1},{2})".format(self._name, self._snum, self._address)


class TransferStudent(Student):
    # subclass of Student
    def __init__(self, name, snum, address, transfer_uni):
        super().__init__(name, snum, address) # repeate the initialization
        self._transfer_uni = transfer_uni
        self._credit_courses = []

    def assign_credit(self, courses):
        self._credit_courses.extend(courses)

    def get_credit(self):
        return self._credit_courses

    def __repr__(self):
        # represent of the information of the object
        # if dont write this in the subclass, it will show the repr of the parent class - only name, snum and address
        return "TransferStudent({0},{1},{2},{3})".format(self._name, self._snum, self._address, self._transfer_uni)


## normally can put all the common attributes in the parent class & put the specific attributes for each subclass in the subclass

class Fees(object):
    def __init__(self):
        self._fee_per_course = 1000

    def calc_tuition_cost(self, student):
        no_of_courses = len(student.get_courses())
        discount = 0.1*self._fee_per_course * /9no_of_course-2)
        
        if no_of_courses >=3:
            course_fee = no_of_courses*self._fee==
        return no_of_courses * self._fee_per_course - discount




class Animal(object):
    def __init__(self,name):    # constructor of the class
        self._name = name

    def get_name(self):
        return self._name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'

    
        






