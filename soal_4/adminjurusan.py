from interface. admin_jurusan_operation import AdminJurusanOperation
from abc import ABC,abstractmethod


class AdminJurusan(AdminJurusan, ABC):

@abstractmethod
def mencatat_kehadiran(self)-> None:
    super().mencatat_kehadiran()
    
@abstractmethod
def mempublikasikan_jadwal_ujian(self)-> None:
    super().mempublikasikan_jadwal_ujian()
    