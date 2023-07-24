# main.py
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from qr_code import create_qrcode
from qr_decode import decode_qr_code
from PIL import ImageTk, Image as PILImage
# import io
from tkinter import ttk

def on_create():
    input_path = filedialog.asksaveasfilename(
        title="Save Image", filetypes=(("PNG File", ".png"), ("All Files", "*.*"))
    )

    if input_path:
        if not input_path.endswith(".png"):
            input_path = f"{input_path}.png"

        create_qrcode(e1.get(), input_path)

        with open(input_path, "rb") as f:
            qr_img = PILImage.open(f)
            qr_img = ImageTk.PhotoImage(qr_img)

        l1.config(image=qr_img)
        l1.image = qr_img

def on_clear():
    e1.delete(0, END)
    l1.config(image='')

def on_decode():
    input_path = filedialog.askopenfilename(
        title="Open Image", filetypes=(("PNG File", ".png"), ("All Files", "*.*"))
    )

    if input_path:
        with open(input_path, "rb") as f:
            qr_img = PILImage.open(f)
            qr_img = ImageTk.PhotoImage(qr_img)

        l3.config(image=qr_img)
        l3.image = qr_img

        decoded_data = decode_qr_code(input_path)
        if decoded_data:
            result_label.config(text=f"QR Decoded: {decoded_data}")
        else:
            result_label.config(text="No QR code found in the image.")

root = tk.Tk()
root.title('QR Code Generator and Decoder')

paned_window = PanedWindow(root, orient=HORIZONTAL, bd=3, relief="ridge")
paned_window.pack(fill=BOTH, expand=True)

# Left pane: QR Code Generator
generator_frame = Frame(paned_window, padx=10, pady=10, highlightbackground='pink', highlightthickness=7)
paned_window.add(generator_frame, stretch="always")  

l2 = Label(generator_frame, text='QR Code Generator', font=('Helvetica', 18))
l2.pack(pady=20)

e1 = Entry(generator_frame, font=('Helvetica', 18))
e1.pack(pady=20)

b1 = Button(generator_frame, text='Create QR Code', bg='pink', font=('Helvetica', 18), command=on_create)
b1.pack(pady=20)

b2 = Button(generator_frame, text='Clear', bg='pink', font=('Helvetica', 18), command=on_clear)
b2.pack(pady=20)

l1 = Label(generator_frame)
l1.pack(pady=20)

# Right pane: QR Code Decoder
decoder_frame = Frame(paned_window, padx=10, pady=10, highlightbackground='pink', highlightthickness=10)
paned_window.add(decoder_frame, stretch="always")

divider = ttk.Separator(root, orient=VERTICAL)  # Use ttk.Separator for a more visible line
divider.pack(side=LEFT, fill=Y, padx=5)

l2 = Label(decoder_frame, text='QR Code Decoder', font=('Helvetica', 18))
l2.pack(pady=20)

l3 = Label(decoder_frame)
l3.pack(pady=20)

result_label = Label(decoder_frame, text='')
result_label.pack(pady=20)

result_button = Button(decoder_frame, text='Decode QR CODE', bg='pink', font=('Helvetica', 18), command=on_decode)
result_button.pack(pady=20)

root.mainloop()
