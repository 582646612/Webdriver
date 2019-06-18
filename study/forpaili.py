for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            for m in range(1,5):
             if (i != k and i!= j and i!= m and j!=k and j!=m and k !=m):
                print(i, j, k,m)