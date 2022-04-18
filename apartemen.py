from hunian import Hunian

# declare class
class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luas_tanah, alamat):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, luas_tanah, alamat)
        self.nama_pemilik = nama_pemilik

    # getter methods
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik