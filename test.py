# Write a function that takes a year and returns its corresponding century.
# Examples

# century_from_year(2005) ➞ 21
# century_from_year(1950) ➞ 20
# century_from_year(1900) ➞ 19

# def century(year):
#     return (century) // 100 + 1

# print(century(2005))

# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
# Examples

# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

# def length(num, length):
#     a = []
#     for i in range(1,length+1): 
#         a.append(i*num)
#     return a

# print(length(7,5))
# print(length(12,10))
# print(length(17,6))

# Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
# Examples

# majority_vote(["A", "A", "B"]) ➞ "A"
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

# def findMajority(arr, n): 
#     maxCount = 0; 
#     index = -A # sentinels 
#     for i in range(n): 
      
#         count = 0
#         for j in range(n): 
          
#             if(arr[i] == arr[j]): 
#                 count += 
          
#         # update maxCount if count of  
#         # current element is greater 
#         if(count > maxCount): 
          
#             maxCount = count 
#             index = i 
        
#         if (maxCount > n//2): 
#             print(arr[index]) 
#     else: 
#         print("No Majority Element") 
  
# # Driver code 
# if __name__ == "__main__": 
#     arr = [1, 1, 2, 1, 3, 5, 1] 
#     n = len(arr) 

#     # Function calling  
#     findMajority(arr, n) 