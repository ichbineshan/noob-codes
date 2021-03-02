import random

randno=random.randint(1,100)
# print(randno)


def game():
    print("guess the number bw 1-100")
    k=int(input())
    i=0
    a=True
    while a: 
        i+=1
        if k>randno:
            print("lower number please \U0001F62A")  
        elif k<randno:
            print("higher number please \U0001F62A")
        elif k==randno:
            print("CORRECT GUESS!! \U0001F600")
            print("No of guesses to reach correct answer:",i)
            a=False
            break 
        k=int(input())
    return i                 

score=game()

with open("guessingbestscore.txt","r") as f:
    previousbest=int(f.read())

if score<previousbest:
    with open("guessingbestscore.txt","w") as f:
        f.write(str(score))

