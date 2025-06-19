#  Add a feature that keeps track of the fewest attempts it took to guess the number correctly. The program should display this "best score" at the end of each game.

import random
a=input('enter the minimum limit ')
b=input('enter the maximum limit ')
if(a.isdigit() == False or b.isdigit() == False):
    print('Invalid input. Please enter numeric values.')  
    raise ValueError('Invalid input. Please enter numeric values.')

comp=random.randint(int(a),int(b))
sum=0
i=5
best_score = i  # Initialize best score with maximum attempts
while (sum<i):
    try:
        user=(input('enter your guess '))
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue
        # if(user.isdigit() == False):
        #     print('invalid input, please enter a number')
        #     continue
    if(comp==int(user)):
        print('correct guess')
        print(f'you have guessed it in {sum}th attempt')
        if sum < best_score:
            best_score = sum
        print(f'your best score is {best_score}')
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
   
             


