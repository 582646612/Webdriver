import time
for i in range(1000, 200000):
    i=str(i)
    sum=0
    for j in range(0,int(len(i)/2)):
        if i[j]==i[-(j+1)]:
            sum+=1
        if sum==int(len(i)/2):
            print(i)
