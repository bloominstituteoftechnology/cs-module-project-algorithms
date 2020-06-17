'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(array):
    # Your code here
    # loop thru array contents
    # count frequencies of unique entries
    # return single number
    #pass

    #single_number_index = 0
    
    result = array[0]

    for i in range(1, len(array)):
        result = result ^ array[i]
    
    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")