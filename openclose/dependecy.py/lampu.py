from barang_elektronik import BarangElektronik 


class Lampu(BarangElektronik):
    def beroperasi(self):
        print("Lampu menyala")
        
    def berhenti(self)-> int:
        print ("Lampu berhenti menyala")
    
    