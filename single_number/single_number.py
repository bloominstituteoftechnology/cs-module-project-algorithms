'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    # set creates a new array for us, containing all contents, with duplicates trimmed
    set_arr = list(set(arr))
    print(set_arr)

    #loop through each index of our trimmed set
    for i in range(len(set_arr)):


        #store element to be removed before removing
        removed_element = set_arr[i] #Current index inside of set_arr
        #remove value from main array
        arr.remove(set_arr[i])


        #if there's another one of 'em after removing, remove that one too and carry on
        if removed_element in arr:
            arr.remove(removed_element)

            #None left? You've found the odd one out.
        else:
            return removed_element
        



    return arr[0]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3,897, 9, 9,0, 0,32,32,55, 55]

    print(f"The odd-number-out is {single_number(arr)}")