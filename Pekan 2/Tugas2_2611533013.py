print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3013 = input("Masukkan Nama Mahasiswa : ")
kelamin_3013 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3013 = int(input("Masukkan Umur : "))
skor_3013 = float(input("Masukkan Skor Tes Awal : "))

alamat_3013 = """
Jln. Griya Madani 4 Blok E/1,
Kecamatan Nanggalo,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_3013: Final = 75.0
token_3013 = 100+3j
lulus_3013 = skor_3013 > kkm_3013

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_3013," | ",type(nama_3013))
print("Jenis Kelamin : ",kelamin_3013," | ",type(kelamin_3013))
print("Alamat Domisili : ",alamat_3013," | ",type(alamat_3013))
print("Umur : ",umur_3013," tahun | ",type(umur_3013))
print("Skor Tes Awal : ",skor_3013," | ",type(skor_3013))
print("ID Token Sinyal: ",token_3013," | ",type(token_3013))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_3013," | ",type(kkm_3013))
print("Apakah Dinyatakan Lulus?: ",lulus_3013," | ",type(lulus_3013))