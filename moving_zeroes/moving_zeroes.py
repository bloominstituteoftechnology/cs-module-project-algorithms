'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    num = 0
    while 0 in arr:
        index = arr.index(0)
        arr.pop(index)
        num += 1
    
    for i in range(num):
        arr.append(0)
        
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")