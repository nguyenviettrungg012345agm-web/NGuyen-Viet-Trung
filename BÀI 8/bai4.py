from tkinter import *

# a) Tạo cửa sổ window form
window = Tk()
window.title("Demo Tkinter")
window.geometry("350x200")

# Nhãn hiển thị
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# c) Hàm xử lý khi nhấn nút
def clicked():
    lbl.configure(text="Button was clicked !!!")

# b) Thêm một button
btn = Button(window, 
             text="Click Me", 
             command=clicked,
             bg="lightblue",   # d) Thay đổi màu nền
             fg="red")         # d) Thay đổi màu chữ

btn.grid(column=1, row=0)

# Vòng lặp giao diện
window.mainloop()
