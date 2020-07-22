'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # assign empty array to single_ladies
    single_ladies = []
    # iterate through array
    for i in range(0, len(arr)):
    # if value at index i is in new list
        if arr[i] in single_ladies:
            # remove i from new list
            single_ladies.remove(arr[i])
        # else
        else:
            # append number to new list
            single_ladies.append(arr[i])
        # return first index of new list
    return single_ladies[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    

    print(f"The odd-number-out is {single_number(arr)}")