'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # if it's not a zero, move it to index self.index - 1
    # or hold index of zero in a variable so that the number is moved to (index of zero) - 1
    # or move zeros to the right and ignore non zero numbers
    # if not zero, swap with last zero
    zero_idx_array = []

    for i in range(len(arr) - 1):
        if arr[i] == 0:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
    """
    for i in range(len(arr)):
        if arr[i] == 0:
            z = i
        if arr[i] != 0:
            arr.insert(z, arr[i])
            arr.pop(arr[i+1])
    
    # new implementation
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_idx_array.append(i)
    print(zero_idx_array)
    for z in zero_idx_array:
        arr.append(0)
        del arr[]
    # new implementation
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            arr.append(0)
            del arr[i]
            i = 0
        else:
            i += 1
               
    for i, z in enumerate(arr):
        print("i = ", i)
        if z == 0:
            arr.append(0)
            print("arr[i] = ", arr[i])
            del arr[i]
        
        print(arr)
    """
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    #arr = [0, 0, 0, 0, 3, 2, 1]
    #arr = [0, 0, 1, 0, -2]

    print(f"The result of moving_zeroes is: {moving_zeroes(arr)}")