import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
import random
import string

# --- Password Strength Checker ---
def check_strength():
    password = entry.get()

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        strength = "Very Strong 💪"
        color = "green"
    elif score == 4:
        strength = "Strong"
        color = "blue"
    elif score == 3:
        strength = "Moderate"
        color = "orange"
    elif score == 2:
        strength = "Weak"
        color = "red"
    else:
        strength = "Very Weak ❌"
        color = "darkred"

    result_label.config(text=f"Strength: {strength}", fg=color)
    progress["value"] = score * 20

    details = f"""
    • Length OK: {not length_error}
    • Has Digit: {not digit_error}
    • Has Uppercase: {not uppercase_error}
    • Has Lowercase: {not lowercase_error}
    • Has Symbol: {not symbol_error}
    """
    details_label.config(text=details.strip())

    # Save report
    with open("password_report.txt", "a") as f:
        f.write(f"\nPassword Checked: {password}\n{details.strip()}\nStrength: {strength}\n{'-'*30}\n")

# --- Toggle Password Visibility ---
def toggle_visibility():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_btn.config(text='🙈 Hide')
    else:
        entry.config(show='*')
        toggle_btn.config(text='👁️ Show')

# --- Suggest Strong Password ---
def suggest_password():
    length = 12
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    suggestion = ''.join(random.choice(chars) for _ in range(length))
    entry.delete(0, tk.END)
    entry.insert(0, suggestion)
    messagebox.showinfo("Suggested Password", f"Try this strong password:\n\n{suggestion}")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 Password Strength Analyzer")
root.geometry("450x450")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack()

# Toggle button
toggle_btn = tk.Button(root, text="👁️ Show", command=toggle_visibility, font=("Arial", 10))
toggle_btn.pack(pady=5)

# Buttons
tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Suggest Strong Password", command=suggest_password, font=("Arial", 12)).pack(pady=5)

# Output labels
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=5)

details_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
details_label.pack(pady=10)

# Run App
root.mainloop()
