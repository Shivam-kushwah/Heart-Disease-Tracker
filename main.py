import tkinter as tk
from tkinter import ttk

from datetime import date
import datetime

import os
import subprocess
import sys
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

from tkinter import messagebox

import webbrowser


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('heart_disease_data.csv')
X = data.drop(columns ='target', axis =1)
Y = data['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

model = LogisticRegression()
model.fit(X_train, Y_train)




window = tk.Tk()
window.title("Heart Disease Tracker")
window.geometry("1250x620")
# window.resizable(False,False)

def analysis():
    # print("Working")
    name = Name.get()
    D1 = Date.get()
    # today = datetime.data.today()


    input=[]

    try:
        A = int(DOB.get())
        current = datetime.datetime.now().year
        db = current-A
        if db<0:
            messagebox.showerror("Wrong Data","Please give ur actual DOB not future!!")
            dob_entry.delete(0,tk.END)

            
    except:
        messagebox.showerror("Missing Data","Please type your year of birth!!")    

    try:
        B = selection()
    except:
        messagebox.showerror("Missing","Please select gender!!!")
        return

    try:
        C = selection2()
    except:
        messagebox.showerror("Missing","Please select Fbs!!!")
        return
    try:
        D = selection3()
    except:
        messagebox.showerror("Missing","Please select Exang!!!")
        return
    try:
        E = int(selection4())
    except:
        messagebox.showerror("Missing","Please select cp!!")
        return
    try:
        F = int(selection5())
    except:
        messagebox.showerror("Missing","Please select Slope!!!")
        return 
    try:
        G = int(ca_combobox.get())
    except:
        messagebox.showerror("Missing","Please select ca")
        return
    try:
        H = int(restecg_combobox.get())
    except:
        messagebox.showerror("Missing","Please select rest ecg")
        return
    try:
        I = int(thal_combobox.get())
    except:
        messagebox.showerror("Missing","Please select thal")
        return 
    try:
        J = int(trestbps.get())
        K = int(chol.get())
        L = float(oldpeak.get())
        M = int(thalach.get())
    except:
        messagebox.showerror("Missing Data","Few missing data entry!") 
        return  


    input = [db,B,E,J,K,C,H,M,D,L,F,G,I]
    input_array = np.asarray(input)
    final_input = input_array.reshape(1,-1)
    prediction = model.predict(final_input) 
    print(prediction) 
    report['text'] = int(prediction)
    if(int(prediction)==0):
        report1['text'] = "No Heart Disease"
    else:
        report1['text'] = "High chances of heart disease"


    f = Figure(figsize=(5,5),dpi = 75)
    a = f.add_subplot(111)
    a.plot(["Sex","fbs","exang"],[B,C,D])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side = tk.BOTTOM,fill = tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=220,height=220,x=550, y=200)
    f.savefig('predicted_graphs/figure1.png', dpi=75)

    f2 = Figure(figsize=(4,4),dpi = 75)
    a2 = f2.add_subplot(111)
    a2.plot(["age","trestbps","chol","thalach"],[db,J,K,M])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side = tk.BOTTOM,fill = tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=220,height=220,x=790, y=200) 
    f2.savefig('predicted_graphs/figure2.png', dpi=75)

    f3 = Figure(figsize=(4,4),dpi = 75)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak","restecg"],[L,H])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side = tk.BOTTOM,fill = tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=220,height=220,x=550, y=420)
    f3.savefig('predicted_graphs/figure3.png', dpi=75)

    f4 = Figure(figsize=(4,4),dpi = 75)
    a4 = f4.add_subplot(111)
    a4.plot(["slope","ca","thal"],[F,G,I])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side = tk.BOTTOM,fill = tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=220,height=220,x=790, y=420)                     
    f4.savefig('predicted_graphs/figure4.png', dpi=75)

def Info():
    icon_window  = tk.Toplevel(window )
    icon_window.title("Info")
    icon_window.geometry("700x600+300+100")

    icon_image = tk.PhotoImage(file="Images/info.png")
    icon_window.iconphoto(False,icon_image)

    tk.Label(icon_window, text="information related to dataset:", font="robot 19 bold").pack(padx=20, pady=20)
    tk.Label(icon_window, text="age - age in years", font = "arial 11").place(x=20, y=100)
    tk.Label(icon_window, text="sex - sex (1 = male; 0 = female)", font = "arial 11").place(x=20, y=130)
    tk.Label(icon_window, text="cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)", font = "arial 11").place(x=20, y=160)
    tk.Label(icon_window, text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)", font = "arial 11").place(x=20, y=190)
    tk.Label(icon_window, text="chol - serum cholestoral in mg/dl", font = "arial 11").place(x=20, y=220)
    tk.Label(icon_window, text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)", font = "arial 11").place(x=20, y=250)
    tk.Label(icon_window, text="restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)", font = "arial 11").place(x=20, y=280)
    tk.Label(icon_window, text="thalach - maximum heart rate achieved", font = "arial 11").place(x=20, y=310)
    tk.Label(icon_window, text="exang - exercise induced angina (1 = yes; 0 = no)", font = "arial 11").place(x=20, y=340)
    tk.Label(icon_window, text="oldpeak - ST depression induced by exercise relative to rest", font = "arial 11").place(x=20, y=370)
    tk.Label(icon_window, text="slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)", font = "arial 11").place(x=20, y=400)
    tk.Label(icon_window, text="ca - number of major vessels (0-3) colored by flourosopy", font = "arial 11").place(x=20, y=430)
    tk.Label(icon_window, text="thal - 0 = normal; 1 = fixed defect; 2 = reversable defect", font = "arial 11").place(x=20, y=460)
    # tk.Label(icon_window, text="", font = "arial 11").place(x=20, y=500)


framebg = "#62a7ff"
framefg = "#fefbfb"

window.configure(bg='#f0ddd5')
# Load the image (ensure the path is correct)
img = tk.PhotoImage(file=r"Images/header.png")

# Create and place the label with the image
head = tk.Label(window, image=img,height=350,bg='#f0ddd5')  
head.place(x=0, y=0)

Heading_entry=tk.Frame(window,width=800,height=160,bg="#df2d4b")
Heading_entry.place(x=450,y=10)

regist = tk.Label(Heading_entry, text = "Registration no.", bg="#df2d4b",fg=framefg ,font=("Arial", 15))
regist.place(x=20,y=0)

date2 = tk.Label(Heading_entry, text = "Date:", bg="#df2d4b",fg=framefg ,font=("Arial", 15))
date2.place(x=430,y=0)


p_name = tk.Label(Heading_entry, text = "Patient Name:", bg="#df2d4b",fg=framefg ,font=("Arial", 15))
p_name.place(x=20,y=90)

dob = tk.Label(Heading_entry, text = "Birth year:", bg="#df2d4b",fg=framefg ,font=("Arial", 15))
dob.place(x=430,y=90)

entry_image = tk.PhotoImage(file="Images/Rounded Rectangle 1.png")
entry_image2 = tk.PhotoImage(file="Images/Rounded Rectangle 2.png")

tk.Label(Heading_entry, image=entry_image, bg="#df2d4b").place(x=20,y=30)
tk.Label(Heading_entry, image=entry_image, bg="#df2d4b").place(x=430,y=30)

tk.Label(Heading_entry, image=entry_image2, bg="#df2d4b").place(x=20,y=120)
tk.Label(Heading_entry, image=entry_image2, bg="#df2d4b").place(x=430,y=120)


Registration = tk.IntVar()
reg_entry = tk.Entry(Heading_entry,textvariable=Registration,width=30,font="arial 15",bg="#0e5363",fg="white",bd="0")
reg_entry.place(x=30,y=45)

Date = tk.StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = tk.Entry(Heading_entry,textvariable=Date,width=15,font='arial 15',bg="#0e5363",fg="white",bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)


Name  = tk.StringVar()
name_entry = tk.Entry(Heading_entry,textvariable=Name,width = 20,font="arial 15",bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB = tk.IntVar()
dob_entry = tk.Entry(Heading_entry,textvariable=DOB,width=15,font="arial 15",bg="#ededed",fg="#222222",bd=0)
dob_entry.place(x=440,y=130)



Detail_entry = tk.Frame(window,width=490,height=280,bg="#dbe0e3")
Detail_entry.place(x=30,y=360)

def selection():
    if (gen.get()==1):
        Gender = 1
        return(Gender)
    elif(gen.get()==2):
        Gender = 0
        return(Gender)
    


def selection2():
    if (fbs.get()==1):
        Fbs = 1
        return(Fbs)
    elif(fbs.get()==2):
        Fbs = 0
        return(Fbs)


def selection3():
    if (exang.get()==1):
        Exang = 1
        return(Exang)
    elif(exang.get()==2):
        Exang = 0
        return(Exang)



def selection4():
    input = cp_combobox.get()
    if(input == "0 = typical angina"):
        return (0) 
    elif(input == "1 = atypical angina"):
        return (1)
    elif(input == "2 = non-anginal pain"):
        return (2)
    elif(input == "3 = asymptotic"):
        return (3) 

def selection5():
    input = slope_combobox.get()
    if(input == "0 = unsloping"):
        return (0) 
    elif(input == "1 = flat"):
        return (1)
    elif(input == "2 = downsloping"):
        return (2) 
    
                    



tk.Label(Detail_entry,text="sex:",font="arial 12",bg=framebg,fg=framefg).place(x=10,y=10)
tk.Label(Detail_entry,text="fbs:",font="arial 12",bg=framebg,fg=framefg).place(x=180,y=10)
tk.Label(Detail_entry,text="exang:",font="arial 12",bg=framebg,fg=framefg).place(x=335,y=10)

gen = tk.IntVar()
R1 = tk.Radiobutton(Detail_entry,text='Male',variable=gen,value=1,command=selection)
R2 = tk.Radiobutton(Detail_entry,text='Female',variable=gen,value=2,command=selection)
R1.place(x=45,y=10)
R2.place(x=93,y=10)

fbs = tk.IntVar()
R3 = tk.Radiobutton(Detail_entry,text='True',variable=fbs,value=1,command=selection2)
R4 = tk.Radiobutton(Detail_entry,text='False',variable=fbs,value=2,command=selection2)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

exang = tk.IntVar()
R5 = tk.Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,command=selection3)
R6 = tk.Radiobutton(Detail_entry,text='No',variable=exang,value=2,command=selection3)
R5.place(x=387,y=10)
R6.place(x=430,y=10)


tk.Label(Detail_entry,text="cp:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
tk.Label(Detail_entry,text="restecg:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
tk.Label(Detail_entry,text="slope:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
tk.Label(Detail_entry,text="ca:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
tk.Label(Detail_entry,text="thal:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)

cp_combobox = ttk.Combobox(Detail_entry,values=['0 = typical angina','1 = atypical angina','2 = non-anginal pain','3 = asymptotic'],state="r",width=20)
restecg_combobox = ttk.Combobox(Detail_entry,values=['0','1','2'],state="r",width=11)
slope_combobox = ttk.Combobox(Detail_entry,values=['0 = unsloping','1 = flat','2 = downsloping'],state="r",width=15)
ca_combobox = ttk.Combobox(Detail_entry,values=['0','1','2','3','4'],state="r",width=11)
thal_combobox = ttk.Combobox(Detail_entry,values=['0','1','2','3'],state="r",width=11)

cp_combobox.place(x=50,y=52)
restecg_combobox.place(x=80,y=92)
slope_combobox.place(x=70,y=132)
ca_combobox.place(x=50,y=172)
thal_combobox.place(x=60,y=212)



tk.Label(Detail_entry,text="smoking:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=50)
tk.Label(Detail_entry,text="trestbps:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=90)
tk.Label(Detail_entry,text="chol:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=130)
tk.Label(Detail_entry,text="thalach:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=170)
tk.Label(Detail_entry,text="old peak:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=210)

trestbps = tk.StringVar()
chol = tk.StringVar()
thalach = tk.StringVar()
oldpeak = tk.StringVar()

trestbps_entry = tk.Entry(Detail_entry, textvariable= trestbps, width=10, font="Arial 15", bg="#ededed", fg="#222222",bd=0)
trestbps_entry.place(x=320, y=90)
chol_entry = tk.Entry(Detail_entry, textvariable= chol, width=10, font="Arial 15", bg="#ededed", fg="#222222",bd=0)
chol_entry.place(x=320, y=130)
thalach_entry = tk.Entry(Detail_entry, textvariable= thalach, width=10, font="Arial 15", bg="#ededed", fg="#222222",bd=0)
thalach_entry.place(x=320, y=170)
oldpeak_entry = tk.Entry(Detail_entry, textvariable= oldpeak, width=10, font="Arial 15", bg="#ededed", fg="#222222",bd=0)
oldpeak_entry.place(x=320, y=210)



square_report_image = tk.PhotoImage(file="Images/Report.png")
report_background = tk.Label(image=square_report_image, bg="#f0ddd5")
report_background.place(x=1050, y=275)

report = tk.Label(window, text=" ",font="arial 35 bold", bg="white",fg="#8dc63f")
report.place(x=1150, y=460)
report1 = tk.Label(window, text=" ",font="arial 10 bold", bg="white")
report1.place(x=1100, y=520)



graph_image = tk.PhotoImage(file="Images/graph.png")
tk.Label(image=graph_image).place(x=550, y=200)
tk.Label(image=graph_image).place(x=800, y=200)
tk.Label(image=graph_image).place(x=550, y=420)
tk.Label(image=graph_image).place(x=800, y=420)

analysis_button = tk.PhotoImage(file="Images/Analysis.png")
tk.Button(window,image=analysis_button,bd=0,bg="#f0ddd5",cursor='hand2', activebackground="#f0ddd5",command=analysis).place(x=1060, y=200)

info_button = tk.PhotoImage(file="Images/info.png")
tk.Button(window, image=info_button, bd=0, bg="#f0ddd5",cursor= 'hand2', activebackground="#f0ddd5", command=Info).place(x=10,y=200)

save_button = tk.PhotoImage(file="Images/save.png")
tk.Button(window, image=save_button, bd=0, bg="#f0ddd5",cursor= 'hand2', activebackground="#f0ddd5").place(x=440,y=200)

button_mode = True
choice = "smoking"

def change_mode():
    global button_mode
    global choice
    if button_mode:
        choice = "non_smoking"
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode = False
    else:
        choice = "smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = True  
    print(choice)    

smoking_icon = tk.PhotoImage(file = "Images/smoker.png")
non_smoking_icon = tk.PhotoImage(file=r"Images/non-smoker.png")
mode = tk.Button(window, image=smoking_icon, bg="#dbe0e3", bd=0, cursor="hand2",command = change_mode)
mode.place(x=350, y=405)



def credit():
    subprocess.Popen([sys.executable, 'credit.py'])
#     icon_window1  = tk.Toplevel(window )
#     icon_window1.title("Credit")
#     icon_window1.geometry("700x600+300+100")

#     icon_image1 = tk.PhotoImage(file="Images/boy.png")
#     icon_window1.iconphoto(False,icon_image1)



#     img = tk.PhotoImage(file="Images/user.png")
#     imgg = tk.Label(icon_window1,image=img)
#     imgg.place(x=10, y=10)


#     link_label = tk.Label(icon_window1, text="Git Hub", fg="blue", cursor="hand2")
#     link_label.pack(pady=20)

#     # Bind the click event to open the link
#     link_label.bind("<Button-1>", open_link)

# def open_link(event):
#     # This function will open the URL in the default web browser
#     webbrowser.open("https://github.com/Shivam-kushwah")    


image_path = "Images/boy.png"  # Path to your image
image = Image.open(image_path)

# Resize the image (e.g., 50x50 pixels)
resized_image = image.resize((50, 50))  # Change these values as needed

# Convert the image to a format Tkinter understands
about_button = ImageTk.PhotoImage(resized_image)

# Create the button with the resized image
button = tk.Button(window, image=about_button, bd=0, cursor='hand2',bg="#df2d4b",activebackground="#df2d4b",command=credit)
button.place(x=20, y=10)

tk.Label(window,text="Credits",font="Arial 10",bg="#df2d4b",fg="white").place(x=22,y=60)



#log out button
# log_out_button = tk.Button(window, bd=0, )

def logout():
    window.destroy()


image_path9 = "Images/logout.png"  # Path to your image
image9 = Image.open(image_path9)

# Resize the image (e.g., 50x50 pixels)
resized_image9 = image9.resize((25, 25))  # Change these values as needed

# Convert the image to a format Tkinter understands
logout_button = ImageTk.PhotoImage(resized_image9)

# Create the button with the resized image
button9 = tk.Button(window, image=logout_button, bd=0, cursor='hand2',bg="#df2d4b",activebackground="#df2d4b",command=logout)
button9.place(x=30, y=100)

tk.Label(window,text="log out",font="Arial 10",bg="#df2d4b",fg="white").place(x=22,y=130)




# Start the main event loop

window.mainloop()
