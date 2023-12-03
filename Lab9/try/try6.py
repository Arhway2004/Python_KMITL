from tkinter import *
#创建主窗口
win = Tk()
win.config(bg='#8DB6CD')
win.title("C语言中文网")
win.geometry('400x300')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
txt = "C语言中文网，网址是：c.biancheng.net"
msg = Message (win, text=txt,width =60,font=('微软雅黑',10,'bold'))
msg .pack (side=LEFT)
#开始程序循环
win .mainloop ()