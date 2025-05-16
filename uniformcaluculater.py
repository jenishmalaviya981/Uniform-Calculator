import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫":
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("jenish Calculator")
root.geometry("320x480")
root.config(bg="#2E2E2E")
root.resizable(False, False)


entry = tk.Entry(root, font="Arial 28", bd=10, relief=tk.RIDGE, justify=tk.RIGHT, bg="#1C1C1C", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, sticky="nsew", padx=10, pady=10)


buttons = [
    ['⌫', 'C', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['.', '0', '00', '=']
]


btn_bg = {
    'default': "#4E4E4E",
    'operator': "#FF9500",
    'equal': "#34C759",
    'clear': "#FF3B30",
    'back': "#636366"
}

# Create buttons using grid
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == "=":
            bg_color = btn_bg['equal']
        elif btn_text in "+-*/%":
            bg_color = btn_bg['operator']
        elif btn_text == "C":
            bg_color = btn_bg['clear']
        elif btn_text == "⌫":
            bg_color = btn_bg['back']
        else:
            bg_color = btn_bg['default']
        
        btn = tk.Button(
            root, text=btn_text, font="Arial 18", relief=tk.FLAT,
            bg=bg_color, fg="white", bd=0,
            activebackground="#888"
        )
        btn.grid(row=i+1, column=j, sticky="nsew", padx=2, pady=2)
        btn.bind("<Button-1>", click)

# Make all rows and columns expandable evenly
for i in range(5):  # 5 rows of buttons
    root.grid_rowconfigure(i+1, weight=1)
for j in range(4):  # 4 columns of buttons
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
