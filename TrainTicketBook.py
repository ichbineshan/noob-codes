class Train:
    def __init__(self,TrainName,TrainFare,SeatsAvailable):
        self.TrainName=TrainName
        self.TrainFare=TrainFare
        self.SeatsAvailable=set()
        for i in range(SeatsAvailable):
            self.SeatsAvailable.add(i+1)

    def book(self):
        print(f"To book in {self.TrainName}, press Y/N:")
        n=input()

        if n=="Y" and len(self.SeatsAvailable)>0:
            print(f"enter your name")
            PassengerName=input()
            print(f"enter your age")
            PassengerAge=input()
            print("+++++++++++++++++++++++++++++++++++++")
            print("your ticket has been booked succesfully!!!")
            print(f"name of the passenger is {PassengerName}")
            print(f"age of the passenger is {PassengerAge}")     
            print("++++++++++++++++++++++++++++++++++++++++++")
            self.SeatsAvailable.remove(len(self.SeatsAvailable))

        elif n=="N":
            print("booking failed!")
            exit()
        elif len(self.SeatsAvailable)==0:
            print("Sorry the seats are booked!")    
            
    def getstatus(self):
        print(f"*******************\nthe no. of available seats in {self.TrainName} are {len(self.SeatsAvailable)}\n***********************")
        print(self.SeatsAvailable)

    def Fareinfo(self):
        print(f"The fair for {self.TrainName} is {self.TrainFare}")

    def CancelTicket(self,seatNoToBeCancelled):
        print(f"Your Ticket {seatNoToBeCancelled} has been cancelled.......")
        self.SeatsAvailable.add(seatNoToBeCancelled)
        
            
js=Train("Jan Shatabdi","Rs.270",5)
gr=Train("Garib Rath","Rs.294",2)


y="y"
while y=='y' or y=="Y":
    u1=input("Jan Shatabdi or Garib Rath?? (type J/G) : ")
    if u1=="J":
        u2=input("Status(S)/Fare(F)/Booking(B)/Cancellation(C)?? ")
        if u2=="S":
            js.getstatus()
        elif u2=="F":
            js.Fareinfo()
        elif u2=="B":
            js.book()
        elif u2=="C":
            js.CancelTicket(input())
        else:
            print("wrong request!!")
            exit()    
    elif u1=="G":
        u2=input("Status(S)/Fare(F)/Booking(B)/Cancellation(C)?? ")
        if u2=="S":
            gr.getstatus()
        elif u2=="F":
            gr.Fareinfo()
        elif u2=="B":
            gr.book()
        elif u2=="C":
            gr.CancelTicket(input())
        else:
            print("wrong request!")
            exit()                

    y=input("Any furthur help? (Y/N): ")
    


#CAN WE ADD A self.passengerName with respect to trains and print names on demand?