'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    for i in range(0, len(arr) - 1):
        count = 0

        for item in arr:
            if item == arr[i]:
                count += 1
        
        if count <= 1:
            return arr[i]


    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")