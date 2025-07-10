# 🔐 Password Strength Checker Tool

A Python-based GUI application that evaluates the strength of user-entered passwords and provides real-time feedback and improvement suggestions.

---

## 📌 Project Overview

Weak passwords are one of the primary causes of data breaches. This project aims to:
- Help users create stronger, more secure passwords.
- Provide educational feedback based on standard security practices.
- Suggest strong password alternatives using randomized generation.

---

## 🎯 Objective

Develop a GUI tool that:
- Evaluates password strength in real-time.
- Checks compliance with 5 key security rules.
- Provides feedback and suggestions.
- Offers a randomly generated strong password if the original is weak.

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI development
- **re** – Regular expressions for pattern matching
- **string** – Character sets for password generation
- **random** – Randomized selection of characters

---

## ✅ Password Strength Rules

1. At least 8 characters long  
2. Includes **at least one uppercase** letter  
3. Includes **at least one lowercase** letter  
4. Includes **at least one digit**  
5. Includes **at least one special character**

---

## 💡 Features

- Real-time password strength feedback (Weak, Moderate, Strong)
- Suggestions for improving weak passwords
- Random strong password generator
- Clean and user-friendly Tkinter interface

---

## 📋 Strength Classification

| Score | Classification |
|-------|----------------|
| 0-2   | Weak           |
| 3-4   | Moderate       |
| 5     | Strong         |

---

## 🖥️ GUI Layout

- Input field for password (characters hidden)
- "Check Strength" button
- Output:
  - Strength label (Weak/Moderate/Strong)
  - Improvement suggestions
  - Random strong password if needed

---

## 🔧 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
