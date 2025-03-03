import tkinter 
import tkinter as tk
import sqlite3
import random
from tkvideo import tkvideo
from tkinter import messagebox as ms
from PIL import Image,ImageTk

import re
import numpy






root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Registration Form")



video_label= tk.Label(root)

video_label.place(x=0,y=0)

player=tkvideo("G:/final_fundus_examination/How eyes works_ (Animation) explained within one minute..mp4", video_label,loop=1,size=(w,h))
player.play()

# root=tk.Tk()
# root.configure(background='white')
# w,h=root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w,h))
# # root.title("hello")

# image2=Image.open('C:/Users/COMPUTER/Desktop/Gauri Cource Curricullum/student GUI/Priti Patil/project 1 knee/Project - Copy/Images/1000_F_253175356_73J4XaHNLESTq31lc43PqYJ1CLv72mW0.jpg')
# image2=image2.resize((w,h),Image.ANTIALIAS)

# background_image= ImageTk.PhotoImage(image2)

# background_label=tk.Label(root,image=background_image)

# background_label.image=background_image
  
# background_label.place(x=0,y=0)


#######################################################################################################################################3
# Name = tk.StringVar()
# Email = tk.StringVar()
# password = tk.StringVar()
# password1 = tk.StringVar()

# Address = tk.StringVar()
# Country = tk.StringVar()

# PhoneNo = tk.IntVar()

name = tk.StringVar()
address = tk.StringVar()
#username = tk.StringVar()
Email = tk.StringVar()
country = tk.StringVar()
PhoneNo = tk.IntVar()
var = tk.IntVar()
# age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()


value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('fundas.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT,Gender TEXT, password TEXT)")
db.commit()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# db = sqlite3.connect('project1.db')
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS registration"
#                "(Name TEXT, Email TEXT, password TEXT, Address TEXT,Country  TEXT, PhoneNo TEXT)")
# db.commit()



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 


def insert():
    fname = name.get()
    addr = address.get()
    un = country.get()
    email = Email.get()
    mobile = PhoneNo.get()
    gender = var.get()
    pwd = password.get()
    cnpwd = password1.get()
    
    with sqlite3.connect('fundas.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    # find_user = ('SELECT * FROM registration WHERE Email = ?')
    # c.execute(find_user, [(Email.get())])
    
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    # elif (c.fetchall()):
    #     ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (un == ""):
        ms.showinfo("Message", "Please Enter valid Country")
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('fundas.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(name, address, Email,country, Phoneno, Gender, password) VALUES(?,?,?,?,?,?,?)',
                (fname, addr, email, un ,mobile,gender, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
          
            from subprocess import call
            call(['python','login.py'])

    
    
    


         
            
##################################################################################################################################################
label=tk.Label(root,text="Registeration Form",
               font=('Arial',30),
            
               fg="BLACK")
label.place(x=180,y=90)
canvas=tk.Canvas(root,background="white",borderwidth=5)
canvas.place(x=150,y=150,width=400,height=530)


label=tk.Label(root,text="Name:",font=("Calibri",10),
               bg="white")
label.place(x=200,y=200)

entry=tk.Entry(root,border=2,textvar=name)
entry.place(x=330,y=195)

label=tk.Label(root,text="Email:",font=("Calibri",10),
               bg="white")
label.place(x=200,y=240)

entry=tk.Entry(root,border=2,textvar=Email)
entry.place(x=330,y=245)

label=tk.Label(root,text="Password:",font=("Calibri",10),
               bg="white")
label.place(x=200,y=300)

entry=tk.Entry(root,border=2,show="*",textvar=password)
entry.place(x=330,y=305)

label=tk.Label(root,text="Re-Enter Password:",font=("Calibri",10),
               bg="white")
label.place(x=200,y=350)

entry=tk.Entry(root,border=2,show="*",textvar=password1)
entry.place(x=330,y=355)

label=tk.Label(root,text="Address:",font=("Calibri",10),
               bg="white")
label.place(x=200,y=400)

entry=tk.Entry(root,border=2,textvar=address)
entry.place(x=330,y=405)

label=tk.Label(root,text="FUNDUS EXAMINATION",font=("Calibri",45),
               bg="WHITE",
               width=50,
               height=1)
label.place(x=0,y=0)


# label=tk.Label(root,text="SUFERING FROM KNEE \n PAIN!?",font=("Calibri",30),
#                bg="BLACK",
#                fg="WHITE")
# label.place(x=1050,y=320)

# label=tk.Label(root,text="Register for free consult",font=("Calibri",20),
#                bg="BLACK",
#                fg="WHITE")
# label.place(x=1100,y=440)


# label=tk.Label(root,text="Free information on knee related diseases",font=("Calibri",15),
#                bg="BLACK",
#                fg="WHITE")
# label.place(x=1060,y=480)
# entry=tk.Entry(root,border=2)
# entry.place(x=330,y=455)


label=tk.Label(root,text="Country:",font=("Calibri",10),
                bg="white")
label.place(x=200,y=450)

entry=tk.Entry(root,border=2,textvar=country)
entry.place(x=330,y=455)

label=tk.Label(root,text="Phone no:",font=("Calibri",10),
               bg="white")
label.place(x=200,y=515)



entry=tk.Entry(root,border=2,textvar=PhoneNo)
entry.place(x=330,y=520)

a1=tk.Label(root,text="Gender:",font=("Calibri",10),bg="white").place(x=200,y=570)

tk.Radiobutton(root,text="Male",font=("Calibri",10),bg="white",value=1,variable=var).place(x=330,y=570)
tk.Radiobutton(root,text="FeMale",font=("Calibri",10),bg="white",value=2,variable=var).place(x=400,y=570)







def reg():
    from subprocess import call
    call(['python','Login form.py'])
    
btn=tk.Button(root,text="Create Account",font=("Arial"),width=20, command=insert,
              
              bg="black",
              fg="white",
            )
btn.place(x=250,y=620)



register2=tk.Label(root,text="Already have an account? " ,bg="white",font=('Cambria',11)).place(x=330,y=700)


def reg():
    from subprocess import call
    call(['python','login.py'])

button1=tk.Button(root,text="log in",fg='blue' ,bg='white',command=reg)
button1.place(x=500,y=700)

root.mainloop()