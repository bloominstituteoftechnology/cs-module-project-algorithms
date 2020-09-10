"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""


# O(n) time, O(n) memory
def single_number(arr):
    # hash table
    ht = {}
    # for each item in the array
    for a in arr:
        # if its in the hash table, remove it from the hash table
        if a in ht:
            ht.pop(a)
        # otherwise, add it to the hash table
        else:
            ht[a] = 1
    # there should only be one item in the hash table at this point.
    return list(ht.keys())[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")