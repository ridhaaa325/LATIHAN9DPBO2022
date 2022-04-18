from hunian import Hunian

# declare class
class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, alamat):
        super().__init__("Rumah", jml_penghuni, jml_kamar, luas_tanah, alamat)
        self.nama_pemilik = nama_pemilik

    # getter methods
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik