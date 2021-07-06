'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in range(len(arr) -1):
        firstNum = arr[i]
        for j in range(i + 1, len(arr)):
            secondNum = arr[j]
            if firstNum > secondNum:
                return [firstNum, secondNum]
            else:
                return [secondNum, firstNum]
        
        return []




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")