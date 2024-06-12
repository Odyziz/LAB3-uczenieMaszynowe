import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumber:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        # Ustawienie rozmiaru okna
        self.root.geometry("400x300")

        self.random_number = random.randint(1, 1000)
        self.guess_count = 0

        self.label = tk.Label(root, text="Zgadnij liczbę między 1 a 1000")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Potwierdź", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 1000:
                raise ValueError("Liczba poza zakresem")
        except ValueError as e:
            if str(e) == "Liczba poza zakresem":
                messagebox.showerror("Błąd", "Wprowadź liczbę całkowitą od 1 do 1000")
            else:
                messagebox.showerror("Błąd", "Wpisz poprawną liczbę całkowitą")
            return

        self.guess_count += 1

        if guess < self.random_number:
            self.result_label.config(text="Za mała, spróbuj ponownie")
        elif guess > self.random_number:
            self.result_label.config(text="Za duża, spróbuj ponownie")
        else:
            self.result_label.config(text=f"Brawo! Odgadłeś liczbę przy {self.guess_count} próbie.")
            messagebox.showinfo("Wygrana", f"Brawo! Odgadłeś liczbę przy {self.guess_count} próbie.")
            self.reset_game()

    def reset_game(self):
        self.random_number = random.randint(1, 1000)
        self.guess_count = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        messagebox.showinfo("Nowa gra", "Wylosowano nową liczbę. Zacznij zgadywać!")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumber(root)
    root.mainloop()

