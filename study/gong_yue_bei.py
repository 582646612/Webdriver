def gongyue(x,y):
    if x>y:
        temp=y
    else:
        temp=x
    for i in range(1,temp+1):
        if x%i==0 and y%i==0:
            end=i
    return end

def gongbei(x,y):
    end=0
    if x>y:
        temp=x
    else:
        temp=y
    while(end==0):
        if temp%x==0 and temp%y==0:
            end=temp
        temp+=1
    return end
x=gongbei(12,18)
print(x)