'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    left, right = [], []
    i = 0
    while i < len(arr):
        if abs(arr[i]) != 0:
            left.append(arr[i])
        else:
            right.append(arr[i])
        i += 1
    
    arr = left
    arr.extend(right[:len(right)])
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")