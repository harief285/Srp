from abc import ABC, abstractmethod




class Mahasiswa(Mahasiswa, ABC):



@abstractmethod
def mencatat_kehadiran(self) -> None:
    super().mencatat_kehadiran()

@abstractmethod
def mengerjakan_ujian(self) -> None:
    super().mengerjakan_ujian()
