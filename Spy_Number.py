n=int(input())
s=0
m=1
while(n!=0):
    k=n%10
    s=s+k
    m=m*k
    n=n//10
if(s==m):
    print("Spy Number")
else:
    print("Not Spy Number")