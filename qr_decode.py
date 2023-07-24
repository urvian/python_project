# qr_decoder.py
from PIL import Image as PILImage
from pyzbar.pyzbar import decode

def decode_qr_code(file_path):
    decode_QR = decode(PILImage.open(file_path))
    if decode_QR:
        return decode_QR[0].data.decode('ascii')
    else:
        return None



# # import pyqrcode
# from PIL import ImageTk, Image as PILImage  # Renamed Image to PILImage
# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog
# from pyzbar.pyzbar import decode
# # import io

# root = Tk()
# root.title('My Friend QR')

# l2 = Label(root, text='This Is Your Own QR Code Generator', font=('Helvetica', 18))
# l2.pack(pady=20)

# def decode_it():
#     input_path = filedialog.askopenfilename(
#         title="Open Image", filetypes=(("PNG File", ".png"), ("All Files", "*.*"))
#     )

#     if input_path:
#         with open(input_path, "rb") as f:
#             qr_img = PILImage.open(f)  # Using PILImage.open() instead of Image.open()
#             qr_img = ImageTk.PhotoImage(qr_img)

#         l1.config(image=qr_img)
#         l1.image = qr_img

#         decode_QR = decode(PILImage.open(input_path))  # Using PILImage.open() here too
#         result_label.config(text=f"QR Decoded: {decode_QR[0].data.decode('ascii')}")

# l1 = Label(root)
# l1.pack(pady=20)

# result_label = Label(root, text='')
# result_label.pack(pady=20)

# result_button = Button(root, text='Decode QR CODE', bg='pink', font=('Helvetica', 18), command=decode_it)
# result_button.pack(pady=20)

# root.mainloop()
