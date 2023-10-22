print("Menghitung Luas Dan Volume Prisma Segi Tiga")

print("a.s = alas segitiga")
print("t.s = tinggi segitiga")
print("t.p = tinggi prisma")

# Input alas segitiga, tinggi segitiga, tinggi prisma
alas_segitiga = float(input("Masukkan a.s: "))
tinggi_segitiga = float(input("Masukkan t.s: "))
tinggi_prisma = float(input("Masukkan t.p: "))

# Menghitung luas segitiga
luas_segitiga = 1/2 * alas_segitiga * tinggi_segitiga
# Menghitung luas selimut
luas_selimut = 3 * tinggi_prisma * tinggi_segitiga
# Menghitung luas permukaan prisma segitiga
luas_permukaan_prisma_segitiga = tinggi_segitiga * alas_segitiga + (3 * tinggi_prisma)
# Menghitung volume prisma segitiga
volume_prisma_segitiga = 1/2 * alas_segitiga * tinggi_segitiga * tinggi_prisma

# Menampilkan hasil
print(f"Luas selimut adalah: {luas_selimut}")
print(f"Luas permukaan prisma segitiga adalah: {luas_permukaan_prisma_segitiga}")
print(f"Volume prisma segitiga adalah: {volume_prisma_segitiga}")