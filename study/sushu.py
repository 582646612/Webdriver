from math import sqrt
for i in range(2,100):
    num=0
    for j in range(2,int(sqrt(i))+1):
        if(i%j==0):
            num+=1
    if num==0:
        print(i)
