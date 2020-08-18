'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #empty list non_zero
    non_zero = []
    #empty list for zero
    zero = []

    for num in arr:
        # numbers not equal to zero append to non_zero
        if num != 0:
            non_zero.append(num)
        # everthing else aka 0, append to the 0 list    
        else:
            zero.append(num)

    # returns the two lists
    return non_zero + zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

