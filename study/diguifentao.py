
# for i in range(20,10,-1):
#     print(i)

if __name__ == '__main__':
    for j in range(2000):
        n=j
        for i in range(5):
            n=(n/4)*5+1
        n=str(n)
        # print(n)
        # print(n[-1])
        if n[-1]==0:
            print(n)