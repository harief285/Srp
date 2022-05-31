from persegi import Persegi 
from hitung_persegi import * 
from persegi_view import Show 

persegi= Persegi(2)
penghitung_persegi= Hitung()
penampil_persegi= Show()

penampil_persegi.show_luas(persegi, penghitung_persegi)
penampil_persegi.show_keliling(persegi, penghitung_persegi)