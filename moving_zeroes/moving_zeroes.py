'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    i = 0
    end_idx = len(arr) - 1
    while i < len(arr):
        # print(i, end_idx, arr[i])
        if arr[i] == 0:
            if i >= end_idx:
                break
            arr.append(arr.pop(i))
            i -= 1
            end_idx -= 1
        i += 1
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")