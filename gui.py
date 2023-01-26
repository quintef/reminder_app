import tkinter as tk
from datetime import datetime, timedelta
import pytz
import threading
import phone
import time



info=[]



def get_name():
    global info
    aSID  = entry1.get()
    info.append(aSID)

    aToken = entry2.get()
    info.append(aToken)

    numberFrom = entry3.get()
    info.append(numberFrom)

    numberTo = entry4.get()
    info.append(numberTo)



    root.destroy()

    

def add_label():

    text = entry.get()
    label = tk.Label(new_window, text=text)
    label.pack()
    text.strip()
    text = text.replace(" ","")

    message = ''
    
    for i in range(len(text)):
        if text[i] == '+':
            message += text[i+1:]
    

def schedule_reminders():
    new_window.destroy()
    new_window2=tk.Tk()
    new_window2.geometry("300x200")
    
    label = tk.Label(new_window2, text="Reminders Have Been Scheduled")
    label.pack()
    new_window2.destroy()
    new_window2.mainloop()
    
    phone.phoneSetup(info)
        
     
    



root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root, text="Auth SID:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Account Token:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="number From:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

label4 = tk.Label(root, text="number to:")
label4.pack()

entry4 = tk.Entry(root)
entry4.pack()

button = tk.Button(root, text="Submit", command=get_name)
button.pack()
root.mainloop()


########### Reminders Page#################################


new_window=tk.Tk()
new_window.geometry("300x200")
entry = tk.Entry(new_window) # create an entry widget
entry.pack()

add_button = tk.Button(new_window, text="Add Reminder \n in this format : \n remindertextgoeshere + 00:00, 01/01", command=add_label) # create a button to add the label
add_button.pack()

add_button = tk.Button(new_window, text="Send Current Reminders", command=schedule_reminders) # create a button to add the label
add_button.pack()

new_window.mainloop()







    
