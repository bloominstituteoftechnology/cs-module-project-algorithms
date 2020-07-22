'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    length = (len(arr))
    for x in range(length):
        if arr[x] == 0:
            arr.remove(arr[x])
            arr.insert((len(arr)), 0)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")