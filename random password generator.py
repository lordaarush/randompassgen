#random password generator
import random
length = random.randint(7,20)
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","~"]
randset = [numbers,symbols,letters]
password=""
for i in range(length):
    a = random.choice(randset)
    password+= random.choice(a)
print(password)
