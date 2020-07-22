'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    location = 0
    for x in arr:
        value = arr.pop(x)
        if value in arr:
            arr.insert(location, value)
            location += 1
        else:
            return value
             



        
            

        #if number doesn't exist:
            #return number


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")