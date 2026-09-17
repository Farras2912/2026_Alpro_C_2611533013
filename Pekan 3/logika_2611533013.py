# Memasukkan nilai boolean 
# Input tidak peka terhadap huruf besar dan kecil
a1_3013 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3013 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("/nA1_3013 =", a1_3013)
print("A2_3013 =", a2_3013)   

# Konjungsi bernilai True jika keduanya True
hasil_3013 = a1_3013 and a2_3013
print("/nOperator Konjungsi (AND)")
print("A1_3013 and A2_3013 =", hasil_3013)

# Disjungsi bernilai True jika salah satunya True
hasil_3013 = a1_3013 or a2_3013
print("/nDisjungsi (OR)")
print("A1_3013 or A2_3013 =", hasil_3013)

# Negasi A1_3013: membalik nilai A1_3013
hasil_3013 = not a1_3013
print("/nNegasi A1_3013 (NOT)")
print("not A1_3013 =", hasil_3013)

# Negasi A2_3013: membalik nilai A2_3013
hasil_3013 = not a2_3013
print("/nNegasi A2_3013 (NOT)")
print("not A2_3013 =", hasil_3013)

# XOR: bernilai True jika kedua nilai berbeda
hasil_3013 = a1_3013 != a2_3013
print("\nDisjungsi Eksklusif (XOR)")
print("A1_3013 XOR A2_3013 =", hasil_3013)