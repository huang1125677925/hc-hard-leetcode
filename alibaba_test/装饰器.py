import time
from abc import abstractmethod


class test():
    def __new__(cls, a = 'huang'):
        print a
        
    def __init__(self):
        self.__new__()
        print 'facu'
        
    @abstractmethod
    def first(self):
        pass


from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    
    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration
a_function_requiring_decoration()
    
    
    
        

