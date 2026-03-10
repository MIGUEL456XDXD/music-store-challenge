from datetime import datetime
from datetime import datetime

class Transaction:
    SELL = 1
    SUPPLY = 2

    def __init__(self, type, copies):
        self.type = type
        self.copies = copies
        self.date = datetime.now()