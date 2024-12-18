import tkinter as tk
from tkinter import ttk
import subprocess
import time
import sys
from PIL import Image, ImageTk

# Function to open the second GUI after closing the welcome window
def open_second_gui():
    # Close the current window
    root.destroy()

    # Open the second Python file using subprocess
    subprocess.Popen([sys.executable, 'main.py'])

# Function to update the progress bar
def update_progress_bar():
    # Update progress bar for 5 seconds
    for i in range(101):  # Progress from 0 to 100
        progress_bar['value'] = i
        root.update_idletasks()  # Update the UI
        time.sleep(0.03)  # Delay for 30 milliseconds (simulating progress)
    
    # After the progress bar is complete, open the second GUI
    open_second_gui()

# Function to change the background color of the image
def change_image_background(image, color="#333333"):
    # Convert the image to RGBA (if it's not already in RGBA mode)
    image = image.convert("RGBA")
    
    # Create a new image with the desired background color
    background = Image.new("RGBA", image.size, color)
    
    # Paste the original image onto the background, using the alpha channel as a mask
    background.paste(image, (0, 0), image)
    
    return background

# Create the main window (welcome window)
root = tk.Tk()
root.title("Heart Disease tracker Welcome")

# Set the dimensions and position of the window
root.geometry("600x500")  # Width x Height

root.config(bg="#333333")

# Add an image to the welcome screen
image_path = "Images/welcome.png"  # Replace with your image file path
image = Image.open(image_path)

# Change the background color of the image to #333333
image_with_bg = change_image_background(image, color="#333333")

# Resize the image (if needed)
image_with_bg = image_with_bg.resize((550, 300))

# Convert the image to a Tkinter-compatible photo image
photo = ImageTk.PhotoImage(image_with_bg)

# Label for the image
image_label = tk.Label(root, image=photo, bd=0, relief="flat", bg="#333333")
image_label.pack(pady=20)

# Add a label to display the welcome message
welcome_label = tk.Label(root, text="Welcome to the Heart Disease Tracker !!!", font=("Helvetica", 16),bg="#333333",fg="white")
welcome_label.pack(expand=True)

# Add a progress bar
progress_bar = ttk.Progressbar(root, length=200, mode='determinate', maximum=100)
progress_bar.pack(pady=20)

# Start the progress bar update in a separate thread
root.after(100, update_progress_bar)

# Start the Tkinter event loop
root.mainloop()
