
class InsufficientBalance(Exception):
    pass


class Wallet(object):

    def __init__(self, intialBalance=0):
        self._balance = intialBalance

    def getBalance(self):
        return self._balance

    def addCash(self, amount):
        self._balance = self._balance + amount

    def spend(self, amount):

        if self._balance < amount:
            raise InsufficientBalance("Insufficient wallet balance")
        self._balance = self._balance - amount

