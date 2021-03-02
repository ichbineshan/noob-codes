'''for vectors of unequal dimensions, these code still works, unlike the inheritance chapter practice set Q5'''

class Vector:
    def __init__(self,l):
        self.list=l

    def __add__(self,other):
        result=[]
        if len(self.list)==len(other.list):
            for i in range(len(self.list)):
                result.append(self.list[i]+other.list[i])
            return result
        elif len(self.list)>len(other.list):
            for i in range(len(other.list)):
                result.append(self.list[i]+other.list[i])
            for i in range(len(other.list),len(self.list)):    
                result.append(self.list[i]+0)
            return result
        elif len(self.list)<len(other.list):
            for i in range(len(self.list)):
                result.append(self.list[i]+other.list[i])
            for i in range(len(self.list),len(other.list)):    
                result.append(other.list[i]+0)
            return result                   

    def __mul__(self,other):
        dot=0
        for i in range(min(len(self.list),len(other.list))):
            dot=dot+self.list[i]*other.list[i]
        return dot    


v1=Vector([1,4,-1])
v2=Vector([2,3,5,6,7])

print(v1+v2)
print(v1*v2)

#_______________________________________________________________________________________________________
'''the code below returns the class object not the lists like above question,
then we define __str__ to print the list in the form of concatenated string equation'''

# class Vector:
#     def __init__(self,l):
#         self.list=l

#     def __add__(self,other):
#         result=[]
#         if len(self.list)==len(other.list):
#             for i in range(len(self.list)):
#                 result.append(self.list[i]+other.list[i])
#             return Vector(result)
#         elif len(self.list)>len(other.list):
#             for i in range(len(other.list)):
#                 result.append(self.list[i]+other.list[i])
#             for i in range(len(other.list),len(self.list)):    
#                 result.append(self.list[i]+0)
#             return Vector(result)
#         elif len(self.list)<len(other.list):
#             for i in range(len(self.list)):
#                 result.append(self.list[i]+other.list[i])
#             for i in range(len(self.list),len(other.list)):    
#                 result.append(other.list[i]+0)
#             return Vector(result)                   

#     def __mul__(self,other):
#         dot=0
#         for i in range(min(len(self.list),len(other.list))):
#             dot=dot+self.list[i]*other.list[i]
#         return "the dot product is : "+str(dot)   

#     def __str__(self):
#         st=''
#         index=0
#         for i in self.list:
#             if i<0:
#                 st=st+f"-{-i}a{index}"
#             elif i>=0:
#                 st=st+f"+{i}a{index}"    
#             index=index+1
#         return st      


# v1=Vector([-1,-4,-1])
# v2=Vector([2,-3,5,6])

# print(v1+v2)
# print(v1*v2)



            