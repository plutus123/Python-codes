from tkinter import *
from tkinter import messagebox
import random
import string
import json
window=Tk()
window.title("Password Generator")
window.minsize(500,500)
window.configure(width=200,height=200)
window.config(padx=0,pady=80)
canvas=Canvas(width=200,height=200)
canvas.grid(column=1,row=0)
lock=PhotoImage(file="./passmanager/images.png")
canvas.create_image(100,100,image=lock)
def gen_pass():
    e3.delete(0,END)
    c=5
    password=""
    random_password=[]
    for x in range(0,c):
        x=random.choice(string.ascii_letters)
        password=password+x
        random_password+=x
    d=5
    for y in range(0,d):
        y=random.choice(string.punctuation)
        password=password+y
        random_password+=y
    e=5
    for z in range(0,e):
        z=str(random.randint(0,9))
        password=password+z
        random_password+=z
    random.shuffle(random_password)
    new_password = ""
    for char in random_password:
        new_password+=char
    e3.insert(0,new_password)
    
    
def find_password():
    web=[]
    ep=[]
    try:
        with open("./passmanager/data.json",mode="r") as data:
                dict=json.load(data)
    except FileNotFoundError:
        messagebox.askquestion(title="HelpBox",message=f"File not found")
    else:
        for _ in dict:
            web.append(_)
        if e1.get() in web:
            for _ in dict[e1.get()]:
                ep.append(dict[e1.get()][_])
    if len(ep)==0:
        messagebox.askquestion(title="HelpBox",message=f"No details for the website")
    email=ep[0]
    password=ep[1]
    messagebox.askquestion(title="HelpBox",message=f"The Email is {email} \nThe Password is {password}")
               
               
    
            
    
    
    
    
    
    
def save():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    new_dict={
        a:
            {
                "email":b,
                "password":c
            }
    }
    is_ok=messagebox.askquestion(title=a, message=f"These are the details entered: \nEmail: {b} \nPassword: {c} \nIs it okay? ")
    if is_ok:
        try:
            with open("./passmanager/data.json",mode="r") as datafile:
                # json.dump(new_dict,datafile,indent=4)
                data=json.load(datafile)
        except:
            with open("./passmanager/data.json",mode="w") as datafile:
                json.dump(new_dict,datafile,indent=4)
        else:
            data.update(new_dict)
            with open("./passmanager/data.json",mode="w") as datafile:
                json.dump(data,datafile,indent=4)
        finally:
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
        

l1=Label(text="Website:",font=("Courier",12,"bold"))
l1.grid(column=0,row=1)
l2=Label(text="Email/Username:",font=("Courier",12,"bold"))
l2.grid(column=0,row=2)
l3=Label(text="Password:",font=("Courier",12,"bold"))
l3.grid(column=0,row=3)
e1 = Entry(width=40)
e1.insert(END, string="")
e1.grid(column=1,row=1,columnspan=2)
e1.focus()
e2 = Entry(width=40)
e2.insert(END, string="")
e2.grid(column=1,row=2,columnspan=2)
e3 = Entry(width=40)
e3.insert(END, string="")
e3.grid(column=1,row=3,columnspan=2)

b1=Button(text="Generate Password",bg="white",command=gen_pass)
b1.grid(column=2,row=3)
b2=Button(text="Add",bg="white",width=44,command=save)
b2.grid(column=1,row=4,columnspan=2)
b3=Button(text="Search",bg="white",width=14,command=find_password)
b3.grid(column=2,row=1)



window.mainloop()