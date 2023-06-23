n=int(input())
N=n**2
k=0
while(N!=0):
    x=N%10
    k=k+x
    N=N//10
if(n==k):
    print("NEON NUMBER ")
else:
    print("NOT A NEON NUMBER")
    