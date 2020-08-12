'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    num_dict = {}
    for num in arr:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for key, value in num_dict.items():
        if value == 1:
            return key



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")