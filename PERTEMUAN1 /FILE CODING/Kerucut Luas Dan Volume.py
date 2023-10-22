import math
print("Menghitung Luas Dan Volume Kerucut")

print("r = jari jari")
print("t = tinggi")
print("s = garis lurus tali busr dari titik pusat lingkaran")

# input r, t, s
jari_jari = float(input("Masukkan r: "))
tinggi = float(input("Masukkan t: ")) 
s = float(input("Masukkan s: ")) 

# Menghitung luas selimut kerucut
luas_selimut_kerucut = math.pi * jari_jari * s
# Menghitung luas permukaan kerucut
luas_permukaan_kerucut = (math.pi * jari_jari * s) + (math.pi * jari_jari * jari_jari * jari_jari)
# Menghitung volume kerucut
volume_kerucut = 1/3 * math.pi * jari_jari * jari_jari * tinggi

# Menampilkan hasil
print(f"Luas luas selimut kerucut adalah: {luas_selimut_kerucut}")
print(f"Luas permukaan kerucut adalah: {luas_permukaan_kerucut}")
print(f"Volume kerucut adalah: {volume_kerucut}")