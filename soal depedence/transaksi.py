from kartubank import KartuBank
class Transaksi():
    def __init__(self, kartu : KartuBank):
        self.kartu = kartu
    def do_payment(self):
        return self.kartu