'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     s = set() #array that accepts unique values
#     # use either a dictionary or a set 
#     # sets: holding onto unique elements 
#     # loop through our arr
#     for x in arr:
#         # for each element
#         # check if it is already in our set
#         # if it is, then that's not our out-element-out 
#         if x in s:
#             # remove the element from our set 
#             s.remove(x)
#         else:
#             s.add(x)
#     # the odd-element-out will be the only element in the set 
#     return list(s)[0]​

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
# ​
def single_number(arr):
    s = [] #holds single number that doesnt have a copy of itself
    for x in arr: #we are looping through original array of ints to find a single one
        if x not in s: 
            s.append(x) #if element is not found in single array we will add it to singles array
        else:
            s.remove(x) #else we will remove it if its already found in singles array we remove duplicate
    return s[0] #this is single number remaining that is first item in singles array

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")