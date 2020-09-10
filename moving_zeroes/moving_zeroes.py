'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Array of non-zero elements
    non_zero_arr = [i for i in arr if i is not 0]
    # Array of zero elements
    zero_arr = [i for i in arr if i is 0]
    # Combine the two arrays
    return non_zero_arr + zero_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")