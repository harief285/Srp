from abc import ABC, abstractmethod

class Persegi(PerhitungBangunDatar):
    
        
    def hitung_keliling(self,persegi:Persegi)->float:
        return 2*((persegi.get_panjang()+persegi.get_lebar()))
    
    def hitung_luas(self,persegi:Persegi)->float:
        return(persegi.get_panjang()*persegi.get_lebar())