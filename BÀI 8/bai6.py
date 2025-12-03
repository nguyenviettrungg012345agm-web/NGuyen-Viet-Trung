from tkinter import *

# ---------------------------
# Bước 3: Thêm các hàm xử lý menu
# ---------------------------

def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def Exit():
    print("Exit!")
    root.quit()

def InsText():
    print("Insert Text!")

def InsPic():
    print("Insert Picture!")

def About():
    print("This is a simple example of a menu")

# ---------------------------
# Bước 1: Tạo window chính
# ---------------------------
root = Tk()
root.title("Menu Example")
root.geometry("400x300")

# ---------------------------
# Tạo menu
# ---------------------------
menu = Menu(root)
root.config(menu=menu)

# ----- Menu File -----
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# ----- Menu Insert -----
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# ----- Menu Help -----
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="About...", command=About)

# ---------------------------
# Chạy giao diện
# ---------------------------
root.mainloop()
