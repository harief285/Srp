from kartubank import KartuBank

class KartuDebit(KartuBank):
    def do_transaction(self,total :int):
        self.total=total
        print("kartuDebit",self.total)