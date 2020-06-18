'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # takes in an array
    # probably will loop over each number (for loop or while loop?)
    # could we sort the array for faster looping?
        # the array needs to have even number of elements to do comparison 
    # do we need to declare any varibles, maybe a counter or index?
    # may need to do some check of does this element == next element
        # if so, that element is a duplicate
        # else, this is the single number
    
    index = 0
    single_element = None
    length = len(arr)

    arr.sort()
  
    if length % 2 == 0: # even length of array (to compare a pair of numbers)
        while index < length:
            current_element = arr[index]
            next_element = arr[index + 1]
            if current_element == next_element:
                index = index + 2
            else:
                single_element = current_element 
                break # need to exit the loop if you found the number
        return single_element
    else: # odd length of array
        last_element = arr[-1] # declare a variable to hold the last element in the array
        while index < length-1: # loop through UNTIL the last element
            current_element = arr[index]
            next_element = arr[index + 1]
            if current_element == next_element:
                index = index + 2
            else:
                single_element = current_element 
                break # need to exit the loop if you found the number
        return single_element or last_element 


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

'''
What are arrays NOT good at? Are they the best option when we are searching for a particular value?
What is the runtime complexity of that search, in the worst case?
'''

# def single_number(nums): # one possible first-pass solution
#     no_dups = [] # create an array, to hold numbers we see in the nums array
#     for num in nums: # loop over nums array
#         if num not in no_dups: # check to see if the number is already in the no_dups array
#             no_dups.append(num) # if it's not, append it to the no_dups array
#         else: # otherwise
#             no_dups.remove(num) # remove it from the no_dups array
#     return no_dups[0] # when loop is done, the only number in our no_dups array is the odd number out

# def single_number_optimized(nums):
#     counts = {} # keep track of number of times an item occurs in input

#     for num in nums: # loop through input list
#         if num in counts: # check if item is in counts
#             del counts[num] # remove item
#         else: # otherwise
#             counts[num] = 1 # add item 

#     for k, v in counts.items(): # for key, value 
#         if v == 1:
#             return k


        


    

