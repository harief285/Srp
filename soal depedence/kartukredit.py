from kartubank import KartuBank

class KartuKredit(KartuBank):
    def do_transaction(self,total : int):
        self.total=total
        print("kartuKredit",self.total)