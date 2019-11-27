class Account:
    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        while self.balance < 0:
            del self._transactions[-1]
