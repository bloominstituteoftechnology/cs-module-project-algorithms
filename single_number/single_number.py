'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Need to loop through the code through each element
    for i in range(0, len(arr) - 1):
        cur = id

        for j in range(i+1, len(arr)):
            if arr[j] == cur:
                return j
        else:
            return None

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")