import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

class ColorMixerApp:
    def __init__(self, root):
        self.root = root
        root.title("Color Mixer")

        self.color1_button = tk.Button(root, text="Select Color 1", command=self.choose_color1, width=15)
        self.color2_button = tk.Button(root, text="Select Color 2", command=self.choose_color2, width=15)
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image, width=15)
        self.camera_button = tk.Button(root, text="Open Camera", command=self.open_camera, width=15)
        
        self.color1_label = tk.Label(root, text="Color 1", bg="white", width=15)
        self.color2_label = tk.Label(root, text="Color 2", bg="white", width=15)
        
        self.color1_button.grid(row=0, column=0, padx=10, pady=10)
        self.color2_button.grid(row=0, column=1, padx=10, pady=10)
        self.upload_button.grid(row=1, column=0, padx=10, pady=10)
        self.camera_button.grid(row=1, column=1, padx=10, pady=10)
        self.color1_label.grid(row=2, column=0, padx=10, pady=10)
        self.color2_label.grid(row=2, column=1, padx=10, pady=10)
        
        self.color1 = "white"
        self.color2 = "white"
        
        self.camera = None

    def choose_color1(self):
        color = colorchooser.askcolor()
        if color:
            self.color1 = color[1]
            self.color1_label.config(bg=self.color1)

    def choose_color2(self):
        color = colorchooser.askcolor()
        if color:
            self.color2 = color[1]
            self.color2_label.config(bg=self.color2)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if file_path:
            image = Image.open(file_path)
            self.process_and_display_image(image)

    def open_camera(self):
        if not self.camera:
            self.camera = cv2.VideoCapture(0)
        
        ret, frame = self.camera.read()
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_pil = Image.fromarray(image)
            self.process_and_display_image(image_pil)

    def process_and_display_image(self, image):
        resized_image = image.resize((100, 100))
        color = self.get_dominant_color(resized_image)
        self.display_result("Extracted Color: " + color, color)

    def get_dominant_color(self, image):
        pixels = np.array(image)
        pixels = pixels.reshape(-1, 3)
        dominant_color = pixels.mean(axis=0)
        return "#{:02X}{:02X}{:02X}".format(int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2]))

    def display_result(self, text, color):
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")
        result_label = tk.Label(result_window, text=text, bg=color, width=20, height=5)
        result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorMixerApp(root)
    root.mainloop()
