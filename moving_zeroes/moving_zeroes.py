'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    originalArrCount = len(arr)
    arr[:] = filter(None, arr) #remove zeroes
    newArrCount = len(arr)
    arr.extend([0] * (originalArrCount - newArrCount)) #add zeroes based on the count descrepency
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")