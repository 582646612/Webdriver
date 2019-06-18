def permutations(arr, start, end):
    if start == end:
        print(arr)

    else:
        for x in range(start, end):
            permutations(arr, start + 1, end)
            arr[x], arr[start] = arr[start], arr[x]



arr = ["a", "b", "c","d","e"]
permutations(arr, 0, len(arr))
