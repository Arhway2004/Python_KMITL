import tkinter as tk

screen = tk.Tk(screenName=None, baseName=None, className="JJ", useTk=1)
screen.title("Arhway")
screen.geometry('450x300')#大小
screen.iconbitmap("33FF52")#logo
screen["background"] = "#C9C9C9"#背景
text=tk.Label(screen,text="C语言中文网,欢迎您",bg="yellow",fg="red",font=('Times', 20, 'bold italic'))
text.pack()#line 8,9 is together
button=tk.Button(screen,text="关闭",command=screen.quit)
button.pack(side="bottom")
_ok = tk.Button(screen,text ="OK")
_ok.pack(side = "bottom")

screen.mainloop()
