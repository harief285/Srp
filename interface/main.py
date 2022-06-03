from driver_controller import DriverController
from pembeli_controller import PembeliController
from penjual_controller import *

pembeli=PembeliController()
pj_1=PenjualController()
pj_2=PenjualController()
driver_1=DriverController()
driver_2=DriverController()

pembeli.memesan_pesanan()
pj_1.menolak_pesanan()
pj_2.menyiapkan_pesanan()
driver_1.menolak_pesanan()
driver_2.mengantarkan_pesanan()