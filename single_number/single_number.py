'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # the idea for the first-pass soltuion
    # we'll keep an array, call it 'no_dups' to hold numbers we see int eh nums array
    # iterate through nums
        # check to see if the number is already in the 'no_dups' array
        # if it is, remove it from the 'no_dups' array
    # when we're done iterating, the only number in our 'no_dups' array is the odd number out
    # we'lll return it.

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")