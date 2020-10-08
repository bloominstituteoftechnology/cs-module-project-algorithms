'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    '''
    list ->int
    Return odd-number-out element
    '''
    # # check every element appears once or not
    for i in range(0, len(arr)):
        j=i+1
        #keep comparing i th  element with the others element
        # until we find match
        count = ''
        while count !='found' and j < len(arr)-1:
             if arr[i] == arr[j]:
                 count = 'found'  
                 #pop the value from the array
                 arr.pop(j)
             else: 
                 j=j+1
        # Return the number if we did not find the match
        if count !='found':
             return arr[i]
'''
 Better soluntion with singlr loop but still O(n^2)
 count function has O(n) runtime
 Better solution  in reading perspective
 Is there datastructure that  would help us
 Dictionary  and setsis a good datastructure in finding the duplicate values
 Space Complexity - addition datastructure or varibale used in the program to store that
'''
    
def single_number(arr):
    '''
    list ->int
    Return odd-number-out element
    '''
    for x in arr:
        if arr.count(x) ==1:
            return x

def single_number(arr):
    '''
    list ->int
    Return odd-number-out element
    '''
    # as far as the space complexity concerned
    #worst case would be we have half of the element store
    #in the sets before we start removing it
    #initialize a sets-O(1)
    s = set() 
    #loop through every element in the list
    for i in arr: #O(n)
        if i in s: #O(1)
            s.remove(x) # O(1)
        else:
            s.add(x) # O(1)
    return list(s)[0] # O(1)


 
        

        
            
                       
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 5, 3,5, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")