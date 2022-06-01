from interface. kehadiran_akademik import KehadiranAkademik
from abc import ABC,abstractmethod


class AdminJurusanOpertion(KehadiranAkademik, ABC):

@abstractmethod
def mencatat_kehadiran(self)-> None:
    super().mencatat_kehadiran()
    
@abstractmethod
def mempublikasikan_jadwal_ujian(self)-> None:
    super().mempublikasikan_jadwal_ujian()
    