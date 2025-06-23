from tkinter import *
from tkinter import filedialog
from stegano import lsb
from tkinter import messagebox

root = Tk()
root.title("PythonGeeks Image Steganography")

def fileopen():
   path = filedialog.askopenfilename(title="Select Image", filetypes=(
       ("PNG Files", "*.png"), ("JPEG Files", "*.jpeg"), ("JPG Files", "*.jpg"), ("All Files", "*.*")))
   ent.delete(0, END)
   ent.insert(0, path)

def img2():
   path = filedialog.asksaveasfilename(title="Save as", defaultextension=".png")
   entry3.delete(0, END)
   entry3.insert(0, path)

def message():
   msg = filedialog.askopenfilename(title="Select Message",
                                    filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
   with open(msg, "r") as file:
       msg = file.read()
       entry2.delete("1.0", END)
       entry2.insert(END, msg)

def encoder():
   path1 = ent.get()
   path2 = entry3.get()
   text = entry2.get()
   response = messagebox.askyesno("PopUp", "Do you want to encode the image")

   if response == 1:
       secret = lsb.hide(path1, text)
       secret.save(path2)
       messagebox.showinfo("Pop Up", "Successfully Encoded the image")
   else:
       messagebox.showwarning("Pop Up", "Unsuccessful,please try again")

frame1 = Frame(root)
frame1.pack(pady=20)
l1 = Label(frame1, text="Select Image:")
l1.pack(side="left", padx=10)
ent = Entry(frame1)
ent.pack(side="left", padx=10)
b1 = Button(frame1, text="Select the file", command=fileopen)
b1.pack()

frame2 = Frame(root)
frame2.pack(pady=20)
l2 = Label(frame2, text="Enter or select Text:")
l2.pack(side="left", padx=10)
entry2 = Entry(frame2)
entry2.pack(side="left", padx=10)
b2 = Button(frame2, text="Select", command=message)
b2.pack(side="right", padx=10)

frame3 = Frame(root)
frame3.pack(pady=20)
l3 = Label(frame3, text="Save Image")
l3.pack(side="left", padx=10)
entry3 = Entry(frame3)
entry3.pack(side="left", padx=10)
b3 = Button(frame3, text="Select", width=20, command=img2)
b3.pack(side="right", padx=10)

b4 = Button(text="Encode", command=encoder)
b4.pack(pady=20)

mainloop()
