'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    set_1, set_2 = set(), set()

    for n in arr:
        if n not in set_1:
            set_1.add(n)
        else:
            set_2.add(n)

    return (set_1 - set_2).pop()



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")