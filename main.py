
#  Add a feature that keeps track of the fewest attempts it took to guess the number correctly. The program should display this "best score" at the end of each game.


import random
a=int(input('enter the minimum limit '))
b=int(input('enter the maximum limit '))
comp=random.randint(a,b)
sum=0
i=5
while (sum<i):
    user=(input('enter your guess '))
    if(user.isdigit() == False):
        print('invalid input, please enter a number')
        continue
    elif(comp==int(user)):
        print('correct guess')
        print(f'you have guessed it in {sum}th attempt')
        break
    elif(sum==i-1):
        print(f'you have exhausted your attempts, the correct number was {comp}')
        break
    elif(int(user)<comp):
        print('try higher value')
    elif(int(user)>comp):
        print('try lesser value')
    # else:
    #     ('invalid input')  
    sum=sum+1  