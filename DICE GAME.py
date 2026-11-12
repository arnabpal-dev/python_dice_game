import random

while 10>5:
    choice=input("input your choice(Y/N)").lower()
    if choice=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice=='n':
        print("Thanks for visiting")
        break
    else:
        print("invalid input")
