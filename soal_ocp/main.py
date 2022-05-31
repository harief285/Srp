from pengendara import *
from pemukul import *
from penembak import *


nabrak = KarakterPengendara("Lari kencang",20)
print(nabrak.menyerang())

mukul=KarakterPemukul("Gebug pake kayu",50)
print(mukul.menyerang())

tembak=KarakterPenembak("Pistor dor",70)
print(tembak.menyerang())