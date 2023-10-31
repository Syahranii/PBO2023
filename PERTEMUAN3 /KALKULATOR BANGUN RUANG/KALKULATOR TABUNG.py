import tkinter as tk
import math
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas_selimut():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())

    luas_selimut = 2 * math.pi * r * t

    txtluas_selimut.delete(0,END)
    txtluas_selimut.insert(END,luas_selimut)

def hitung_luas_permukaan():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    
    luas_permukaan = (2 * math.pi * r * t) + 2 * math.pi * r * r

    txtluas_permukaan.delete(0,END)
    txtluas_permukaan.insert(END,luas_permukaan)

def hitung_volume():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    
    volume = math.pi * r * r * t

    txtvolume.delete(0,END) 
    txtvolume.insert(END,volume)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Tabung")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label Nama
nama = Label (frame, text="SYAHRANI 220511094 TI22E(R5)")
nama.grid(row=0, column=0)

# Label Jari_jari
jari_jari= Label (frame, text="Jari - jari: ")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label (frame, text="Tinggi: ")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari_jari
txtjari_jari = Entry (frame)
txtjari_jari.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry (frame)
txttinggi.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label (frame, text="Luas Selimut: ") 
luas_selimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label (frame, text="Luas Permukaan: ") 
luas_permukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtluas_selimut = Entry (frame) 
txtluas_selimut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtluas_permukaan = Entry (frame) 
txtluas_permukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()