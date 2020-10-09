'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    appearsOnceArray = []                                   # Array to hold all numbers we've only seen once
    for i in range(0, len(arr)):
        if arr[i] in appearsOnceArray:                      # Check if this number is a duplicate
            for x in range(0, len(appearsOnceArray)):       # It is a duplicate, remove it's match from appearsOnceArray
                if appearsOnceArray[x] == arr[i]:
                    appearsOnceArray.pop(x)
                    break                                   # We must break here because if we keep looping x will reach OOB since we .pop()'d
        else:                                               # This number is not a duplicate, add it to appearsOnceArray
            appearsOnceArray.append(arr[i])

    return appearsOnceArray[0]                              # The sole remaining member will be the single_number

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [9, 1, 4, 4, 5, 5, 3, 3, 0, 0, 1]

    print(f"The odd-number-out is {single_number(arr)}")
