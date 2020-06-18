'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0
    newArr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
        else:
            newArr.append(arr[i])
    for i in range(count):
        newArr.append(0)
    return newArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0,0,0,0,0,0, 3,0, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


def moving_zeroes_opt(arr):
    # left pointer at the begining
    # right pointer at the end 

    #loop until left and right pointers meet or right pointer passes the left pointer
    # right pointer is less than left pointer
        #swapping:
        # left sees zero and right sees non-zero
            # swap the items
            # increment left
            # increment right
        # non-swapping:
            # if left sees none -zero
                #increment left
            # if right sees zero 
                # decrement right
