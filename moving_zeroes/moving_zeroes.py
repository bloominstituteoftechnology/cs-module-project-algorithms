'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #walk through the array one by one
    # create a variable index to keep track where
    # we going to place the index when its not 0
    insert_index = 0
  
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_index] = arr[i]
            insert_index += 1
            
    for i in range(insert_index, len(arr)):
        arr[i] = 0
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")