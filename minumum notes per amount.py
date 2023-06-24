n=int(input())
l=[500,200,100,50]
s=0 
for i in l:
    while(n>=i):
        s=s+1 
        n=n-i
print(s)