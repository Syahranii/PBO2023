import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import lalas, lsisi_tegak, lplimas_segiempat, vlimas_segiempat

def hitung_luas_alas():
    ps = float(txtpanjang_sisi_alas.get())
    tl = float(txttinggi_limas.get())

    luas_alas = lalas(ps)
    
    txtluas_alas.delete(0,END)
    txtluas_alas.insert(END,luas_alas)

def hitung_luas_sisi_tegak():
    ps = float(txtpanjang_sisi_alas.get())
    tl = float(txttinggi_limas.get())

    luas_sisi_tegak = lsisi_tegak(ps,tl)

    txtluas_sisi_tegak.delete(0,END)
    txtluas_sisi_tegak.insert(END,luas_sisi_tegak)

def hitung_luas_permukaan():
    ps = float(txtpanjang_sisi_alas.get())
    tl = float(txttinggi_limas.get())   
    la = float(txtluas_alas.get())
    st = float(txtluas_sisi_tegak.get())
    
    luas_permukaan = lplimas_segiempat(la,st)

    txtluas_permukaan.delete(0,END)
    txtluas_permukaan.insert(END,luas_permukaan)

def hitung_volume():
    ps = float(txtpanjang_sisi_alas.get())
    tl = float(txttinggi_limas.get())
    la = float(txtluas_alas.get())
    st = float(txtluas_sisi_tegak.get())
    
    volume = vlimas_segiempat(la,tl)

    txtvolume.delete(0,END) 
    txtvolume.insert(END,volume)

def hitung():
    hitung_luas_alas()
    hitung_luas_sisi_tegak()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Limas Segi Empat")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label Nama
nama = Label (frame, text="SYAHRANI 220511094 TI22E(R5)")
nama.grid(row=0, column=0)

# Label Panjang Sisi Alas 
panjang_sisi_alas= Label (frame, text="Panjang Sisi Alas: ")
panjang_sisi_alas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Limas
tinggi_limas = Label (frame, text="Tinggi Limas: ")
tinggi_limas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang Sisi Alas 
txtpanjang_sisi_alas = Entry (frame)
txtpanjang_sisi_alas.grid(row=1, column=1)

# Textbox Tinggi Limas
txttinggi_limas = Entry (frame)
txttinggi_limas.grid(row=2, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Alas
luas_alas = Label(frame, text="Luas Alas: ") 
luas_alas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Sisi Tegak
luas_sisi_tegak = Label(frame, text="Luas Sisi Tegak: ") 
luas_sisi_tegak.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan: ")
luas_permukaan.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Alas
txtluas_alas = Entry (frame)
txtluas_alas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Sisi Tegak
txtluas_sisi_tegak = Entry (frame)
txtluas_sisi_tegak.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtluas_permukaan = Entry (frame)
txtluas_permukaan.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()