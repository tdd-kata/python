"""
watch -n 0.1 pytest -v class.py
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.result = 0

    def greet(self):
        return "Hello, my name is {}.".format(self.name)

    def add(self, first, second):
        self.result += first + second
        return self.result


# 상속
# class 자식_클래스(부모_클래스)
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        else:
            return "C"


def test_person():
    person = Person("John")
    assert person.greet() == "Hello, my name is John."


def test_is_instance():
    john = Person("John")
    assert isinstance(john, Person)


def test_add():
    john = Person("John")
    assert john.add(1, 2) == 3
    assert john.add(2, 2) == 7
    assert john.add(3, 2) == 12


def test_child_class():
    john = Student("John", 12345)
    assert john.greet() == "Hello, my name is John."
    assert john.grade(90) == "A"
    assert john.grade(80) == "B"
    assert john.grade(70) == "C"
