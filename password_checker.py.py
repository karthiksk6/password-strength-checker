# password_checker.py
import tkinter as tk
from tkinter import messagebox
import re
import string
import random

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    if strength <= 2:
        return "Weak", feedback
    elif strength == 3 or strength == 4:
        return "Moderate", feedback
    else:
        return "Strong", ["Great job!"]

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(12))

def evaluate():
    password = entry.get()
    strength, feedback = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}")
    feedback_text.delete(1.0, tk.END)
    for item in feedback:
        feedback_text.insert(tk.END, f"- {item}\n")
    if strength != "Strong":
        suggestion = generate_strong_password()
        feedback_text.insert(tk.END, f"\nSuggested Password: {suggestion}")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter your password:").pack()
entry = tk.Entry(root, width=40, show="*")
entry.pack()

tk.Button(root, text="Check Strength", command=evaluate).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()

feedback_text = tk.Text(root, height=10, width=50)
feedback_text.pack()

root.mainloop()