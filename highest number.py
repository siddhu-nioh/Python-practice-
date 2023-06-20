n=[1,27,2322,64232,929]
c=0
for i in range(len(n)):
    for j in range(len(n)):
        if(n[i]>n[j]):
            c=c+1 
            if(c==len(n)-1):
                print(n[i])
    c=0            
                