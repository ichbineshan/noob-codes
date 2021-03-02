from statistics import median

n=int(input())
a=list(map(int,input().split()))
a.sort()
q2=median(a)
if n%2==0:
    a1=a[0:int(n/2)]
    a2=a[int(n/2):n]

    q1=median(a1)
    q3=median(a2)

elif n%2!=0:
    a.remove(q2)
    n=n-1
    a1=a[0:int(n/2)]
    a2=a[int(n/2):n]

    q1=median(a1)
    q3=median(a2)

print(q1)
print(q2)
print(q3)

