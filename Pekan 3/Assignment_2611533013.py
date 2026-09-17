# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_3013 = int(input("input angka-1: "))
angka2_3013 = int(input("input angka-2: "))

print("\nNilai awal angka1_3013 =", angka1_3013)
print("Nilai awal angka2_3013 =", angka2_3013)

# Assignment biasa
# hasil = angka1_3013
print("\nAssignment Biasa (=)")
print("Hasil_3013 =", angka1_3013)

# Assignment penambahan
hasil_3013 = angka1_3013
hasil_3013 += angka2_3013
print("\nAssignment Penambahan (+=)")
print("Hasil =", hasil_3013)

# Assignment pengurangan
hasil_3013 = angka1_3013
hasil_3013 -= angka2_3013
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_3013)

# Assignment perkalian
hasil_3013 = angka1_3013
hasil_3013 *= angka2_3013
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_3013)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3013 != 0:
    hasil_3013 = angka1_3013
    hasil_3013 /= angka2_3013
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_3013)
    # Operator Tambahan
    hasil_3013 = angka1_3013
    hasil_3013 //= angka2_3013
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_3013)
    hasil_3013 = angka1_3013
    hasil_3013 %= angka2_3013
    print("\nAssignment Sisa Bagi (%=)")
    print("Hasil =", hasil_3013)
else:
    print("Angka kedua tidak boleh bernilai 0.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3013 = angka1_3013
hasil_3013 **= angka2_3013
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil_3013)