import tkinter as tk
from tkinter import ttk
import subprocess
import time
import sys
from PIL import Image, ImageTk
import webbrowser

root = tk.Tk()
root.title("Credits")
root.config(bg="white")
root.geometry("700x600+300+100")

# img = tk.PhotoImage(file="Images/shivam.png")
# imgg = tk.Label(root,image=img)
# imgg.place(x=10, y=10)

image_path = "Images/shiv.png"  # Path to your image
image = Image.open(image_path)

# Resize the image (e.g., 50x50 pixels)
resized_image = image.resize((150,150))  # Change these values as needed

# Convert the image to a format Tkinter understands
about_button = ImageTk.PhotoImage(resized_image)

# Create the button with the resized image
button = tk.Label(root, image=about_button, bd=0)
button.place(x=20, y=10)

tk.Label(root,text="Shivam Kushwah",font="arial 18",bg="white",fg="black").place(x=200,y=40)

def git1():
    webbrowser.open("https://github.com/Shivam-kushwah")

image_path1 = "Images/github.png"  # Path to your image
image1 = Image.open(image_path1)

# Resize the image (e.g., 50x50 pixels)
resized_image1 = image1.resize((40,40))  # Chahese values as needed

# Convert the image to a format Tkinter understands
about_button1 = ImageTk.PhotoImage(resized_image1)

# Create the button with the resized image
button1 = tk.Button(root, image=about_button1, bd=0,bg="white",command=git1)
button1.place(x=210, y=80)









def link1():
    webbrowser.open("https://www.linkedin.com/in/shivamkushwah?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")

image_path2 = "Images/linkedin.png"  # Path to your image
image2 = Image.open(image_path2)

# Resize the image (e.g., 50x50 pixels)
resized_image2 = image2.resize((40,40))  # Chahese values as needed

# Convert the image to a format Tkinter understands
about_button2 = ImageTk.PhotoImage(resized_image2)

# Create the button with the resized image
button2 = tk.Button(root, image=about_button2, bd=0,bg="white",command=link1)
button2.place(x=270, y=80)

# tk.Label(root,text="Shivam Kushwah",font="arial 18",bg="white",fg="black").place(x=200,y=40)


#................................shivam's about ends here....................................





image_path3 = "Images/chandu.png"  # Path to your image
image3 = Image.open(image_path3)

# Resize the image (e.g., 50x50 pixels)
resized_image3 = image3.resize((150,150))  # Change these values as needed

# Convert the image to a format Tkinter understands
about_button3 = ImageTk.PhotoImage(resized_image3)

# Create the button with the resized image
button3 = tk.Label(root, image=about_button3, bd=0)
button3.place(x=20, y=180)

tk.Label(root,text="Chandresh Garg",font="arial 18",bg="white",fg="black").place(x=200,y=210)

def git2():
    webbrowser.open("https://github.com/Chandresh-Garg")

image_path4 = "Images/github.png"  # Path to your image
image4 = Image.open(image_path4)

# Resize the image (e.g., 50x50 pixels)
resized_image4 = image4.resize((40,40))  # Chahese values as needed

# Convert the image to a format Tkinter understands
about_button4 = ImageTk.PhotoImage(resized_image4)

# Create the button with the resized image
button4 = tk.Button(root, image=about_button4, bd=0,bg="white",command=git2)
button4.place(x=210, y=250)









def link2():
    webbrowser.open("https://www.linkedin.com/in/chandresh-garg-356213292?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")

image_path5 = "Images/linkedin.png"  # Path to your image
image5 = Image.open(image_path5)

# Resize the image (e.g., 50x50 pixels)
resized_image5 = image5.resize((40,40))  # Chahese values as needed

# Convert the image to a format Tkinter understands
about_button5 = ImageTk.PhotoImage(resized_image5)

# Create the button with the resized image
button5 = tk.Button(root, image=about_button5, bd=0,bg="white",command=link2)
button5.place(x=270, y=250)

# tk.Label(root,text="Chandresh Garg",font="arial 18",bg="white",fg="black").place(x=200,y=40)

root.mainloop()
