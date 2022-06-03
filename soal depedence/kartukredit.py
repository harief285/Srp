from kartubank import KartuBank

class KartuKredit(KartuBank):
    def do_transaction(self,total : int):
        print(F"Transaksi Sebesar {total} dengan mengunakan Kredit")