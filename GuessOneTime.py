import random
num=random.randint(0,10)

ans=int(input("Give me a number from one to ten:"))
if num == ans:
    print("Congratulations! You guessed right!")
else:
    print("Please try again.")