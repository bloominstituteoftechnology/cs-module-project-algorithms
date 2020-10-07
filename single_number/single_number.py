def single_number(arr):
    """
    Given a non-empty array of integers where every element appears twice except for one. Find that single number.
    Input: a List of integers where every int except one shows up twice
    Returns: an integer
    """
    # isn't there a way to take the item in the list then iterate over it until it finds it another pair?
    # iterate
    for i in arr:
        # if the number of values is 1 return the single value
        if arr.count(i) == 1:
            return i

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
