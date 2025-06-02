# password_checker.py
import re 

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r"\d", password): # \d matches any digit (0-9)
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r"[!@#$%^&*()_+={}\[\]:;<>,.?~\\-]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if score == 5:
        print("Password Strength: STRONG")
    elif score >= 3:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: WEAK")

    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)