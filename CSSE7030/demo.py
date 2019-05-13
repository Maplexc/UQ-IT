class Person:
    def __init__(self, salary):
        self.salary = salary
    def __add__(self, other):
        return self.salary+other.salary
    def __eq__(self, other):
        return self.salary == other.salary
    
    
p1 = Person(salary=100)
p2 = Person(salary=100)
print(p1+p2)
print(p1==p2)
print(id(p1))
print(id(p2))