i=2
j=1
sum=0
for a in range(20):
    sum+=i/j
    b=i
    i=i+j
    j=b
print(sum)