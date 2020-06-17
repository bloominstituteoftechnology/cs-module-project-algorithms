'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    arr.sort()
    arr.reverse()

    length = len(arr)
    if 0 not in arr:
        return arr
    while arr[length - 1] is not 0:
        item = arr.pop()
        arr.insert(0, item)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")