'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):
    #This applies a sorting key ONLY to 0s, to make them appear at the end of the list every time.
    #It leaves all other values in place.
    return sorted(arr, key=lambda x: x in [1000000,0])


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")