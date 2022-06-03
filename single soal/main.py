from balok import Balok
from hitung_balok import Hitung
from tampil_balok import ShowBalok

balok= Balok(8,7,6)
penghitung_balok= Hitung()
penampil_balok= ShowBalok()

penampil_balok.show_luas(balok, penghitung_balok)
penampil_balok.show_keliling(balok, penghitung_balok) 
penampil_balok.show_volume(balok, penghitung_balok)