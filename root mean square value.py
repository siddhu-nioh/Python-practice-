'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
A=[10,12,10,8]
P=[12,14,8,6]
L=[]
for i in range(len(A)):
    x=A[i]-P[i]
    L.append(x*x)
s=sum(L)
e=s/len(A)
print(e**1/2)