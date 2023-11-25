from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimasS4:
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
        Label(mainFrame, text="Panjang Sisi Alas:").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Limas:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Alas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Sisi Tegak:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtpanjang_sisi_alas = Entry(mainFrame) 
        self.txtpanjang_sisi_alas.grid(row=0, column=1, padx=5, pady=5) 
        self.txttinggi_limas = Entry(mainFrame)
        self.txttinggi_limas.grid(row=1, column=1, padx=5, pady=5)

        self.txtluas_alas = Entry(mainFrame)
        self.txtluas_alas.grid(row=3, column=1, padx=5, pady=5)
        self.txtluas_sisi_tegak = Entry(mainFrame)
        self.txtluas_sisi_tegak.grid(row=4, column=1, padx=5, pady=5) 
        self.txtluas_permukaan = Entry(mainFrame)
        self.txtluas_permukaan.grid(row=5, column=1, padx=5, pady=5)
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=6, column=1, padx=5, pady=5)  
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        ps = int(self.txtpanjang_sisi_alas.get())
        tl = int(self.txttinggi_limas.get())

        luas_alas = ps * ps

        self.txtluas_alas.delete(0, END)
        self.txtluas_alas.insert(END, str(luas_alas))
    
        luas_sisi_tegak = 4 * (1 / 2 * ps * tl)

        self.txtluas_sisi_tegak.delete(0, END)
        self.txtluas_sisi_tegak.insert(END, str(luas_sisi_tegak))

        luas_permukaan = luas_alas + luas_sisi_tegak

        self.txtluas_permukaan.delete(0, END)
        self.txtluas_permukaan.insert(END, str(luas_permukaan))

        volume = 1 / 3 * luas_alas * tl

        self.txtvolume.delete(0, END)
        self.txtvolume.insert(END, str(volume))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasS4(root, "Program Luas dan Volume Limas Segi Empat")
    root.mainloop() 