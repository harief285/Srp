from kartubank import KartuBank

class KartuDebit(KartuBank):
    
    def do_transaction(self,total :int):
        print(f"Transaksi Sejumlah {total} Mengunakan Debit")