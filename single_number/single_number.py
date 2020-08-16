'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    while len(arr) > 0:
        #select number and remove it from list
        number = arr.pop(0)
        
        #if number is not in the list, return single number 
        if number not in arr:
            return number
        
        #else remove it by the value
        else: 
            arr.remove(number)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd number is {single_number(arr)}")