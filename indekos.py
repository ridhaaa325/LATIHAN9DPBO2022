from hunian import Hunian 

# declare class
class Indekos(Hunian): 
    def __init__(self, nama_pemilik, nama_penghuni, luas_tanah, alamat, harga_sewa):
        super().__init__("Indekos", 1, 1, luas_tanah, alamat)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga_sewa = harga_sewa

    # getter methods
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_summary(self):
        return "Hunian Indekos."

    def get_harga_sewa(self):
        return self.harga_sewa + "/bulan"
