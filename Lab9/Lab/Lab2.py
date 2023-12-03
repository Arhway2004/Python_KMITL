# import tkinter as  T
# from tkinter import messagebox

# def USD():
#     current_value = float(entry1.get())
#     new_value = current_value *30
#     return new_value
# def THB():
#     current_value = float(entry1.get())
#     new_value = current_value / 30
#     return new_value

# def click_button_1():
#     messagebox.showinfo(title='温馨提示', message=f"{float(entry1.get()):.2f}USD = {THB():.2f}THB")

# def click_button_2():
#     messagebox.showinfo(title='温馨提示', message=f"{float(entry1.get()):.2f}THB = {USD():.2f}USD")

# screen = T.Tk(screenName=None, baseName=None, className="JJ", useTk=1)
# screen.title("Currency Converter")
# screen.geometry('450x300')
# # x = T.StringVar()
# # x.set("50")
# # label = T.Label(screen, textvariable=x).pack()
# entry1.insert("")

# button_1 = T.Button(screen,text='USD->THB',width=5, height=2,command=click_button_2).pack()
# button_2 = T.Button(screen,text='THB->USD',width=5, height=2,command=click_button_1).pack()

# T.mainloop()
import tkinter as T
from tkinter import messagebox

def USD_to_THB():
    current_value = float(entry.get())
    new_value = current_value * 30
    return new_value

def THB_to_USD():
    current_value = float(entry.get())
    new_value = current_value / 30
    return new_value

def click_button_1():
    messagebox.showinfo(title='Conversion Result', message=f"{float(entry.get()):.2f} USD = {USD_to_THB():.2f} THB")

def click_button_2():
    messagebox.showinfo(title='Conversion Result', message=f"{float(entry.get()):.2f} THB = {THB_to_USD():.2f} USD")

screen = T.Tk()
screen.title("Currency Converter")
screen.geometry('450x300')

entry = T.Entry(screen)
entry.pack()

button_1 = T.Button(screen, text='USD -> THB', width=10, height=2, command=click_button_1)
button_1.pack()

button_2 = T.Button(screen, text='THB -> USD', width=10, height=2, command=click_button_2)
button_2.pack()

T.mainloop()
