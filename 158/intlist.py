import statistics


class IntList(list):
    @property
    def mean(self):
        return statistics.mean(self)

    @property
    def median(self):
        return statistics.median(self)

    def append(self, *args):
        try:
            super().append(*[int(arg) for arg in args])
        except ValueError:
            raise TypeError

    def __add__(self, other):
        try:
            return super().__add__([int(value) for value in other])
        except ValueError:
            raise TypeError

    def __iadd__(self, other):
        try:
            return super().__iadd__([int(value) for value in other])
        except ValueError:
            raise TypeError
