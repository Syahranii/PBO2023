from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from fungsi import lsegitiga, lsprisma, lpprisma, vprisma

class FrmPrismaS3:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text="Panjang Alas Segitiga:").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Segitiga:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Prisma:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas Segitiga:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Selimut:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=7, column=0,
            sticky=W, padx=5, pady=5)        

        # pasang textbox
        self.txtalas_segitiga = Entry(mainFrame) 
        self.txtalas_segitiga.grid(row=0, column=1, padx=5, pady=5) 
        self.txttinggi_segitiga = Entry(mainFrame)
        self.txttinggi_segitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txttinggi_prisma = Entry(mainFrame)
        self.txttinggi_prisma.grid(row=2, column=1, padx=5, pady=5)

        self.txtluas_segitiga = Entry(mainFrame)
        self.txtluas_segitiga.grid(row=4, column=1, padx=5, pady=5)
        self.txtluas_selimut = Entry(mainFrame)
        self.txtluas_selimut.grid(row=5, column=1, padx=5, pady=5) 
        self.txtluas_permukaan = Entry(mainFrame) 
        self.txtluas_permukaan.grid(row=6, column=1, padx=5, pady=5)  
        self.txtvolume = Entry(mainFrame) 
        self.txtvolume.grid(row=7, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        at = int(self.txtalas_segitiga.get())
        ts = int(self.txttinggi_segitiga.get())
        tp = int(self.txttinggi_prisma.get())

        luas_segitiga = lsegitiga(at,ts)

        self.txtluas_segitiga.delete(0, END)
        self.txtluas_segitiga.insert(END, str(luas_segitiga))

        luas_selimut = lsprisma(tp,ts)

        self.txtluas_selimut.delete(0, END)
        self.txtluas_selimut.insert(END, str(luas_selimut))

        luas_permukaan = lpprisma(ts,at,tp)

        self.txtluas_permukaan.delete(0, END)
        self.txtluas_permukaan.insert(END, str(luas_permukaan))

        volume= vprisma(at,ts,tp)

        self.txtvolume.delete(0,END) 
        self.txtvolume.insert(END,volume)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrismaS3(root, "Program Luas dan Volume Limas Segi Tiga")
    root.mainloop() 