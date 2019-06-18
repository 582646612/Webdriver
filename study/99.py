import time
a = [1, 2, 3,4,5,6,7]
b = a[:]
for i in range(1, 10):
    for j in range(1, i+1):
        print ("%d*%d=%d" % (i, j, i*j),end=' ')
    print()

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()