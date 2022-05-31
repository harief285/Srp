from hitung_persegi import Hitung
from persegi import Persegi
class Show:
    def show_luas(self,persegi :Persegi , persegi_hitug : Hitung):
        print(persegi_hitug.hitung_luas(persegi))
    def show_keliling(self,persegi :Persegi , persegi_hitug : Hitung):
        print(persegi_hitug.hitung_keliling(persegi))