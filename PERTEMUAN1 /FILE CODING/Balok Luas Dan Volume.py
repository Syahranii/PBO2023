print("Menghitung Luas Dan Volume Balok")

print("p = panjang")
print("l = lebar")
print("t = tinggi")

# Input pangjang, lebar, tinggi
panjang = float(input("Masukkan p: "))
lebar = float(input("Masukkan l: "))
tinggi = float(input("Masukkan t: "))

# Menghitung luas balok
luas_balok = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi) 
# Menghitung volume balok
volume_balok = panjang * lebar * tinggi 

# Menampilkan hasil
print(f"Luas balok adalah: {luas_balok}")
print(f"Volume balok adalah: {volume_balok}")