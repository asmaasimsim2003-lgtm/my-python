import random
print ("")
secret_number=random.randint(1,10)
guess=int(input("guess a number between 1 and 10:"))
while guess !=secret_number:
    if guess< secret_number:
        guess=int(input("Too low! guess again:"))
    else:
        guess=int(input("too high! guess again:"))
print ("congratulations!you guess the number!")

