from datetime import datetime
from datetime import datetime


class Transaction:
    SELL = 1
    SUPPLY = 2

    def __init__(self, type: int, copies: int):
        self.type = type
        self.copies = copies
        self.date = datetime.now()


class Disc:

    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):

        self.sid = sid
        self.title = title
        self.artist = artist
        self.sale_price = sale_price
        self.purchase_price = purchase_price
        self.quantity = quantity

        self.transactions = []
        self.song_list = []

    def add_song(self, song: str):
        self.song_list.append(song)

    def sell(self, copies: int):
        if copies > self.quantity:
            return False
        else:
        self.quantity -= copies
        t = Transaction(Transaction.SELL, copies)
        self.transactions.append(t)
        return True

    def supply(self, copies: int):
        self.quantity += copies
        t = Transaction(Transaction.SUPPLY, copies)
        self.transactions.append(t)

    def copies_sold(self) -> int:
        total = 0
        for t in self.transactions:
            if t.type == Transaction.SELL:
                total += t.copies
        return total

    def __str__(self):
        songs = ", ".join(self.song_list)
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {songs}"
