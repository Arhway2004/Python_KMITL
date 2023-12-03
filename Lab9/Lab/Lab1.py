import tkinter as  T

def increment_x():
    current_value = int(x.get())
    new_value = current_value + 1
    x.set(new_value)
def decrement_x():
    current_value = int(x.get())
    new_value = current_value - 1
    x.set(new_value)
def Reset_x():
    new_value = "0"
    x.set(new_value)

screen = T.Tk(screenName=None, baseName=None, className="JJ", useTk=1)
screen.title("Spiner")
screen.geometry('450x300')
x = T.StringVar()
x.set("0")
label = T.Label(screen, textvariable=x).pack()
# text=T.Label(screen,text=x).pack(side="left")
button_1 = T.Button(screen,text='+',width=5, height=2,command=increment_x).pack()
button_2 = T.Button(screen,text='-',width=5, height=2,command=decrement_x).pack()
button_3 = T.Button(screen,text='Reset',width=5, height=2,command=Reset_x).pack()

T.mainloop()