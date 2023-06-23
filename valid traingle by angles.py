x=int(input())
y=int(input())
z=int(input())
s=x+y+z
if(x==0 or y==0 or z==0 & s<180 & s>180):
    print("it is not a valid triangle")
elif(s==180):
    print("it is a valid traingle")
else:
    print("it is not a valid trainglr")