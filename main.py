import tkinter as tk
from tkinter import messagebox

def sum_nums():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        wynik = a + b
        sum_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Error", "Give right data!")

def sub_nums():
    try:
        a = float(entry3.get())
        b = float(entry4.get())
        wynik = a - b
        sub_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Error", "Give right data!")

def mult_nums():
    try:
        a = float(entry5.get())
        b = float(entry6.get())
        wynik = a * b
        mult_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Error", "Give right data!")

def div_nums():
    try:
        a = float(entry7.get())
        b = float(entry8.get())
        if b == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            wynik = a / b
            div_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Error", "Give right data!")

root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="Addition").grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(root, text="Number 1:").grid(row=1, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=2, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Add", command=sum_nums).grid(row=3, column=0, columnspan=2, pady=5)
sum_label = tk.Label(root, text="Result: ")
sum_label.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Subtraction").grid(row=5, column=0, columnspan=2, pady=10)
tk.Label(root, text="Number 1:").grid(row=6, column=0, padx=5, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=7, column=0, padx=5, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=7, column=1, padx=5, pady=5)

tk.Button(root, text="Subtract", command=sub_nums).grid(row=8, column=0, columnspan=2, pady=5)
sub_label = tk.Label(root, text="Result: ")
sub_label.grid(row=9, column=0, columnspan=2, pady=5)

tk.Label(root, text="Multiplication").grid(row=0, column=3, columnspan=2, pady=5)
tk.Label(root, text="Number 1:").grid(row=1, column=3, padx=5, pady=5)
entry5 = tk.Entry(root)
entry5.grid(row=1, column=4, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=2, column=3, padx=5, pady=5)
entry6 = tk.Entry(root)
entry6.grid(row=2, column=4, padx=5, pady=5)

tk.Button(root, text="Multiply", command=mult_nums).grid(row=3, column=3, columnspan=2, pady=5)
mult_label = tk.Label(root, text="Result: ")
mult_label.grid(row=4, column=3, columnspan=2, pady=5)

tk.Label(root, text="Division").grid(row=5, column=3, columnspan=2, pady=10)
tk.Label(root, text="Number 1:").grid(row=6, column=3, padx=5, pady=5)
entry7 = tk.Entry(root)
entry7.grid(row=6, column=4, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=7, column=3, padx=5, pady=5)
entry8 = tk.Entry(root)
entry8.grid(row=7, column=4, padx=5, pady=5)

tk.Button(root, text="Divide", command=div_nums).grid(row=8, column=3, columnspan=2, pady=5)
div_label = tk.Label(root, text="Result: ")
div_label.grid(row=9, column=3, columnspan=2, pady=5)

root.mainloop()
