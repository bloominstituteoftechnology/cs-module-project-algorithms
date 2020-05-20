'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for i in range(len(arr)):
        twice_flag = False
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                twice_flag = True
        if not twice_flag:
            return arr[i]
    return -1

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")