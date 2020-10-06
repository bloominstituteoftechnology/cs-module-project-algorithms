'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Make an empty list to keep of all values, where the length of the list is == to the value of the largest number

    instance_list = [0] * (max(arr) + 1)
    print(instance_list)

    #loop through arr, increase the value at the instance_list index that corresponds to the value in arr

    for value in arr:
        instance_list[value] += 1
    print(instance_list)

    #loop through the instance_list and return the index where instance_list[i] == 1

    for i in range(len(instance_list)):
        if instance_list[i] == 1:
            return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")