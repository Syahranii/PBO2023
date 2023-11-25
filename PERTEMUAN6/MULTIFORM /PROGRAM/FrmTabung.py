import math
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from fungsi import lstabung, lptabung, vtabung

class FrmTabung:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x250")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text="Jari - Jari:").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Selimut:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtjari_jari = Entry(mainFrame) 
        self.txtjari_jari.grid(row=0, column=1, padx=5, pady=5) 
        self.txttinggi = Entry(mainFrame)
        self.txttinggi.grid(row=1, column=1, padx=5, pady=5)

        self.txtluas_selimut = Entry(mainFrame)
        self.txtluas_selimut.grid(row=3, column=1, padx=5, pady=5)
        self.txtluas_permukaan = Entry(mainFrame)
        self.txtluas_permukaan.grid(row=4, column=1, padx=5, pady=5)
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=5, column=1, padx=5, pady=5)  
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        r = int(self.txtjari_jari.get())
        t = int(self.txttinggi.get())

        luas_selimut = lstabung(r,t)

        self.txtluas_selimut.delete(0, END)
        self.txtluas_selimut.insert(END, str(luas_selimut))
    
        luas_permukaan = lptabung(r,t)

        self.txtluas_permukaan.delete(0, END)
        self.txtluas_permukaan.insert(END, str(luas_permukaan))

        volume = vtabung(r,t)

        self.txtvolume.delete(0, END)
        self.txtvolume.insert(END, str(volume))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTabung(root, "Program Luas dan Volume Tabung")
    root.mainloop() 