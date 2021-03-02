#WITH CONSTRUCTOR
class CalculateIt:

    def __init__(self,n):
        self.num=n
        
        
    def sq(self):
        print(self.num**2)

    def cube(self):
        print(self.num**3)

    def squarert(self):
        print(self.num**0.5)

forYourNum=CalculateIt(9)

forYourNum.sq()
forYourNum.cube()
forYourNum.squarert()


#--------------------------------------------------
#CALCULATIONS WITHIN CONSTRUCTOR
# class CalculateIt:

#     def __init__(self,n):
#         self.num=n
#         self.sqr=n*n
#         self.cube=self.sqr*n
#         self.squarert=n**0.5

#     def squarer(self):
#         return self.sqr

#     def cuber(self):
#         return self.cube

#     def squarerooter(self):
#         return self.squarert

# forNine=CalculateIt(9)

# print(forNine.num)
# print(forNine.squarer())
# print(forNine.cuber())
# print(forNine.squarerooter())
# print(forNine.sqr)

#_______________________________________________________________________

#WITHOUT CONSTRUCTOR

# import math
# class CalculateIt:
    
#     def sq(self,n):
#         return n*n

#     def cube(self,n):
#         return self.sq(n)*n

#     def squarert(self,n):
#         return math.sqrt(n)

# forYourNum=CalculateIt()
# num=int(input())

# print(forYourNum.sq(num))
# print(forYourNum.cube(num))
# print(forYourNum.squarert(num))

