from persegi import Persegi
class Hitung:
    def hitung_luas(self,persegi : Persegi)->float:
        return persegi.get_sisi()*persegi.get_sisi()
    def hitung_keliling(self,persegi : Persegi)->float:
        return persegi.get_sisi()*4