'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     # Your code here
#    # [2,2,4,4,]
        
#     j = 1
#     i = 0
#     while i < len(arr)-1:
#         count = 0
#         for j in range(0,len(arr)):
#             if arr[i] == arr[j]:
#                 count +=1
     
#         if count > 1:
#             i = i+1
#         else:
#             return arr[i]
def single_number(arr):
    # Your code here
   # [2,2,4,4,]
    count = {}
  
    for value in arr:
        if value in count:
             
            count[value]+=1
             
        else:

            count[value]=1
    
    for i in count:
        if count[i] == 1:
            return i
       

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")