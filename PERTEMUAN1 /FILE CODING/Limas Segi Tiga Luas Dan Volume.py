print("Menghitung Luas Dan Volume Limas Segi Tiga")

print("p = panjang sisi alas")
print("t.a = tingga segitiga alas")
print("t.l = tinggi limas")

# Input panjang sisi alas segitiga, tinggi segitiga alas, dan tinggi limas
panjang_sisi_alas = float(input("Masukkan p: "))
tinggi_alas = float(input("Masukkan t.a: "))
tinggi_limas = float(input("Masukkan t.l: "))

# Menghitung luas segitiga alas
luas_segitiga_alas = 0.5 * panjang_sisi_alas * tinggi_alas
# Menghitung luas permukaan limas segitiga
luas_permukaan_limas = luas_segitiga_alas + 3 * (0.5 * panjang_sisi_alas * tinggi_limas)
# Menghitung volume limas segitiga
volume_limas_segitiga = (1/3) * luas_segitiga_alas * tinggi_limas

# Menampilkan hasil
print(f"Luas segitiga alas adalah: {luas_segitiga_alas}")
print(f"Luas permukaan limas segitiga adalah: {luas_permukaan_limas}")
print(f"Volume limas segitiga adalah: {volume_limas_segitiga}")