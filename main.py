import tkinter as tk
from tkinter import messagebox

def sum_nums():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        wynik = a + b
        sum_label.config(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Błąd", "Podaj prawidłowe dane!")

def sub_nums():
    try:
        a = float(entry3.get())
        b = float(entry4.get())
        wynik = a - b
        sub_label.config(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Błąd", "Podaj prawidłowe dane!")

root = tk.Tk()
root.title("Kalkulator")

tk.Label(root, text="Dodawanie").grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(root, text="Liczba 1:").grid(row=1, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Liczba 2:").grid(row=2, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Dodaj", command=sum_nums)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

sum_label = tk.Label(root, text="Wynik: ")
sum_label.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Odejmowanie").grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(root, text="Liczba 1:").grid(row=6, column=0, padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Liczba 2:").grid(row=7, column=0, padx=10, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=7, column=1, padx=10, pady=5)

sub_button = tk.Button(root, text="Odejmij", command=sub_nums)
sub_button.grid(row=8, column=0, columnspan=2, pady=5)

sub_label = tk.Label(root, text="Wynik: ")
sub_label.grid(row=9, column=0, columnspan=2, pady=5)

root.mainloop()
