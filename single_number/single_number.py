# Single Number

#Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.  

## Examples

# Sample input: [2, 2, 1]
# Expected output: 1

# Sample iput: [4, 1, 2, 1, 2]
# Expected output: 4

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# function which takes in an input of an array of numbers
#create an empty  array to hold unique values 
# loop through the array
  #for i in array:
    #if i is not in unique_list:
    # add i to unique_list
    #else continue
  # for j in unique list if it is not found in arr return j

  #plan changed a bit
def single_number(arr):
    n = len(arr)
    for i in range(n):
        index = 0
        # loop through array
        while index < n:
            #if item is not == to index and item == arr[index] do nothing
            if(i != index and arr[i] == arr[index]):
                break
            index += 1 #increase index by 1 with ea iteration
        if(index == n):  #if is == n return the item
            return arr[i]
    return -1  #not found

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")