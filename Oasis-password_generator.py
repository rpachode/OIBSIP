import random
import string

password_length = int(input("Enter the lenght for password: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(password_length):
    password += random.choice(characters)

print("\nGenerated Password:", password)