import tkinter as tk
import qrcode as qr
from PIL import Image, ImageTk

defaultImage = Image.open('default.png')
defaultImage = defaultImage.resize((400, 400), Image.ANTIALIAS)

def generateQR():
    data = entry.get()
    qrCode = qr.make(data)
    qrCode = qrCode.resize((400, 400), Image.ANTIALIAS)
    qrCodeTkImage = ImageTk.PhotoImage(qrCode)
    label.config(image=qrCodeTkImage)
    label.image = qrCodeTkImage


r = tk.Tk()

r.title('QR Code Generator')

image = ImageTk.PhotoImage(defaultImage)

label = tk.Label(r, image=image)
entry = tk.Entry(r, width=10)
button = tk.Button(r, text='Generate', width=25, command=generateQR)

label.pack()
entry.pack(fill=tk.X, padx=20, pady=10)
button.pack(pady=10)

r.mainloop()