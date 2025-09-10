import random
import string 

print("WELCOME TO THE PASSWORD GENERATOR :")

total = int(input("Enter the total number of characters in the password :"))
letter = int(input("Enter the letters in the password :"))
numbers = int(input("Enter the numbers in the password :"))
symbols = int(input("Enter the symbols in the password :"))

if total == numbers + symbols + letter :
    password_chars = (
        random.choices(string.ascii_letters, k=letter) +
        random.choices(string.digits, k=numbers) +
        random.choices(string.punctuation, k=symbols)
    )
   
    random.shuffle(password_chars)
    password = "".join(password_chars)
    print(f"Generated Password : {password}")
else:
    print("Error: total must equal the sum of letters, numbers, and symbols!")