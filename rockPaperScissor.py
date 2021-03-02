import random
u = input("enter rock, paper or scissor?? \n")

# if u!="rock"or u!="paper"or u!="scissor":
#     print("INVALID INPUT")
#     exit()

if u=="rock":
    pass
elif u=="paper":
    pass
elif u=="scissor":
    pass
else:
    print("INVALID INPUT")
    exit()

com=random.randint(1,3)

if com==1:
    com="rock"

elif com==2:
    com="paper"

elif com==3:
    com="scissor"

print("computer chose",com)

def rps(com,u):
    if com==u:
        r= "tie"
    elif com=="rock":
        if u=="paper":
            r= True
        elif u=="scissor":
            r= False
    elif com=="paper":
        if u=="scissor":
            r= True
        elif u=="rock":
            r= False 
    elif com=="scissor":
        if u=="rock":
            r= True
        elif u=="paper":
            r= False 
    return r        

c=rps(com,u)

if c==True:
    print("You Win :)")
elif c==False:
    print("Computer wins :(")
elif c=="tie":
    print("its a tie")