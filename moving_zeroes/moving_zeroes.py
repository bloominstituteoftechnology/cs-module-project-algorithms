'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zero_spot = len(arr)-1
    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(len(arr)-1, i, -1):
                if arr[j] != 0:
                    arr[j], arr[i] = arr[i], arr[j]
                    break
    return arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")