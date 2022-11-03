class Student:
    """class description of student"""

    def __init__(self, name, age,mark=4, alive=True):
        self.name = name
        self.age = age
        self.mark = mark
        self.alive = alive

    def __str__(self):
        msg = self.name
        msg += (" is still alive " if self.alive else " is dead ")
        msg += "(mark: " + str(self.mark) + ")"

        return msg
