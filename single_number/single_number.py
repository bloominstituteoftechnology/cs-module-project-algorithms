'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

sample_arr = [1, 1, 2, 2, 5, 5, 10, 10, 20, 20, 15]

def single_number(arr):
    result = 0
    for n in arr:
        result ^= n
    return result

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    my_array = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(sample_arr)}")