import math
print("Menghitung Luas Dan Volume Tabung")

print("r = jari jari")
print("t = tinggi")

# input jari jari, tinggi
jari_jari = float(input("Masukkan r: "))
tinggi = float(input("Masukkan t: ")) 

# Menghitung luas selimut tabung
luas_selimut_tabung = 2 * math.pi * jari_jari * tinggi
# Menghitung luas permukaan tabung
luas_permukaan_tabung = (2 * math.pi * jari_jari * tinggi) + 2 * math.pi * jari_jari * jari_jari
# Menghitung volume tabung
volume_tabung = math.pi * jari_jari * jari_jari * tinggi

# Menampilkan hasil
print(f"Luas luas selimut tabung adalah: {luas_selimut_tabung}")
print(f"Luas permukaan tabung adalah: {luas_permukaan_tabung}")
print(f"Volume tabung adalah: {volume_tabung}")