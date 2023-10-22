print("Menghitung Luas Dan Volume Prisma Segitiga")

# Fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Input panjang alas segitiga dan tinggi alas segitiga
panjang_alas = float(input("Masukkan panjang alas segitiga: "))
tinggi_alas = float(input("Masukkan tinggi alas segitiga: "))
# Input luas alas, keliling alas, dan tinggi prisma
luas_alas = float(input("Masukkan luas alas segitiga: "))
keliling_alas = float(input("Masukkan keliling alas segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Menghitung luas segitiga alas
luas_alas = 0.5 * panjang_alas * tinggi_alas
# Menghitung luas dan volume prisma segitiga
Luas_prisma = (2 * luas_alas) + (keliling_alas * tinggi_prisma)
Volume_prisma = luas_alas * tinggi_prisma

# Menampilkan hasil
print(f"Luas Prisma Segitiga Adalah: {Luas_prisma}")
print(f"Volume Prisma Segitiga Adalah: {Volume_prisma}")