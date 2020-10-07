'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # use count of total intergers to pull out the exclusive one
    n = set(arr)
    for item in n:
        count = arr.count(item)
        if count < 2:
        # can also use if count == 1:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")