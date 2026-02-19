class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status = "Tersedia"

    def dipinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
        else:
            print("Buku sedang dipinjam.")

    def dikembalikan(self):
        self.status = "Tersedia"


class Mahasiswa:
    def __init__(self, nama, nim,jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.daftar_pinjam = []

    def info_mahasiswa(self):
        print(self.nama, "-", self.nim, "-", self.jurusan)



class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.daftar_mahasiswa = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        for i, buku in enumerate(self.daftar_buku, 1):
            print(i, "-", buku.judul, "-", buku.status)

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        for i, mahasiswa in enumerate(self.daftar_mahasiswa, 1):
            print(i, "-",( mahasiswa.nama), "-", mahasiswa.nim, "-", mahasiswa.jurusan)

    def pinjam_buku(self,mahasiswa, buku):
        if buku.status == "Tersedia":
            buku.dipinjam()
            mahasiswa.daftar_pinjam.append(buku)
            print(mahasiswa.nama, "meminjam buku", buku.judul)
        else:
            print("mohon maaf",mahasiswa.nama,"," "buku", buku.judul, "sedang dipinjam.")

    def kembalikan_buku(self, mahasiswa,buku):
        if buku in mahasiswa.daftar_pinjam:
            buku.dikembalikan()
            mahasiswa.daftar_pinjam.remove(buku)
        print(mahasiswa.nama, "mengembalikan", buku.judul)

    def laporan_peminjaman(self):
        print("\nDaftar Mahasiswa yang Meminjam Buku:")
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.daftar_pinjam:
                print("\nNama:", mahasiswa.nama)
                for buku in mahasiswa.daftar_pinjam:
                    print(" -", buku.judul)




buku1 = Buku("Pemrograman Python", "John Doe")
buku2 = Buku("Basis Data", "Jane Doe")
buku3 = Buku("Jaringan Komputer", "Alice Smith")
buku4 = Buku("Sistem Operasi", "Bob Johnson")
buku5 = Buku("Algoritma dan Struktur Data", "Charlie Brown")
buku6 = Buku("Tuntunan Shalat", "Ustadz Abdul")
buku7 = Buku("Tuntunan Puasa", "Ustadz Abdul")
buku8 = Buku("Tuntunan Haji", "Ustadz Abdul")
buku9 = Buku("Tuntunan Zakat", "Ustadz Abdul")
buku10 = Buku("Tuntunan Sedekah", "Ustadz Abdul")

perpustakaan = Perpustakaan("Universitas Islam Sultan Syarif Kasim Riau")

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2) 
perpustakaan.tambah_buku(buku3)
perpustakaan.tambah_buku(buku4)
perpustakaan.tambah_buku(buku5)
perpustakaan.tambah_buku(buku6)
perpustakaan.tambah_buku(buku7)
perpustakaan.tambah_buku(buku8)
perpustakaan.tambah_buku(buku9)
perpustakaan.tambah_buku(buku10)


fajar = Mahasiswa("Fajar", 12345, "Teknik Informatika")
farhan = Mahasiswa("Farhan", 67890, "Manajemen")
farid = Mahasiswa("Farid", 54321, "Ilmu Komputer")
rido = Mahasiswa("Rido", 98765, "Sistem Informasi")
rina = Mahasiswa("Rina", 13579, "Teknik Industri")
rivaldo = Mahasiswa("Rivaldo", 24680, "Teknik Elektro")

perpustakaan.tambah_mahasiswa(fajar)
perpustakaan.tambah_mahasiswa(farhan)
perpustakaan.tambah_mahasiswa(farid)
perpustakaan.tambah_mahasiswa(rido)
perpustakaan.tambah_mahasiswa(rina)
perpustakaan.tambah_mahasiswa(rivaldo)

print("\nDaftar Mahasiswa:")
perpustakaan.tampilkan_mahasiswa()

print("\nRiwayat peminjaman dan pengembalian buku:\n")
perpustakaan.pinjam_buku(fajar, buku1)
perpustakaan.pinjam_buku(farhan, buku2)
perpustakaan.pinjam_buku(rivaldo, buku3)
perpustakaan.pinjam_buku(rina, buku4)
perpustakaan.pinjam_buku(farid, buku5)
perpustakaan.kembalikan_buku(fajar, buku1)

perpustakaan.laporan_peminjaman()

print("\nDaftar Buku:")
perpustakaan.tampilkan_buku()





