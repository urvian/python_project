# qr_generator.py
import pyqrcode

def create_qrcode(data, file_path):
    qr_code_data = pyqrcode.create(data)
    qr_code_data.png(file_path, scale=6)



# import pyqrcode
# from PIL import ImageTk, Image
# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog

# root = Tk()
# root.title('My Friend QR')

# l2 = Label(root,text='This Is Your Own QR Code Generator',font=('Helvetica', 18))
# l2.pack(pady=20)

# def create_qrcode():
#     input_path = filedialog.asksaveasfilename(
#         title="Save Image", filetypes=(("PNG File", ".png"), ("All Files", "*.*"))
#     )

#     if input_path:
#         if not input_path.endswith(".png"):
            
#             input_path = f"{input_path}.png"

#         qr_code_data = pyqrcode.create(e1.get())
#         qr_code_data.png(input_path, scale=6)
#     else:
#         input_path = f'{input_path}.png'
#         get_code = pyqrcode.create(e1.get())
#         get_code.png(input_path, scale=6)

#     # Load the image using ImageTk.PhotoImage from the temporary file
#     with open(input_path, "rb") as f:
#         qr_img = ImageTk.PhotoImage(file=f)
    
#     l1.config(image=qr_img)
#     l1.image = qr_img  # Keep a reference to the image to prevent it from being garbage collected

# def clear():
#     e1.delete(0, END)
#     l1.config(image='')

# e1 = Entry(root, font=('Helvetica', 18))
# e1.pack(pady=20)

# b1 = Button(root, text='Create', bg='pink', font=('Helvetica', 18), command=create_qrcode)
# b1.pack(pady=20)

# b2 = Button(root, text='Clear', bg='pink', font=('Helvetica', 18), command=clear)
# b2.pack(pady=20)

# l1 = Label(root)
# l1.pack(pady=20)

# root.mainloop()
