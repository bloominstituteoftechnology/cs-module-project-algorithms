'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new_arr = [] #initial values 
    count = 0
    for i in range(len(arr)): # for loop to iterate
        # print(i, arr[i])
        if arr[i] != 0: # if it's not a zero
            # print(arr[i])
            new_arr.append(arr[i]) # append to new array
        else:
            count += 1 # go to next next number
    for i in range(count): # iterate through the counting array
        new_arr.append(0) # append the zeros you find in there to the new array
    print(new_arr) # print out the new array 
    arr = new_arr # set new array to new array
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")