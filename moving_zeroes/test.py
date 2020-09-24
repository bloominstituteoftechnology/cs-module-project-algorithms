def moving_zeroes(arr):
    zereos = []
    others = []
    # Your code here
    # for x in arr:
    #     print(arr[3:])
    # loop through all elements in the array
    for x in range(len(arr)):
        if arr[x] == 0:
            zereos.append(arr[x])
        else:
            others.append(arr[x])
            
    arr = others + zereos
    
    return arr

arr = [0, 3, 1, 0, -2]
moving_zeroes(arr)