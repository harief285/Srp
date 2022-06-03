from kartubank import KartuBank

class Transaksi:
    def __init__(self, transaksi : KartuBank):
        self.__transaksi = transaksi
        
    def do_payment(self,total: int):
        self.__transaksi.do_transaction(total)