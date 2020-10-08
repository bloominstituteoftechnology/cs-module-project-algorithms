'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    """
    list ->list
    Return list of shifted non_zero element to the left
    """
    j = 0
    for i in range(1, len(arr)):
        if arr[i] !=0:  
            # swap the value with zero element of the list   
            arr[j], arr[i] =arr[i], arr[j]
            #move to the next zero element of the list
            j = j+1
   
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    #arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")