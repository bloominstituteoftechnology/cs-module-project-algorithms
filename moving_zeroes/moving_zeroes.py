'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for i in arr:
        if i == 0:
            arr.append(arr.pop(arr.index(0)))
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 1, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")