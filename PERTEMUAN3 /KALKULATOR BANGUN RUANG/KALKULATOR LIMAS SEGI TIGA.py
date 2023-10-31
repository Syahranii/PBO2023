import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas_segitiga_alas():
    ps = float(txtpanjang_sisi_alas.get())
    ts = float(txttinggi_segitiga_alas.get())
    tl = float(txttinggi_limas.get())
    
    luas_segitiga_alas = 0.5 * ps * ts

    txtluas_segitiga_alas.delete(0,END)
    txtluas_segitiga_alas.insert(END,luas_segitiga_alas)

def hitung_luas_permukaan():
    ps = float(txtpanjang_sisi_alas.get())
    ts = float(txttinggi_segitiga_alas.get())
    tl = float(txttinggi_limas.get())
    sa = float(txtluas_segitiga_alas.get ())

    luas_permukaan = sa + 3 * (0.5 * ps * tl)

    txtluas_permukaan.delete(0,END)
    txtluas_permukaan.insert(END,luas_permukaan)

def hitung_volume():
    ps = float(txtpanjang_sisi_alas.get())
    ts = float(txttinggi_segitiga_alas.get())
    tl = float(txttinggi_limas.get())
    sa = float(txtluas_segitiga_alas.get ())
    
    Volume_balok = (1/3) * sa * tl

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume_balok)

def hitung():
    hitung_luas_segitiga_alas()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Limas Segi Tiga")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label Nama
nama = Label (frame, text="SYAHRANI 220511094 TI22E(R5)")
nama.grid(row=0, column=0)

# Label Panjang Sisi Alas
panjang_sisi_alas = Label (frame, text="Panjang Sisi Alas: ")
panjang_sisi_alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Segitiga Alas
tinggi_segitiga_alas = Label (frame, text="Tinggi Segitiga Alas: ")
tinggi_segitiga_alas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Limas
tinggi_limas = Label (frame, text="Tinggi Limas")
tinggi_limas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang Sisi Alas
txtpanjang_sisi_alas = Entry (frame)
txtpanjang_sisi_alas.grid(row=1, column=1)

# Textbox Tinggi Segitiga Alas
txttinggi_segitiga_alas = Entry (frame)
txttinggi_segitiga_alas.grid(row=2, column=1)

# Textbox Tinggi Limas
txttinggi_limas = Entry (frame)
txttinggi_limas.grid(row=3, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Segitiga Alas
luas_segitiga_alas = Label (frame, text="Luas Segitiga Alas: ") 
luas_segitiga_alas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label (frame, text="Luas Permukaan: ")
luas_permukaan.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Segitiga Alas
txtluas_segitiga_alas = Entry (frame) 
txtluas_segitiga_alas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtluas_permukaan = Entry (frame)
txtluas_permukaan.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()