'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    placeHolder = []
    zero_counter = 0
    for i in range(len(arr)):           #loop through array
        if arr[i] != 0:                    
            placeHolder.append(arr[i])    # append to placeHolder if not zero
        else:                             
            zero_counter += 1             # do a zero counter if zero
        

    while zero_counter > 0:               # for every zero counter add a zero
        placeHolder.append(0)            # to placeholder
        zero_counter -= 1
    return placeHolder



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")