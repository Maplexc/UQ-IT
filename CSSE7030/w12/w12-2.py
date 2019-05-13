class Foo(object):
    @classmethod # (compare to class) dont need to create a object to call the method
                 # can direcly call the method
    def hello(cls,caller = 'Tim'):  # cls - represent the self
        print('hello from {}'.format(caller))
        print('hello from {}'.format(cls.__name__)) # print the name of the class

    @staticmethod # like a regular method can put inside the class
    def hello2(caller = 'Mary'): # don't need any specific argument, can be anything
        print('hello from {}'.format(caller))
            
