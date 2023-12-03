import tkinter as tk

def append_to_display(char):
    current_text = display_var.get()
    display_var.set(current_text + char)

def delete_rightmost_char():
    current_text = display_var.get()
    display_var.set(current_text[:-1])

def dial_number():
    current_number = display_var.get()
    popup_message = f"Dialing {current_number}"
    popup = tk.Toplevel(root)
    popup_label = tk.Label(popup, text=popup_message)
    popup_label.pack()
    popup_button = tk.Button(popup, text="OK", command=popup.destroy)
    popup_button.pack()

root = tk.Tk()
root.title("Phone Dialer")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 24))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#',
    'Talk', '<'
]

row, col = 1, 0
for button_text in buttons:
    if button_text == '<':
        button = tk.Button(root, text=button_text, command=delete_rightmost_char)
    elif button_text == 'Talk':
        button = tk.Button(root, text=button_text, command=dial_number)
    else:
        button = tk.Button(root, text=button_text, command=lambda text=button_text: append_to_display(text))
    button.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

root.mainloop()
