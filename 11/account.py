class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    #  add dunder methods below

    def __len__(self):
        return len(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __getitem__(self, key):
        return self._transactions[key]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._transactions):
            transaction = self._transactions[self.index]
            self.index += 1
            return transaction
        else:
            raise StopIteration

    def __add__(self, value):
        self._transactions.append(int(value))

    def __sub__(self, value):
        self._transactions.append(-int(value))

    def __str__(self):
        return f"{self.name.title()} account - balance: {self.balance}"
