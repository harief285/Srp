from penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod
class PenjualOperation(PenolakanOperation, ABC):
    @abstractmethod
    def menolak_pesanan(self):
        pass
    @abstractmethod
    def menyiapkan_pesanan(self):
        pass