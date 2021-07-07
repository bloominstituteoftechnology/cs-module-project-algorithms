'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# ***First Pass***
def single_number(arr):
    '''
    - function takes in an array
    - will loop over each number (for/while)
    - maybe sort for faster looping
        - array needs to have even number elements for comps
    - do a check for matching elements 
        - matching elements are duplicates
        - if not duplicate that's the single number
    '''
    index = 0
    single_element = None
    length = len(arr)

    arr.sort()
    if length % 2 == 0: # even length array to compare number pairs
        while index < length:
            current_element = arr[index]
            next_element = arr[index + 1]

            if current_element == next_element:
                index = index + 2

            else:
                single_element = current_element

                break # exits the loop if the number is found

        return single_element 

    else: # odd length array
        last_element = arr[-1] # declare variable to hold the last element in array

        while index < length - 1: # loop through until find last element
            current_element = arr[index]
            next_element = arr[index + 1]
..
            if current_element == next_element:
                index = index + 2

            else:
                single_element = current_element
                break # exit the loop if number is found

        return single_element or last_element


# def single_number(arr):
#     index = 0
#     single_element = None
#     length = len(arr)

#     arr.sort()

#     if length % 2 == 1:
#         length = len(arr) - 1
    
#     while index < length:
#         current_element = arr[index]
#         next_element = arr[index + 1]
#         last_element = arr[-1] 
        
#         if current_element == next_element:
#             index = index + 2
        
#         else:
#             single_number = current_element
#             break

#         return single_element or last_element



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")