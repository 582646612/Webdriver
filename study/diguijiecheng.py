def digui(x):
    if x==1:
        return 1

    else:
        return x*digui(x-1)
sum=0
for i in range(1,21):
    sum=sum+digui(i)
print(sum)

def age(n):

    if n==1:
        return 10
    else:
        c=age(n-1)+2
        return c
print(age(2))