#!/usr/bin/python2.7
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
class Student(object):
    pass

    def __init__(self, name, score):
        self.name = name
        self.score = score
