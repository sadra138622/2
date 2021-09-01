n=0
n= int(input())
for a in range (2, n+1):
    i=1
    b=0
    while (i<=a):
        if (a%i==0):
            b=b+1
        i=i+1
    if (b==2):
        print(a)

