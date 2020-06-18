'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# First Pass Solution

# def single_number(arr):
#     # Your code here
#     unique = set()
#     double_total = 0
#     single_total = 0
#     for item in arr:
#         double_total += item
#         if unique.__contains__(item):
#             continue
#         else:
#             unique.add(item)
#             single_total += item
#     return (single_total * 2) - double_total

# From Lecture Optimized Solution

def single_number(arr):
    # Your code here
    a_dict = dict()
    count = 1
    for item in arr:
        if a_dict.__contains__(item):
            a_dict.__delitem__(item)
        else:
            a_dict[item] = "Unique"
    return list(a_dict.keys())[0]

foo = [2, 2, -1, -1, -12]
x = single_number(foo)
print(x)
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")