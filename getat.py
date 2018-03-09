class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if item=='score':
            return 99


s=Student()
s.score