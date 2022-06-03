from penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod
class DriverOperation(PenolakanOperation, ABC):
    @abstractmethod
    def menolak_pesanan(self):
        pass
    @abstractmethod
    def mengantarkan_pesanan(self):
        pass