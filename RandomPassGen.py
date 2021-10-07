import random 
import pyperclip

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*"

number = input("how many passwords:")
numbers = int(number)

#set counter for number
ammount = 0

length = input("how long would you like the passwords:")
lengths = int(length)

while(numbers != ammount):
    password = ""
    for length in range(lengths):
        password += random.choice(chars)
    
    ammount +=1
    print(password)



pyperclip.copy(password)

