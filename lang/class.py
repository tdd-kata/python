"""
watch -n 0.1 pytest -v class.py
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, my name is {}.".format(self.name)

def test_person():
    person = Person("John")
    assert person.greet() == "Hello, my name is John."

def test_is_instance():
    john = Person("John")
    assert isinstance(john, Person)
