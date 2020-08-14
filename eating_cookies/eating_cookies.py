'''
Input: an integer
Returns: an integer
'''

# first-pass solutions

def eating_cookies_three(n):
  total = 0
  if n == 0:
    return 1
  elif n < 0:
    return 0
  else:
    total += eating_cookies_three(n-1) + eating_cookies_three(n-2) + eating_cookies_three(n-3)
  return total

print(eating_cookies_three(5))

def debug_eating_cookies(n, arr, j):
    # Your code here
    total = 0
    if n == 0:
        print(arr)
        return 1
    for i in range(1, n+1):
        arr[j] = i
        total += debug_eating_cookies(n - i,arr, j + 1)
        arr[j] = 0
    return total

k = 3

arr = [0] * k 
# print(debug_eating_cookies(k, arr, 0))

# def eating_cookies(n):
#     total = 0
#     if n == 0:
#         return 1
#     for i in range(0, n+1):
#         total += eating_cookies(n-1)
#     return total

def eating_cookies(n):
  memo = [0 for _ in range(0,n+1)]
  def eat(n, memo):
    total = 0
    if n == 0:
      return 1
    for i in range(1, n+1):
      if i - memo[n] == 0:
        total += 1
      else: total += eat(n - i, memo)
      memo[i] = i
    return total
  return eat(n, memo)

# print(eating_cookies(4))

        
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
