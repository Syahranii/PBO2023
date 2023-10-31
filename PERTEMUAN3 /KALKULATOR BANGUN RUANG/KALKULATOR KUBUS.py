import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    r = float(txtrusuk.get())

    Luas_kubus = 6*r*r

    txtLuas.delete(0,END)
    txtLuas.insert(END,Luas_kubus)

def hitung_volume():
    r = float(txtrusuk.get())
    
    Volume_rusuk = r*r*r

    txtvolume.delete(0,END) 
    txtvolume.insert(END,Volume_rusuk)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kubus")

# Windows
frame = Frame (app)
frame.pack(padx=90, pady=90)

# Label Nama
nama = Label (frame, text="SYAHRANI 220511094 TI22E(R5)")
nama.grid(row=0, column=0)

# Label Rusuk
rusuk= Label (frame, text="Rusuk: ")
rusuk.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtrusuk = Entry (frame)
txtrusuk.grid(row=1, column=1)

# Button
hitung_button = Button (frame, text="Hitung", command=hitung) 
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ") 
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry (frame) 
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()