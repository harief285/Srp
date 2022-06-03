from hitung_balok import Hitung
from balok import Balok
class ShowBalok:
    def show_luas(self,balok : Balok,hitung : Hitung):
        print(hitung.hitung_luas(balok))
    def show_keliling(self,balok : Balok,hitung : Hitung):
        print(hitung.hitung_keliling(balok))
    def show_volume(self,balok : Balok,hitung : Hitung):
        print(hitung.hitung_volume(balok))