'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
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