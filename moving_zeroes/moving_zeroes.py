'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    end = len(arr) - 1
    for i in range(len(arr)):
        if i >= end:
            return arr
        
        if arr[i] is 0:
            while (arr[end] is 0) and (end > i):
                end -= 1
            
            if i == end:
                return arr
            else:
                arr[i], arr[end] = arr[end], arr[i]
                end -= 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")