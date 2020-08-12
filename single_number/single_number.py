'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # Understand:
    # A list of ints where every element is duplicated except one
    # Return that one non-duplicated value
    # Assume there's always only one number that isn't duplicated

    # Plan:
    # Cycle through the list
    #   call the count() list method to determine if there are 1 or 2 copies
    #   if one, return that value. otherwise, keep going.

    # Execute:

    for val in arr:
        if arr.count(val) == 1:
            return val


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
