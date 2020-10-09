'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# o(n^2)
# def single_number(arr):
#     boii = []

#     if arr == 0:
#         return 0

#     else: 
#         for num in range(len(arr)):
#             for other in range(num + 1, len(arr)):
#                 if boii.__contains__(arr[num]):
#                     break
                
#                 if arr[other] == arr[num]:
#                     boii.append(arr[other])
#                     break
#                 else: 
#                     if other + 1 == len(arr):
#                         print(arr[num])
#                         return arr[num]
                        
#                     else: 
#                         continue

# def single_number(arr):
#     for x in arr:
#         if arr.count(x) == 1: # 0(n) linear
#             return x
#         else:
#             continue

# as far as space complexity is concerned, worst case would
# if we have half of the lements in the set before we start removing them
# 0((1/2) * n) space complexity
s = set() #o(1)
def single_number(arr):
 for x in arr: #o(n)
     if x in s: #o(1)
         s.remove(x) #o(1)

     else: 
        s.add(x) #o(1)

 # at this point we should only have one element in our set
 return list(s)[0] #o(1)                    
                    

# Space complexity: 
# Any data structures that are passed into a function do not count towards space complexity
# Space complexity only cares about any additional data strucutres that are initialized
# during 


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")