'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    placeHolder = []
    for i in arr:                  # loop through given array
        if i in placeHolder:         # if the current number is already in placeholder
            placeHolder.remove(i)       # remove it from placeholder
        else:
            placeHolder.append(i)  # if the number does not exist add it to placeholder
    return placeHolder[0]               
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")