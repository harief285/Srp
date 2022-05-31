from karakter import Karakter

class Pengendara(Karakter):
    
    def nama (self, karakter: Karakter)->str:
        return ("NAMA",karakter.get_nama)

    def power (self, karakter: Karakter)-> float:
        return ("POWERRRRR",karakter.get_power)