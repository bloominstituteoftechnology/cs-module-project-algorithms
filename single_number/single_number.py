'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Check every element if it appears once or not.
    #once the element with single occurence is found,
    #return it 

    #Better solution:
    
    #XOR of a number with itself is 0
    #XOR of a number with 0 is number itself
    #XOR operator is ^
    # res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4
    # XOR ->  res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)
    #         res = 7 ^ 0 ^ 0 ^ 0
    #         res = 7 ^ 0 = 7
    # XOR a number with itself is 0
    # Since i ^ i = 0 for any integer i, and i ^ 0 = i
    result = 0
    for i in arr:
        result ^= i
    return result



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")