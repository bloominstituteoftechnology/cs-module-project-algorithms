'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

"""
Plan
    Loop through the array
    Check for zeros
    use list.remove and list.append
    return index of 0 in array
"""
"""
Pseudocode
    Loop through the array
    If item in array is equal to zero
        - remove the item from the array
        - add the item to the end of the list    
    return index of the first occurence of 0
"""