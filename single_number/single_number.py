'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Set each value to keys of a dictionary, initialize count to 0
    counter = {value: 0 for value in arr}

    # Count occurrence of each value
    for value in arr:
        counter[value] += 1

    # Return value that only occurred once. Runs until there's a count of 1
    for value, count in counter.items():
        if count == 1:
            return value

    raise ValueError(f'No values in {arr} occurred only once')

    ''' Slower due to Python's sort() method
    arr.sort()
    idx = 0

    while  idx+1 < len(arr) and arr[idx] == arr[idx+1]:
        idx += 2

    return arr[idx]
    '''

    ''' Shouldn't modify arr while looping by arr
    duplicated = []
    for num in arr:
        arr.remove(num)
        if num not in arr and num not in duplicated:
            return num
        else:
            duplicated.append(num)

    return -1 # no unique number
    '''



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")