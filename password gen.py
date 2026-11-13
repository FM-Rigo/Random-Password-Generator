#library "random" for random password generation
import random

#letters, numbers and symbols to be used in the password
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols="!@#$%^&*();'"
numbers="0123456789"

#You can change the length of the password by changing the value of lenght and the characters by changing the variables lower, upper, symbols and numbers.
all=lower+upper+symbols+numbers
lenght=16

#.join makes junction of all the variables and sets the chosen lenght
password="".join(random.sample(all,lenght))
print("------------------------")
print("Password generated:")
print(password)
print("------------------------")

#Each password will be different because of the random.sample function.

#Fun fact: each password generated with more than 12 characters and full ASCII characters, takes roughly 100,000 to Trillions of years (or MORE) to crack with brute force... Or 1.5 years with a supercomputer.
