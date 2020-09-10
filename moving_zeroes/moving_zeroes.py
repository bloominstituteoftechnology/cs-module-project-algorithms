'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    ''' FIRST PASS SOLUTION '''

    # # Array of non-zero elements
    # non_zero_arr = [i for i in arr if i is not 0]

    # # Array of zero elements
    # zero_arr = [i for i in arr if i is 0]

    # # Combine the two arrays
    # return non_zero_arr + zero_arr

    ''' WRITING BETTER SOLUTIONS '''
    # List to store solutions
    result = []

    # Loop through the array until index becomes greater than the length
    for i in arr:
        # If i is 0, move to the end of result list and continue to the next element in arr
        if i is 0:
            result.append(0)
            continue

        # If i is not 0, move to the front of result list
        result.insert(0, i)

    return result

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")