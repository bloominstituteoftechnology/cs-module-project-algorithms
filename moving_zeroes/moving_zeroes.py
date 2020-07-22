'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     for i in arr:
#         if i != 0:
#             old_index = arr.index(i)
#             new_index = 0
#             arr.insert(new_index, arr.pop(old_index))
            
#     return arr

def moving_zeroes(arr):
    length = len(arr)
    count = 0
    
    for i in range(length):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < length:
        arr[count] = 0
        count += 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")