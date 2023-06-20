'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
l=int(input("length pf the wall: "))
b=int(input("BREADTH OF THE WALL:"))
l1=int(input("length of the first painting"))
b1=int(input("breadth of the first painting"))
l2=int(input("length of the second painting"))
b2=int(input("breadth of the second painting"))
A=l*b
a1=l1*b1
a2=l2*b2
if((a1+a2)<=A):
    if((l1+l2)<=l or (b1+b2)<=b):
        print("raj can fix the both paintings")
    else:
        print("rAJ CANNOT FIX THE BOTH PAIMTINGS PERFECTLY")
else:
    print("raj cannot fix paintings")