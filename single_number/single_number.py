'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# from collections import Counter 

def single_number(arr):

    
    counts = {}
    for number in arr:
        if number in counts:
            counts[number]+= 1
        else:
            counts[number] = 1
    for key, value in counts.items():
        if value == 1:
            return key
    
"""
    # Your code here
    # Understand the problem:
    # An array of numbers where every each of one appears twice except of one that it appears only once.
    # Input = array =[3 2 5 2 5 3 1]
    # Output = 1
    
    not_duplicate_list = []
    nums = arr
    # for every number in numbers:
    for number in nums:# loop through numbers array
        if number in not_duplicate_list:# remove any duplicate number
             not_duplicate_list.remove(number)
        else:
            not_duplicate_list.append(number)# otherwise add the number to the list
    return not_duplicate_list.pop()
        """


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")