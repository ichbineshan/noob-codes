'''APPROACH1 -------> methods using simple f strings'''



class Complex:
    def __init__(self,a,b):
        self.alpha=a
        self.beta=b
        print(f"complex number initialising...3..2..1..GOOOO!! \nthe real part is {self.alpha}\nthe imaginary part is {self.beta}\n")

    def __add__(self,other):
        print("gonna add!")
        return f"{self.alpha+other.alpha} + {self.beta+other.beta}i"

    def __mul__(self,other):
        print("gonna multiply!")
        return f"{self.alpha*other.alpha-self.beta*other.beta} + {self.alpha*other.beta+self.beta+other.alpha}i"

c1=Complex(8,-5)
c2=Complex(1,-4)

print(c1+c2)
print(c1*c2)

#_______________________________________________________________________________________________________________________

'''APPROACH2 ---------->  class method __add__ and __mul__ return the complexno. as 
    the same class's object  
    and then we use __str__ to get a readable output
    
    this is helpful since now we only need to put condition once in __str__ instead of 
    all the functions individually to check if output isn't printed as 3+ -5i
    '''

# class Complex:
#     def __init__(self,a,b):
#         self.alpha=a
#         self.beta=b

#     def __add__(self,other):
#         return Complex(self.alpha+other.alpha, self.beta+other.beta)
#         # here we are storing the return values as the class Complex object itself 

#     def __mul__(self,other):
#         return Complex(self.alpha*other.alpha-self.beta*other.beta,self.alpha*other.beta+self.beta+other.alpha)
#         # here we are storing the return values as the class Complex object itself 


#     def __str__(self):
#         if self.beta<0:
#           return f"{self.alpha}-{-self.beta}i"
#         return f"{self.alpha}+{self.beta}i"   
#         # here we are overloading print statement to print the Complex values returned above as strings 


# c1=Complex(8,-5)
# c2=Complex(1,-4)

# print(c1+c2)
# print(c1*c2)