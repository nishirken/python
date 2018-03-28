class Value:
    def __set__(self, instance, value):
        self._value = value - instance.commission * value

    def __get__(self, instance, owner):
        return self._value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


account = Account(0.1)
account.amount = 100
print(account.amount)
