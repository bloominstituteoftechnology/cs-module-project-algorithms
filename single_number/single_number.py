'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Firstpass: would be to make a hash table, iterate through the array
    # and count the values in the hash table, then traverse the hash table and
    # output the value with only 1.  This is O(n) and not single pass.
    # single pass requires the exclusive or (xor) operation. So it relies on 
    # the fact that duplicates fail and exclusiveor, so if you chain every 
    # number with an exclusiveor, only the single one will true out.

    #so I take value1 xor value2 xor value3 etc.  Best way to do this is with
    # a loop.

    xor_chain = arr[0]

    for i in range(1, len(arr)): #I already assigned the first element
        xor_chain = xor_chain ^ arr[i]

    return xor_chain


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")