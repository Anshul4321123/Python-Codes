class Print:
    def __init__(self, value):
        global a
        self.a = value
        print(self.a)

    def print(self):
        print(self.a)


first = Print(5)


class Print2:
    def __init__(self, value):
        global a
        a=value
        self.a = a
        print(self.a)
    def print(self):
        print(self.a)

class Print3(Print2):
    def __init__(self, value):
        super().__init__(value)
        self.a = value + 5
        

    def print(self):
        print(self.a)


second = Print2(10)
first.print()
