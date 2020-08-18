import random
num=random.randint(1,20)
i=0
while i<5:
    ans=int(input("Please give me a number from 1-20:"))
    if ans == num:
        print("Congratulations! You guessed correctly!")
        print("You did it in",i,"guesses.")
        break
    elif ans > num:
        print("Sorry your number is too high. Please try again.")
    elif ans < num:
        print("Sorry,the number that you guessed is too low. Please try again.")        
    else:
        print("Please try again.")
    i=i+1
   