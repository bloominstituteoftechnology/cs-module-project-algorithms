'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here
#     for i in range(0, len(arr)):
#         j=i+1
#         if arr[i] == 0:
#             while  j < len(arr):
#                 if arr[j] != 0:
#                     arr[i], arr[j] = arr[j], arr[i]
#                     break
#                 else:
#                     j = j + 1
#     return arr

def moving_zeroes(arr):
    pass

                




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")