a=[4,2,5,23,66,2,45,23,65,11]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            print(a)
b=[]
for i in range(len(a)):
    b[i]=a[i]