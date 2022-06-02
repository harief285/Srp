from kehadiran import KehadiranAkademik
from abc import ABC,abstractmethod

class AdminJurusanOpertion(KehadiranAkademik, ABC):

    @abstractmethod
    def mencatat_kehadiran(self)-> None:
        pass
    @abstractmethod
    def mempublikasikan_jadwal_ujian(self)-> None:
        pass