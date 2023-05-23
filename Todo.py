# Importing Module :

from tkinter import *
from tkinter import messagebox

# Creating Functions 
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning", "please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

# Configuring + creating  mainwindow and initializing the module

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('PythonGuides')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

# Creating widgets ( Frame,listbox,scrollbar,entry,button)

frame = Frame(ws)
frame.pack(pady=10)

# Adding Listbox:

lb= Listbox (
    frame,
    width=25,
    height=8,
    font=('Times',18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",  
)
lb.pack(side=LEFT , fill=BOTH)

#Adding Dummy data:

task_List = [
    'write software',
    'write documentation',
    'take a nap',
    'Learn something' 
]
 
for item in task_List:
   lb.insert(END,item)   


# Adding Scrollbar:

sb = Scrollbar(frame)
sb.pack(side=RIGHT , fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Adding entry box:

my_entry = Entry(
    ws,
    font=('Times',24)
)

my_entry.pack(pady=20)

# Adding another frame for buttons:

Button_frame = Frame(ws)
Button_frame.pack(pady=20)


# Adding Buttons:

addTask_btn = Button(
    Button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    Button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)

delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

# New task function:

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

# Delete Task function:
def deleteTask():
    lb.delete(ANCHOR)


ws.mainloop()


