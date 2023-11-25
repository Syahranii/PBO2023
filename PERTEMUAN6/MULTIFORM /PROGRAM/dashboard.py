import tkinter as tk
from tkinter import Menu
from FrmBalok import *
from FrmBola import *
from FrmKerucut import *
from FrmKubus import *
from FrmLimasS4 import *
from FrmLimasS3 import *
from FrmPrismaS3 import *
from FrmTabung import *



# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("500x200")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Balok', command= lambda: new_window("Luas dan Volume Balok", FrmBalok)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Luas dan Volume Bola", FrmBola)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Luas dan Volume Kerucut", FrmKerucut)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Luas dan Volume Kubus", FrmKubus)
)
app_menu.add_command(
    label='App Limas Segi Empat', command= lambda: new_window("Luas dan Volume Limas Segi Empat", FrmLimasS4)
)
app_menu.add_command(
    label='App Limas Segi Tiga', command= lambda: new_window("Luas dan Volume Kubus", FrmLimasS3)
)
app_menu.add_command(
    label='App Prisma Segi Tiga', command= lambda: new_window("Luas dan Volume Prisma Segi Tiga", FrmPrismaS3)
)
app_menu.add_command(
    label='App Limas Tabung', command= lambda: new_window("Luas dan Volume Tabung", FrmTabung)
)

def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)
    
root.mainloop()