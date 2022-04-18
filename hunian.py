# declare class
class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, luas_tanah = 0, alamat=""):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_tanah = luas_tanah
        self.alamat = alamat

    # getter methods
    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return str(self.jml_penghuni) + " orang"

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_luas_tanah(self):
        return str(self.luas_tanah) + " m2"

    def get_alamat(self):
        return self.alamat

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."