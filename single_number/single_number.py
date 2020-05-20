'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    buckets = {}
    for x in arr: 
        if buckets.get(x) is None:
            buckets[x] = 1
        else:
            buckets[x]+= 1

    for i in buckets:
        if buckets[i] == 1:
            return i 
        
        


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")