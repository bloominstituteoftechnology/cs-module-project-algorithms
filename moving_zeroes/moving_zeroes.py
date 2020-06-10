'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    i = 0
    j = 1
    
    while j<len(arr):
        if (arr[i] == 0 and  arr[j] == 0):
            j +=1
        elif (arr[i] == 0 and arr[j] !=0):
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
            i+=1
        elif (arr[i] != 0 and arr[j] ==0):
            j+=1
            i+=1
        else:
            j+=1
            i+=1
        
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1] 

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")