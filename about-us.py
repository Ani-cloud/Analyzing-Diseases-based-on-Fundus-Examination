import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *

# Create the main application window
root = tk.Tk()
root.configure(background="white")
root.title("FUNDUS EXAMINATION")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

l2 = tk.Label( text="ABOUT US -----",bg="white", width=12, font=("Times new roman", 15, "bold"),bd=5, fg="black")
l2.place(x=100, y=150)


l2 = tk.Label( text="OUR MISSON",bg="white", width=15, font=('Calibri', 30, "bold"),bd=5, fg="YELLOW")
l2.place(x=150, y=230)

l2 = tk.Label( text='''Welcome to the Fundus Examination site.
              On these pages you will be able to learn more 
              about our doctors and the services they provide
              as well as general information about your eyes.
              We hope that you find this site informative and
              easy to navigate.

              The mission of is to provide the most comprehensive
              eye care services to the residents  all Over World 
              and surrounding areas in a friendly, inviting and
              professional environment''')
l2.place(x=150, y=300,)




# image_paths =[
#               # "C0309334-Fundus_oculi_examination.jpg",
#               # "C0040875-Fundus_oculi_examination.jpg",
#               # "fundus-camera-use-examination-eye-260nw-394578469.webp",
#               # "fundus-camera-use-examination-eye-260nw-394578469.webp",
#               # "fundus-camera-use-examination-eye-260nw-394578481.webp"
#               ]

# image_label = tk.Label(root, height=500, width=500)
# image_label.place(x=700,y=150)

# current_image_index = 0



# Function to update the image label
# def update_image():
#     global current_image_index
#     # Open the next image
#     webp_image = Image.open(image_paths[current_image_index])
#     desired_width = 1500
#     aspect_ratio = float(webp_image.height) / webp_image.width
#     desired_height = int(aspect_ratio * desired_width)
#     resized_image = webp_image.resize((desired_width, desired_height), Image.ANTIALIAS)
#     converted_image = ImageTk.PhotoImage(resized_image)
#      # Update the image label
#     image_label.configure(image=converted_image)
#     image_label.image = converted_image  # Keep a reference to avoid garbage collection
#     # Increment the current image index, and loop back to the beginning if necessary
#     current_image_index = (current_image_index + 1) % len(image_paths)
    
#     # Schedule the next update after a certain delay (e.g., 2000ms or 2 seconds)
#     root.after(2000, update_image)

# update_image()


root.mainloop()
