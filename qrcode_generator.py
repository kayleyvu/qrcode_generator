# This is a QR code generator 
# using the segno python library 
# with a tkinter python user interface
# Files will be saved at 10x10 px in PNG 

#Libraries: Turtle, Segno
import tkinter as tk
from tkinter import simpledialog 
import segno 

#User input fields with tkinter 
ROOT=tk.Tk()
ROOT.withdraw()
url=simpledialog.askstring(title='Website link',
                           prompt='Enter a website url for QR code')
size=simpledialog.askinteger(title='File size',
                             prompt='Set a file size (rec: 10)')
color=simpledialog.askstring(title='Color',
                             prompt='Enter a color')
name=simpledialog.askstring('File name',
                            prompt='Name file with desired file format')

#Make QR code 
qrcode=segno.make_qr(url)

#Store encoded content as variable to save QR code as image  
qrcode.save(name,scale=size,border=5,dark=color)

