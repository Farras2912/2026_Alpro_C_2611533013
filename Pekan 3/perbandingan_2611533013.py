# buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit terakhir NIM contoh: nilai_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_3013 = int(input("Input angka-1_3013: "))
angka2_3013 = int(input("Input angka-2_3013: "))

# Lebih besar dari
hasil = angka1_3013 > angka2_3013
print("\nOperator Lebih besar Dari")
print("angka1_3013 > angka2_3013 =", hasil)

# lebih kecil dari
hasil = angka1_3013 < angka2_3013
print("\nOperator Lebih kecil Dari")
print("angka1_3013 < angka2_3013 =", hasil)

# Lebih besar dari atau sama dengan
hasil = angka1_3013 >= angka2_3013
print("\nOperator Lebih besar Dari atau sama dengan")
print("angka1_3013 >= angka2_3013 =", hasil)    

# Lebih kecil dari atau sama dengan
hasil = angka1_3013 <= angka2_3013
print("\nOperator Lebih kecil Dari atau sama dengan")
print("angka1_3013 <= angka2_3013 =", hasil)

# Sama dengan
hasil = angka1_3013 == angka2_3013
print("\nOperator Sama dengan")
print("angka1_3013 == angka2_3013 =", hasil)

# Tidak sama dengan
hasil = angka1_3013 != angka2_3013
print("\nOperator Tidak sama dengan")
print("angka1_3013 != angka2_3013 =", hasil)

# Tambahan: perbandingsn berantai dalam python
hasil = 0 < angka1_3013 < 100
print("\nPerbandingan Berantai")
print("0 < angka1_3013 < 100 =", hasil)

hasil= 0 < angka2_3013 < 100
print("0 < angka2_3013 < 100 =", hasil)