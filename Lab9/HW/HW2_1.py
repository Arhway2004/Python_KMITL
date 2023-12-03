import tkinter as tk
from tkinter import colorchooser

class ColorMixerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("颜色操作器")
        
        # 创建颜色选择按钮
        self.color1_button = tk.Button(root, text="选择颜色1", command=self.choose_color1, width=15)
        self.color2_button = tk.Button(root, text="选择颜色2", command=self.choose_color2, width=15)
        
        # 创建操作按钮
        self.mix_button = tk.Button(root, text="混合颜色", command=self.mix_colors)
        self.add_button = tk.Button(root, text="相加颜色", command=self.add_colors)
        self.subtract_button = tk.Button(root, text="相减颜色", command=self.subtract_colors)
        
        # 显示操作结果颜色
        self.result_label = tk.Label(root, text="", bg="white")
        
        # 布局
        self.color1_button.grid(row=0, column=0, padx=10, pady=10)
        self.color2_button.grid(row=0, column=1, padx=10, pady=10)
        self.mix_button.grid(row=1, column=0, padx=10, pady=10)
        self.add_button.grid(row=1, column=1, padx=10, pady=10)
        self.subtract_button.grid(row=1, column=2, padx=10, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        self.color1 = "white"
        self.color2 = "white"

    def choose_color1(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color1 = color
            self.color1_button.config(background=color)
            
    def choose_color2(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color2 = color
            self.color2_button.config(background=color)
    
    def mix_colors(self):
        # 在这里执行颜色混合操作，这里简单地使用平均值作为混合方法
        r1, g1, b1 = self.hex_to_rgb(self.color1)
        r2, g2, b2 = self.hex_to_rgb(self.color2)
        mixed_color = "#{:02X}{:02X}{:02X}".format((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2)
        self.display_result("混合颜色: " + mixed_color, mixed_color)
    
    def add_colors(self):
        r1, g1, b1 = self.hex_to_rgb(self.color1)
        r2, g2, b2 = self.hex_to_rgb(self.color2)
        added_color = "#{:02X}{:02X}{:02X}".format(min(r1 + r2, 255), min(g1 + g2, 255), min(b1 + b2, 255))
        self.display_result("相加颜色: " + added_color, added_color)
    
    def subtract_colors(self):
        r1, g1, b1 = self.hex_to_rgb(self.color1)
        r2, g2, b2 = self.hex_to_rgb(self.color2)
        subtracted_color = "#{:02X}{:02X}{:02X}".format(max(r1 - r2, 0), max(g1 - g2, 0), max(b1 - b2, 0))
        self.display_result("相减颜色: " + subtracted_color, subtracted_color)
    
    def display_result(self, text, background):
        self.result_label.config(text=text, bg=background)
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorMixerApp(root)
    root.mainloop()
