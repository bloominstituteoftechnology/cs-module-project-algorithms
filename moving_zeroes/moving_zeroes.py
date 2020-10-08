'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    #pass

    # Count zeros in list
    # Drop zeros in place
    # append zeros to end (using previous count)
    # return array

    # zero_counter = arr.count(0)
    # arr[:] = (value for value in arr if value != 0)
    # arr.extend([0 for i in range(zero_counter)])
    # return arr
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")