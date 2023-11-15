import tkinter as tk
import math
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import lskerucut, lpkerucut, vkerucut

def hitung_selimut():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtapotema.get())

    luas_selimut = lskerucut(r,s)

    txtluas_selimut.delete(0,END)
    txtluas_selimut.insert(END,luas_selimut)

def hitung_luas_permukaan():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtapotema.get())

    luas_permukaan = lpkerucut(s,r)

    txtluas_permukaan.delete(0,END)
    txtluas_permukaan.insert(END,luas_permukaan)

def hitung_volume():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtapotema.get())
    
    volume_kerucut = vkerucut(r,t)

    txtvolume.delete(0,END) 
    txtvolume.insert(END,volume_kerucut)

def hitung():
    hitung_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kerucut")

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

# Label Apotema
apotema = Label (frame, text="Apotema: ")
apotema.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari_jari
txtjari_jari = Entry (frame)
txtjari_jari.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry (frame)
txttinggi.grid(row=2, column=1)

# Textbox Apotema
txtapotema = Entry (frame)
txtapotema.grid(row=3, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut: ") 
luas_selimut.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas_permukaan = Label(frame, text="Luas Permukaan: ") 
luas_permukaan.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtluas_selimut = Entry (frame) 
txtluas_selimut.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtluas_permukaan = Entry (frame) 
txtluas_permukaan.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()