import random
import string

class Robot:
    """class to create a robot and name it"""
    def __init__(self):
        self._name = ''  # começa sem nome

    @property
    def name(self):
        if self._name == '':
            self._name = self.new_name()
        return self._name

    def new_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=3))
        return letters + digits

    def reset(self):
        if self._name == self.new_name():
            self._name = self.new_name()


    
            