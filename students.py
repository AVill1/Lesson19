class Student:
    """class description of student"""

    def __init__(self, name, age,mark=4, alive=True):
        self._name = name
        self._age = age
        self._mark = mark
        self._alive = alive

    def __str__(self):
        msg = self._name
        msg += (" is still alive " if self._alive else " is dead ")
        msg += "(mark: " + str(self._mark) + ")"

        return msg

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    mark = property(get_mark, set_mark)
    alive = property(get_alive, set_alive)