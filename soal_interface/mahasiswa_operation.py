from abc import ABC, abstractmethod
from kehadiran import KehadiranAkademik

class MahasiswaOperation(KehadiranAkademik, ABC):

        @abstractmethod
        def  mencatat_kehadiran(self)-> None:
                pass
        @abstractmethod
        def mengerjakan_ujian(self) -> None:
                pass