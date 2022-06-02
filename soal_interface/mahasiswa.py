from abc import ABC, abstractmethod
from mahasiswa_operation import MahasiswaOperation



class Mahasiswa(MahasiswaOperation, ABC):

    def mencatat_kehadiran(self) -> None:
        print("Mencatat kehadiran perhari")

    def mengerjakan_ujian(self) -> None:
        print("Mengerjakan Ujian")