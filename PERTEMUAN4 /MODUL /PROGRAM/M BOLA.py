import tkinter as tk
import math
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi import lbola, vbola

def hitung_luas():
    r = float(txtjari_jari.get())

    Luas_bola = lbola(r)

    txtLuas.delete(0,END)
    txtLuas.insert(END,Luas_bola)

def hitung_volume():
    r = float(txtjari_jari.get())
    
    Volume_bola = vbola(r)

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume_bola)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Bola")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label Nama
nama = Label (frame, text="SYAHRANI 220511094 TI22E(R5)")
nama.grid(row=0, column=0)

# Label Jari_jari
jari_jari= Label (frame, text="Jari - jari: ")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari_jari
txtjari_jari = Entry (frame)
txtjari_jari.grid(row=1, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ") 
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame) 
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()