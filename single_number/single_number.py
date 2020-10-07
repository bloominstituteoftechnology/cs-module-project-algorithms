'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    counter = 0
    for i in arr:
        for j in arr:
            if i == j:
                counter += 1
                
        if counter is not 2:
            return i
        else:
            counter = 0

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    
    # print(f"The odd-number-out is {single_number(arr)}")