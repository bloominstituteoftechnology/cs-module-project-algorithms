'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    max_num = max(arr)
    #print(max_num)
    #create an array of zero for each possible number + 1 for 0
    full_array = [0 for _ in range(max_num + 1)]
    #print('full_array 1', full_array)

    for x in range(len(arr)):
        #print(x)
        full_array[arr[x]] += 1


    #print(full_array)
    for x in range(len(full_array)):
        if full_array[x] == 1:
            return x


arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
single_number(arr)

if __name__ == '__main__':
    #Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")