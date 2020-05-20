'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    count = arr.count(0)
    for i in range(count):
        arr.remove(0)
        arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
