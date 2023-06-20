k=int(input())
for i in range(1,k+1):
    if(i%2==0):
        print(i*i,end=",")
    else:
        print(i**3,end=",")