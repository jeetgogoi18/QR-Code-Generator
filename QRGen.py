import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import qrcode
from PIL import Image, ImageTk


def create_qr():
    data = text_entry.get()
    if data:
        img = qrcode.make(data)  # generate QR code
        img = img.resize((250, 250))  # resize QR code
        tkimage = ImageTk.PhotoImage(img)
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Warning", 'Enter Data in Entry First')


def save_qr():
    data = text_entry.get()
    if data:
        img = qrcode.make(data)  # generate QR code
        img = img.resize((280, 250))  # resize QR code
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            img.save(path)
            messagebox.showinfo("Success", "QR Code is Saved")
    else:
        messagebox.showwarning("Warning", 'Enter Data in Entry First')


root = tk.Tk()
root.title("QR Code Generator")
root.geometry("1000x600+200+50")

frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=0, y=0, width=500, height=600)

frame2 = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame2.place(x=500, y=0, width=500, height=600)


qr_canvas = tk.Canvas(frame2)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame1, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.place(x=5, y=5)

btn_1 = ttk.Button(frame1, text="Create", width=10, command=create_qr)
btn_1.place(x=25, y=50)

btn_2 = ttk.Button(frame1, text="Save", width=10, command=save_qr)
btn_2.place(x=100, y=50)

btn_3 = ttk.Button(frame1, text="Exit", width=10, command=root.quit)
btn_3.place(x=175, y=50)

root.mainloop()