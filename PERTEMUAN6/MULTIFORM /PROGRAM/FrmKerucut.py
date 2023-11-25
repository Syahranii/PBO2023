from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from fungsi import lskerucut, lpkerucut, vkerucut

class FrmKerucut:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("400x250")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text="Jari-jari:").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Apotema:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Selimut:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume Kerucut:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtJarijari = Entry(mainFrame) 
        self.txtJarijari.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggi = Entry(mainFrame) 
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5) 
        self.txtApotema = Entry(mainFrame) 
        self.txtApotema.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas_selimut = Entry(mainFrame) 
        self.txtLuas_selimut.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuas_permukaan = Entry(mainFrame) 
        self.txtLuas_permukaan.grid(row=5, column=1, padx=5, pady=5)
        self.txtVolume_kerucut = Entry(mainFrame) 
        self.txtVolume_kerucut.grid(row=6, column=1, padx=5, pady=5)  
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        r = int(self.txtJarijari.get())
        t = int(self.txtTinggi.get())
        s = int(self.txtApotema.get())

        luas_selimut = lskerucut(r,s)
        luas_permukaan = lpkerucut(s,r)
        volume_kerucut = vkerucut(r,t)

        self.txtLuas_selimut.delete(0,END)
        self.txtLuas_selimut.insert(END,str(luas_selimut))
        self.txtLuas_permukaan.delete(0,END)
        self.txtLuas_permukaan.insert(END,str(luas_permukaan))
        self.txtVolume_kerucut.delete(0,END)
        self.txtVolume_kerucut.insert(END,str(volume_kerucut))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmKerucut(root, "Program Luas dan Volume Kerucut")
    root.mainloop() 