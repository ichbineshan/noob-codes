# Enter your code here. Read input from STDIN. Print output to STDOUT
narr=int(input())
arr=list(map(int,input().split()))
arr.sort()

def mean():
    return sum(arr)/narr

def median():
    if narr%2==0:
        return (arr[int((narr/2)-1)]+arr[int((narr/2))])/2
    elif narr%2!=0:
        return arr[int((narr-1)/2)] #to return (n+1)/2 th term we need to subtract 1 before putting in index
       
    
def mode():
    L=[]
    for i in arr:
        a=arr.count(i)
        L.append(a)

    for j in arr:
        if arr.count(j)==max(L):
            return j    
        
    

print(mean())
print(median())    
print(mode())    

a=input("press enter to quit")    