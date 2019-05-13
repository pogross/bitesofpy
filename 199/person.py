# see __mro__ output in Bite description


class Person(object):
    def __init__(self):
        self.description = "I am a person"

    def __str__(self):
        return self.description


class Father(Person):
    def __init__(self):
        super(Father, self).__init__()
        self.description += " and cool daddy"


class Mother(Person):
    def __init__(self):
        super(Mother, self).__init__()
        self.description += " and awesome mom"


class Child(Father, Mother):
    def __init__(self):
        super(Child, self).__init__()
        self.description = "I am the coolest kid"
