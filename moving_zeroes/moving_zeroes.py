'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in range(len(arr)):
        x = arr[i]

        if x != 0:
            print('[x]:',[x])
            print('arr[:i]', arr[:i])
            print('arr[i+1:]', arr[i+1:])
            # replaces the non-zero value in the front of the array
            arr = [x] + arr[:i] + arr[i+1:]
            print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")