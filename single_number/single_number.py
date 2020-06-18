'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # start by seperating lists
    list1 = []
    list2 = []
    for n in arr:
        if n not in list1:
            list1.append(n)
        else:
            list2.append(n)

    for n in list1:
        if n not in list2:
            return n
    return -1

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")