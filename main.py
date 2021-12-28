from tkinter import *

os = Tk()
os.attributes("-fullscreen", True)
menubar = Menu(os)
fileMenu = Menu(menubar)
fileMenu.add_command(label="Exit", command=lambda: os.destroy())
menubar.add_cascade(label="File", menu=fileMenu)
os.config(menu=menubar)
os.mainloop()