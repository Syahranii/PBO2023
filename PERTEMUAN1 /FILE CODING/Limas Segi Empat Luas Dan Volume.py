print("Menghitung Luas Dan Volume Limas Segi Empat")

print("s = panjang sisi alas")
print("t = tinggi limas atau tinggi selimut")

# Input panjang sisi alas segiempat, tinggi limas, dan tinggi limas
panjang_sisi_alas = float(input("Masukkan s: "))
tinggi_limas = float(input("Masukkan t: "))

# Menghitung luas alas
luas_alas = panjang_sisi_alas * panjang_sisi_alas
# Menghitung luas sisi tegak
luas_sisi_tegak = 4 * (1/2 * panjang_sisi_alas * tinggi_limas)
# Menghitung luas limas segi empat
luas_limas_segiempat = luas_alas + luas_sisi_tegak
# Menghitung volume limas segi empat 
volume_limas_segiempat = 1/3 * luas_alas * tinggi_limas 

# Menampilkan hasil
print(f"Luas alas limas segi empat adalah: {luas_alas}")
print(f"Luas sisi tegak limas segi empat adalah: {luas_sisi_tegak}")
print(f"Luas limas segi empat adalah: {luas_limas_segiempat}")
print(f"Volume limas segi empat adalah: {volume_limas_segiempat}")