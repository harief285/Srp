from adminjurusan import AdminJurusan
from dosen import Dosen
from mahasiswa import Mahasiswa

admin=AdminJurusan()
print(admin.mencatat_kehadiran())
print(admin.mempublikasikan_jadwal_ujian())

dosen=Dosen()
print(dosen.mencatat_kehadiran())
print(dosen.membuat_ujian())

mhs=Mahasiswa()
print(mhs.mencatat_kehadiran())
print(mhs.mengerjakan_ujian())