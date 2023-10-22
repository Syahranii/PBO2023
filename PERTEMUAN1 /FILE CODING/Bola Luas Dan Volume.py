import math
print("Menghitung Luas Dan Volume Kerucut")

print("r = jari jari")

# input jari jari
jari_jari = float(input("Masukkan r: "))

# Menghitung luas bola
luas_bola = 4 * math.pi * jari_jari * jari_jari
# Menghitung volume bola
volume_bola = 4/3 * math.pi * jari_jari * jari_jari * jari_jari

# Menampilkan hasil
print(f"Luas bola adalah: {luas_bola}")
print(f"Volume bola adalah: {volume_bola}")