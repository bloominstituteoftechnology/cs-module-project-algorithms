'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zero_count = arr.count(0)
    curr_count =0
    
    while curr_count<zero_count:
        arr.pop(arr.index(0))
        arr.append(0)
        
        curr_count+=1
    return arr
 
# def moving_zeroes(arr):
#     # Your code here
#     new_arr = []
#     zarr=[]
#     for i in arr:
#         s = str(i)
#         s.split(',')
         
#         new_arr.append(s)
#         for i in new_arr:
#             if '0' in i:
#                zarr.append(i)
#                new_arr.remove(i)
#                arr = new_arr+zarr
#         for i in arr:
#             int(i)       
#     return arr


# stuff = [10,3,4,5,20]
# print("THIS",moving_zeroes(stuff)) 


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")