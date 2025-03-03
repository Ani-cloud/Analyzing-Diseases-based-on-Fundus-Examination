
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
# from neupy import algorithms
# from neupy.layers import *
import numpy as np
import time
from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Flight Delay Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('3.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text="Pcos Detection System ",font=("Times New Roman", 30, 'bold'),
                    background="#778899", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)

# img = Image.open('logo.png')
# img = img.resize((100,70), Image.ANTIALIAS)
# logo_image = ImageTk.PhotoImage(img)

# logo_label = tk.Label(root, image=logo_image)
# logo_label.image = logo_image
# logo_label.place(x=40, y=10)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#

            # We now need to add a logistic layer on top of the MLP
def Data_Preprocessing():
    data = pd.read_csv("dataset1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['MONTH'] = le.fit_transform(data['MONTH'])
    
    data['DAY'] = le.fit_transform(data['DAY'])
    
    #data['AIRLINE'] = le.fit_transform(data['AIRLINE'])

    data['FLIGHT_NUMBER'] = le.fit_transform(data['FLIGHT_NUMBER'])
    
    #data['TAIL_NUMBER'] = le.fit_transform(data['TAIL_NUMBER'])
    
    #data['ORIGIN_AIRPORT'] = le.fit_transform(data['ORIGIN_AIRPORT'])
    
    #['DESTINATION_AIRPORT'] = le.fit_transform(data['DESTINATION_AIRPORT'])
    
    data['DISTANCE'] = le.fit_transform(data['DISTANCE'])
    
    data['SCHEDULED_ARRIVAL'] = le.fit_transform(data['SCHEDULED_ARRIVAL'])
    
    data['ARRIVAL_TIME'] = le.fit_transform(data['ARRIVAL_TIME'])

    
    
  

    """Feature Selection => Manual"""
    x = data.drop(['YEAR','Delay'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Delay']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)


def Model_Training():
    data = pd.read_csv("dataset1.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['MONTH'] = le.fit_transform(data['MONTH'])
    
    data['DAY'] = le.fit_transform(data['DAY'])
    
    #data['AIRLINE'] = le.fit_transform(data['AIRLINE'])

    data['FLIGHT_NUMBER'] = le.fit_transform(data['FLIGHT_NUMBER'])
    
    #data['TAIL_NUMBER'] = le.fit_transform(data['TAIL_NUMBER'])
    
    #data['ORIGIN_AIRPORT'] = le.fit_transform(data['ORIGIN_AIRPORT'])
    
    #data['DESTINATION_AIRPORT'] = le.fit_transform(data['DESTINATION_AIRPORT'])
    
    data['DISTANCE'] = le.fit_transform(data['DISTANCE'])
    
    data['SCHEDULED_ARRIVAL'] = le.fit_transform(data['SCHEDULED_ARRIVAL'])
    
    data['ARRIVAL_TIME'] = le.fit_transform(data['ARRIVAL_TIME'])

    
    
  

    """Feature Selection => Manual"""
    x = data.drop(['YEAR','Delay'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Delay']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=4)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SOFTWARE_MODEL.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"F_model.joblib")
    print("Model saved as F_model.joblib")



# def call_file():
#     import Check_Heart
#     Check_Heart.Train()





def log():
    from subprocess import call
    call(["python","Check.py"])
    
def window():
  root.destroy()


# button1 = tk.Button(root, text="Model Training", command=Model_Training, width=12, height=1,font=('times', 20, ' bold '), bg="white", fg="black")
# button1.place(x=80, y=160)
button2 = tk.Button(root, text="select image ",command=log,width=12, height=1,font=('times', 20, ' bold '), bg="white", fg="black")
button2.place(x=80, y=250)

button3 = tk.Button(root, text="image pridection",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="red", fg="black")
button3.place(x=80, y=330)

button2 = tk.Button(root, text="Check Flight",command=log,width=12, height=1,font=('times', 20, ' bold '), bg="white", fg="black")
button2.place(x=80, y=250)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="red", fg="black")
button3.place(x=80, y=330)

label_l1 = tk.Label(root, text="** Pcos Detection System @2023 By __ **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=250, height=4)
label_l1.place(x=0, y=780)
root.mainloop()