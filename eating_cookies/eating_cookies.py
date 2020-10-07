'''
Input: an integer
Returns: an integer
'''
from itertools import permutations 
def eating_cookies(n):
    # cookies = n
    # three = []
    # two = []
    # if cookies == 0:
    #   return 1
    # if cookies == 1:
    #   return 1
    # if cookies == 2:
    #   return 2
    # while cookies != 0:
    #   if cookies >= 3:
    #     cookies = cookies -3
    #     three.append(3)
    #   elif cookies == 2:
    #     cookies = cookies -2
    #     three.append(2)
    #   else:
    #     cookies = cookies -1
    #     three.append(1)
    # cookies = n
    # while cookies != 0:
    #   if cookies >= 2:
    #     cookies = cookies -2
    #     two.append(2)
    #   else:
    #     cookies = cookies -1
    #     two.append(1)
    # three = len(set(permutations(three)))
    # two = len(set(permutations(two)))
    # one = 1
    # total = three + two + one
    # print(total)
    # print(set(permutations([3,3,3,1])))
    # return total
    cookies = n
    total = 0
    if cookies > 3:
      total += eating_cookies(n-3)
      total += eating_cookies(n-2)
      total += eating_cookies(n-1)
      return total
    elif cookies == 3:
      return 4
    elif cookies ==2:
      return 2
    else:
      return 1




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
