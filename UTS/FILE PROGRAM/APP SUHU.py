import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def konversi_suhu():
    try:
        suhu_awal = float(entry_suhu.get())
        suhu_awal_unit = combo_suhu_awal.get()
        suhu_tujuan_unit = combo_suhu_tujuan.get()

        if suhu_awal_unit == "Celcius":
            suhu_tujuan = konversi_dari_celcius(suhu_awal, suhu_tujuan_unit)
        elif suhu_awal_unit == "Fahrenheit":
            suhu_tujuan = konversi_dari_fahrenheit(suhu_awal, suhu_tujuan_unit)
        elif suhu_awal_unit == "Reamur":
            suhu_tujuan = konversi_dari_reamur(suhu_awal, suhu_tujuan_unit)
        elif suhu_awal_unit == "Kelvin":
            suhu_tujuan = konversi_dari_kelvin(suhu_awal, suhu_tujuan_unit)

        label_hasil.config(text=f"Hasil Konversi: {round(suhu_tujuan, 2)} {suhu_tujuan_unit}")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid untuk suhu!")

def konversi_dari_celcius(suhu_awal, suhu_tujuan_unit):
    if suhu_tujuan_unit == "Celcius":
        return suhu_awal
    elif suhu_tujuan_unit == "Fahrenheit":
        return (suhu_awal * 9/5) + 32
    elif suhu_tujuan_unit == "Reamur":
        return suhu_awal * 4/5
    elif suhu_tujuan_unit == "Kelvin":
        return suhu_awal + 273.15

def konversi_dari_fahrenheit(suhu_awal, suhu_tujuan_unit):
    if suhu_tujuan_unit == "Celcius":
        return (suhu_awal - 32) * 5/9
    elif suhu_tujuan_unit == "Fahrenheit":
        return suhu_awal
    elif suhu_tujuan_unit == "Reamur":
        return (suhu_awal - 32) * 4/9
    elif suhu_tujuan_unit == "Kelvin":
        return (suhu_awal + 459.67) * 5/9

def konversi_dari_reamur(suhu_awal, suhu_tujuan_unit):
    if suhu_tujuan_unit == "Celcius":
        return suhu_awal * 5/4
    elif suhu_tujuan_unit == "Fahrenheit":
        return (suhu_awal * 9/4) + 32
    elif suhu_tujuan_unit == "Reamur":
        return suhu_awal
    elif suhu_tujuan_unit == "Kelvin":
        return (suhu_awal * 5/4) + 273.15

def konversi_dari_kelvin(suhu_awal, suhu_tujuan_unit):
    if suhu_tujuan_unit == "Celcius":
        return suhu_awal - 273.15
    elif suhu_tujuan_unit == "Fahrenheit":
        return (suhu_awal * 9/5) - 459.67
    elif suhu_tujuan_unit == "Reamur":
        return (suhu_awal - 273.15) * 4/5
    elif suhu_tujuan_unit == "Kelvin":
        return suhu_awal

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Konversi Suhu")

# Menambahkan background gambar
background_image = Image.open("galaxy.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Warna biru elektrik
warna_biru_elektrik = "#007FFF"

# Membuat frame dengan ukuran 70x70
frame = tk.Frame(root, width=70, height=70)
frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Menambahkan teks "SYAHRANI NIM 220511094" di paling atas dengan font degradasi bold dan warna putih
label_nama = tk.Label(frame, text="SYAHRANI NIM 220511094", font=("Montserrat", 16, "bold"), foreground="white", background=warna_biru_elektrik)
label_nama.pack(side="top")

# Membuat label dan entry untuk suhu awal
label_suhu_awal = tk.Label(root, text="Suhu Awal:", foreground=warna_biru_elektrik)
label_suhu_awal.grid(row=1, column=0, padx=10, pady=10)

entry_suhu = tk.Entry(root)
entry_suhu.grid(row=1, column=1, padx=10, pady=10)

# Membuat combobox untuk unit suhu awal
label_unit_awal = tk.Label(root, text="Unit Suhu Awal:", foreground=warna_biru_elektrik)
label_unit_awal.grid(row=2, column=0, padx=10, pady=10)

unit_suhu_awal = ["Celcius", "Fahrenheit", "Reamur", "Kelvin"]
combo_suhu_awal = ttk.Combobox(root, values=unit_suhu_awal, style="TCombobox", foreground=warna_biru_elektrik, background="white")
combo_suhu_awal.grid(row=2, column=1, padx=10, pady=10)
combo_suhu_awal.set("Celcius")

# Membuat combobox untuk unit suhu tujuan
label_unit_tujuan = tk.Label(root, text="Unit Suhu Tujuan:", foreground=warna_biru_elektrik)
label_unit_tujuan.grid(row=3, column=0, padx=10, pady=10)

unit_suhu_tujuan = ["Celcius", "Fahrenheit", "Reamur", "Kelvin"]
combo_suhu_tujuan = ttk.Combobox(root, values=unit_suhu_tujuan, style="TCombobox", foreground=warna_biru_elektrik, background="white")
combo_suhu_tujuan.grid(row=3, column=1, padx=10, pady=10)
combo_suhu_tujuan.set("Celcius")

# Tombol konversi
tombol_konversi = tk.Button(root, text="Konversi", command=konversi_suhu, foreground="white", background=warna_biru_elektrik)
tombol_konversi.grid(row=4, column=0, columnspan=4, pady=10)

# Label hasil konversi
label_hasil = tk.Label(root, text="Hasil Konversi:", foreground=warna_biru_elektrik)
label_hasil.grid(row=5, column=0, columnspan=4, pady=10)

# Menjalankan aplikasi
root.mainloop()
