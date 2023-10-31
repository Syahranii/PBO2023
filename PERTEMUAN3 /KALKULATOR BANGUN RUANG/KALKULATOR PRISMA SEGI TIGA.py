import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas_segitiga():
    at = float(txtalas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tp = float(txttinggi_prisma.get())
    
    luas_segitiga = 1/2 * at * ts

    txtluas_segitiga.delete(0,END)
    txtluas_segitiga.insert(END,luas_segitiga)

def hitung_luas_selimut():
    at = float(txtalas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tp = float(txttinggi_prisma.get())

    luas_selimut = 3 * tp* ts

    txtluas_selimut.delete(0,END)
    txtluas_selimut.insert(END,luas_selimut)

def hitung_luas_permukaan():
    at = float(txtalas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tp = float(txttinggi_prisma.get())

    luas_permukaan = ts* at + (3 * tp)

    txtluas_permukaan.delete(0,END)
    txtluas_permukaan.insert(END,luas_permukaan)

def hitung_volume():
    at = float(txtalas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tp = float(txttinggi_prisma.get())

    Volume_balok = 1/2 * at * ts * tp

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume_balok)

def hitung():
    hitung_luas_segitiga()
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Prisma Segi Tiga")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label Nama
nama = Label (frame, text="SYAHRANI 220511094 TI22E(R5)")
nama.grid(row=0, column=0)

# Label Panjang Alas Segitiga
alas_segitiga = Label (frame, text="Alas Segitiga: ")
alas_segitiga.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga
tinggi_segitiga = Label (frame, text="Tinggi Segitiga: ")
tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Prisma
tinggi_prisma = Label (frame, text="Tinggi Prisma")
tinggi_prisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang Alas Segitiga
txtalas_segitiga = Entry (frame)
txtalas_segitiga.grid(row=1, column=1)

# Textbox Tinggi Segitiga
txttinggi_segitiga = Entry (frame)
txttinggi_segitiga.grid(row=2, column=1)

# Textbox Tinggi Prisma
txttinggi_prisma = Entry (frame)
txttinggi_prisma.grid(row=3, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Segitiga 
luas_segitiga = Label (frame, text="Luas Segitiga: ") 
luas_segitiga.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label (frame, text="Luas Selimut: ")
luas_selimut.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan 
luas_Permukaan = Label (frame, text="Luas Permukaan: ")
luas_Permukaan.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Segitiga 
txtluas_segitiga = Entry (frame)
txtluas_segitiga.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtluas_selimut = Entry (frame)
txtluas_selimut.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Permukaan 
txtluas_permukaan = Entry (frame)
txtluas_permukaan.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=8, column=1, sticky=W, padx=5, pady=5)

app.mainloop()