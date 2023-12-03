# import tkinter as tk
# win = tk.Tk()
# # 设置主窗口
# win.geometry('250x100')
# win.title("C语言中文网")
# win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# win.resizable(0,0)
# # 创建输入框控件
# entry1 = tk.Entry(win)
# # 放置输入框，并设置位置
# entry1.pack(padx=20, pady=20)
# entry1.delete(0, "end")
# # 插入默认文本
# entry1.insert(0,'C语言中文网，网址：c.biancheng.net')
# # 得到输入框字符串
# print(entry1.get())
# # 删除所有字符
# # entry1.delete(0, tk.END)
# win.mainloop()
import tkinter as tk
win =tk.Tk()
# 设置主窗口
win.geometry('250x100')
win.title("C语言中文网")
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.resizable(0,0)
# 新建文本标签
labe1 = tk.Label(win,text="账号：")
labe2 = tk.Label(win,text="密码：")
# grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
labe1.grid(row=0)
labe2.grid(row=1)
# 为上面的文本标签，创建两个输入框控件
entry1 = tk.Entry(win)
entry2 = tk.Entry(win)
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
# 显示主窗口
win.mainloop()