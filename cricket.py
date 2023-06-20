'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
tb=int(input())
tr=int(input())
r=int(input())
l=int(input())
a=tb//6
x=tb-(a*6)
y=a+(0.1)*x
print((y))
print(tr/y)
c=l//6
d=l-(c*6)
w=c+(0.1)*d 
z=(r/w)
print("%.1f" %z)
print(w)
if(tr/y <z):
    print("eligible to win")
else:
    print("not eligible avadhu")