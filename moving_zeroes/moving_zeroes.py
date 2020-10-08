'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    if not arr:
        return

    for i in arr:
        if i == 0:
            pop_val = arr.pop(arr.index(i))
            print(pop_val)
            arr.append(pop_val)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
