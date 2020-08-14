'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    n_table = {}
    for n in arr:
        if n not in n_table:
            n_table[n] = 1
        else:
            n_table[n] += 1
    for n in n_table:
        if n_table[n] == 1:
            return n


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
