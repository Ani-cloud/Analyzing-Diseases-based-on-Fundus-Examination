import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *

# Create the main application window
root = tk.Tk()
root.configure(background="whitesmoke")
root.title("Heart disease - Symptoms and causes - Pcmc Hospital")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

# ####For background Image
# image2 = Image.open("E:\FUNDUS\WhatsApp Image 2024-02-05 at 9.49.37 PM.jpeg")
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0) 
# webp_image = Image.open("bg.png")
# desired_width = 155
# aspect_ratio = float(webp_image.height) / webp_image.width
# desired_height = int(aspect_ratio * desired_width)
# resized_image = webp_image.resize((desired_width, desired_height), Image.ANTIALIAS)
# # resized_image = webp_image.resize((desired_width, desired_height), Image.LANCZOS)
# converted_image = ImageTk.PhotoImage(resized_image)
# image_label = tk.Label(root, image=converted_image, height=desired_height, width=desired_width)
# image_label.place(x=0,y=31) 




def reg():
    from subprocess import call
    call(["python","final gui_registration page.py"])
    
    
def log():
    from subprocess import call
    call(["python","login.py"])
    
    
def about():
    from subprocess import call
    call(["python","about-us.py"])
    
    
    
lbl = tk.Label(root, text="FUNDUS EXAMINATION",height=1,width=43, font=('Elephant', 35,' bold '),bg="white",fg="black")
lbl.place(x=1, y=15)


canvas0 = tk.Canvas(root,background="yellow",height=2,width=1500,borderwidth=0, highlightthickness=0)
canvas0.place(x=2,y=15)

canvas0 = tk.Canvas(root,background="yellow",height=2,width=1500,borderwidth=0, highlightthickness=0)
canvas0.place(x=2,y=80)

canvas0 = tk.Canvas(root,background="yellow",height=45,width=1500,borderwidth=0, highlightthickness=0)
canvas0.place(x=2,y=600)
#Create a horizontal line by drawing a line on the Canvas
#line0 = canvas0.create_line(380, 20, 380, 120, fill="white", width=1)

label = tk.Label(root, text='''EYE-CARE''' ,background="white",font=("Times New Roman",35))
label.place(x=100,y=500)


label01=tk.Label(root,text="CENTER",background="white",font=("Times New Roman",15),)
label01.place(x=170,y=550)

button1= tk.Button(root, text='''REGISTER''',background="white" ,font=("Times New Roman",30),bd=0,command=reg )
button1.place(x=750,y=500)



button4= tk.Button(root, text="LOG IN" ,background="white",font=("Times New Roman",30),bd=0,command=log)
button4.place(x=550,y=500)
              
              
button2= tk.Button(root, text='''ABOUT US''' ,background="white",font=("Times New Roman",30),bd=0,command=about)
button2.place(x=1000,y=500)

line01 = canvas0.create_line(860, 20, 860, 120, fill="White", width=1)


image_paths =[
              "202108-Sliders-03Government.png",
              " 202108-Sliders-01EyeDetect-branding.png",
              "202108-Sliders-02Poilice.png",
             " 202108-Sliders-04Corporate.png ",
              "202108-Sliders-05AttorneysInvestigative.png",
             "202108-Sliders-06Corrections.png"
              ]

image_label = tk.Label(root, height=300, width=1500,background="white")
image_label.place(x=0,y=150)

# Index to keep track of the current image
current_image_index = 0



# canvas1=tk.Canvas(root,background="purple")
# canvas1.place(x=15,y=620,width=650,height=30)  

def update_marquee():
    global x, text_size, marquee_canvas
    marquee_canvas.delete("text")
    marquee_canvas.create_text(x, canvas_height / 2, text=marquee_text, fill="white", tags="text", anchor="w", font=("Algerian", text_size))
    x -= 1
    if x < -text_width:
        x = canvas_width
    
    root.after(6, update_marquee)



#Caption Generate For Your Brand
marquee_text = " * Wear Protection to Block Harmful UV Radiation * * Carefully Manage Diabetes * " * 1 # Your text here
text_size = 20  # Increase the text size

canvas_width = 1350  # Increase the canvas width
canvas_height = 32  # Increase the canvas height


marquee_canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightblue")
marquee_canvas.place(x=0,y=605)

x = canvas_width
text_width = len(marquee_text) * 1

update_marquee() 


# canvas1=tk.Canvas(root,background="blue")
# canvas1.place(x=800,y=70,width=430,height=530) 















# Function to update the image label
def update_image():
    global current_image_index
    # Open the next image
    webp_image = Image.open(image_paths[current_image_index])
    desired_width = 1500
    aspect_ratio = float(webp_image.height) / webp_image.width
    desired_height = int(aspect_ratio * desired_width)
    resized_image = webp_image.resize((desired_width, desired_height), Image.ANTIALIAS)
    converted_image = ImageTk.PhotoImage(resized_image)
     # Update the image label
    image_label.configure(image=converted_image)
    image_label.image = converted_image  # Keep a reference to avoid garbage collection
    # Increment the current image index, and loop back to the beginning if necessary
    current_image_index = (current_image_index + 1) % len(image_paths)
    
    # Schedule the next update after a certain delay (e.g., 2000ms or 2 seconds)
    root.after(2000, update_image)

update_image()
root.mainloop()