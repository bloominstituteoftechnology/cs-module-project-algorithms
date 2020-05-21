'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    only_one = False
    i = - 1
    while not only_one and i < len(arr):
        i += 1
        if i == 0:
            if arr[i] not in arr[i+1:len(arr)]:
                only_one = True
            # i += 1
        else:
            if arr[i] not in arr[:i] and arr[i] not in arr[i+1:len(arr)]:
                only_one = True

    return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")