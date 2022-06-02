from kehadiran import KehadiranAkademik
from abc import ABC,abstractmethod


class DosenOperation(KehadiranAkademik, ABC):

    @abstractmethod
    def mencatat_kehadiran(self)-> None:
        pass
    @abstractmethod
    def membuat_ujian(self)-> None:
        pass