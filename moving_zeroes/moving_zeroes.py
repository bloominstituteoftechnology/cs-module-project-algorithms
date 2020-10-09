'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #right and left pointers 
    i = 0
    j = 1
    
    while j<len(arr):
        # if both are both then only move right pointer 
        if (arr[i] == 0 and  arr[j] == 0):
            j +=1
        #if left pointer is 0, right is non zero swap them and move both forward. 
        elif (arr[i] == 0 and arr[j] !=0):
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
            i+=1
         #if left pointer is not 0, right is non zero or zero do nothing, move forward.
        elif (arr[i] != 0 and arr[j] ==0):
            j+=1
            i+=1
        else:
            j+=1
            i+=1
        
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")