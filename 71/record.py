class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.max_score = 0

    def __call__(self, score):
        if score > self.max_score:
            self.max_score = score
        return self.max_score


if __name__ == "__main__":
    record = RecordScore()
    print(record(10))
    print(record(9))
    print(record(11))
    print(record(7))
