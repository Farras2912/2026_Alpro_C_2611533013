# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit terakhir NIM contoh: nilai_1234
# Deklarasi variable dengan tipe data Boolean
is_lulus = True
is_cumlaude = True

# Menggunakan Boolean
nilai_3013 = 85
batas_lulus_3013 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai_3013 >= batas_lulus_3013 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3013)
print("Apakah Lulus:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")
