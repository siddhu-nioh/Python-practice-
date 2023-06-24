n=int(input())
s=str()
while(n!=0):
    if(n%2==0):
        s=s+"0"
        n=n//2
    if(n%2==1):
        s=s+"1"
        n=n//2
l=len(s)
x=4-l
for i in range(x):
    s=s+"0"
print(s[::-1])
    
