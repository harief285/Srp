from karakter import Karakter

class Penembak(Karakter):
    
    def nama (self, karakter: Karakter)->str:
        return ("NAMA",karakter.get_nama)

    def power (self, karakter: Karakter)-> float:
        return ("POWERRRRR",karakter.get_power)