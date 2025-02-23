from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    encrypted_text = text1.get(1.0, END).strip()  # Get the encrypted text
    if encrypted_text:
        try:
            # Decrypt the text by decoding from Base64
            decrypted_text = base64.b64decode(encrypted_text).decode('utf-8')
            text1.delete(1.0, END)  # Clear the text box
            text1.insert(END, decrypted_text)  # Insert the decrypted text
        except Exception as e:
            messagebox.showerror("Decryption Error", "Invalid encrypted text or password.")
    else:
        messagebox.showwarning("Empty Text", "Please enter text to decrypt.")

def encrypt():
    password = code.get()  # Get the password entered by the user

    if password == "1234":
        text = text1.get(1.0, END).strip()  # Get the text to encrypt
        if text:
            # Encrypt the text by encoding to Base64
            encrypted_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            text1.delete(1.0, END)  # Clear the text box
            text1.insert(END, encrypted_text)  # Insert the encrypted text
        else:
            messagebox.showwarning("Empty Text", "Please enter text to encrypt.")
    else:
        messagebox.showerror("Incorrect Password", "The password you entered is incorrect.")

def main_screen():
    global screen, text1, code

    screen = Tk()
    screen.geometry("375x398")

    # icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")  # Clear the entry field
        text1.delete(1.0, END)  # Clear the text field

    Label(text="Enter text for Encryption and Decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
