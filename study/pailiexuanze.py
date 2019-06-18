
arr = ["a", "b", "c"]
arr1=['x','y','z']
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j and i!=k and j!=k and arr1[i]!='x' and arr1[k]!='x' and arr1[k]!='z' ):
                print(arr1[i],arr1[j],arr1[k])