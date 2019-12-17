from itertools import count


class Animal:
    ids = count(start=10001)
    animals = []

    def __init__(self, name):
        self.name = name.title()
        self.id = next(self.ids)
        self.animals.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join(str(animal) for animal in cls.animals)
