from kartu_bank import kartu_bank

class KartuDebit:
    
    def __init__(self, item:KartuBank,keaktifan:bool=false):
        self.__item=item
        self.__keaktifan

    @abstractmethod
    def do_transaction(self):
        pass
    
    