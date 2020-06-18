'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    first = set()
    second = set()

    for num in arr:
        if num in first:
            second.remove(num)
        else:
            first.add(num)
            second.add(num)
    for num in second:
        return num


    # arr.sort()
    # count = 0
    # for num in arr:
    #     if num[0] == num[1]:
    #         arr.remove(num)
    #         count +=1

    # return arr

    # no_dups=[]
    # for num in arr:
    #     if num not in no_dups:
    #        no_dups.append(num)
    #     else:
    #         no_dups.remove(num)
    # return no_dups[0]

# def single_number_optimized(nums):
#     # keep track of number of times an item occurs in input
#     counts={}
#     #loop through input list 0(n), 
#     for nums in nums:
#         #check if item is in counts 
#         if num in counts:
#             #if it is increment the count,
#             nums+=1
#         else:
#             #if not set item count to 1
#             num = 1
        

#     for k,v in counts.item() #0(n)
#     if v == 1:
#         return k

# def single_number_optimizedd(nums):
#     # keep track of number of times an item occurs in nums

#     counts ={}
#     #loop thorugh input list 0(n)
#     for num in nums:
#         # if num in counts
#         if num in counts:
#             # remove item
#             del counts[num]
#         #other wise
#         else:
#             # add item
#             count[num] = 1

#     # return counts
#     for k,v in counts.item() #0(n)
#     if v == 1:
#         return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 0]

    print(f"The odd-number-out is {single_number(arr)}")