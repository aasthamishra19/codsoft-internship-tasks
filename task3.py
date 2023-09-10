#password generator
import random

alphabet=["a","b","c"," d","e","f","g","h","i","j","k","l","m","n","o","p","q ","r","s","t","u","v","w","x","y","z",
          "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

number=["0","1","2","3","4","5","6","7","8","9"]

symbol=["!","@","#","$","%","^","&","*","(",")"]
print("Welcome to the Password Generator \n")
#print("\n")
used_alphabet=int(input("How many letters would you like to use : "))
used_symbol=int(input("How many symbol would you like to use : "))
used_number=int(input("How many number would you like to use : "))
password=" "


for char in range(1,used_alphabet+1):
  password=password+random.choice(alphabet)



for char in range(1,used_symbol+1):
  password=password+random.choice(symbol)


for char in range(1,used_number+1):
  password=password+random.choice(number)


print(f"The password generated is {password}")