'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    setters_are_getters = set(arr)
    lister = list(setters_are_getters)

    for i, elem in enumerate(lister):
        if len(arr) == 1:
            break
        removed_element = lister[i]
        arr.remove(lister[i])
        arr.remove(removed_element)


    return arr[0]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 9,0, 0,32,32,55]

    print(f"The odd-number-out is {single_number(arr)}")