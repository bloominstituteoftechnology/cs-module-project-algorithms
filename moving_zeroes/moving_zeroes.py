'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0

    for index in range(len(arr)):
        if arr[index] != 0:
            arr[count] = arr[index]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
