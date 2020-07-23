# def BinaryReversal(s):
#   b = bin(int(s))[2:]
#   print(b)
  
#   n= 8 
#   print(b.zfill(n))
  
#   while n < len(b):
#     n *= 2
#   return str(int((b.zfill(n))[::-1], 2))

  #txt.zfill(n) -> fill string with 0 until n characters long, 0s are added to the front of the text
  

# keep this function call here 
#print(BinaryReversal(213))

#reverse a string

def ReverseStr(s):
    #convert string to an array
    # arr = []
    # for x in range(len(s)):
    #     arr.append(s[x])
    arr = [x for x in s]
    #put string in a list
    #reverse = [0 for _ in range(len(s))]

    pointer1 = 0
    pointer2 = len(s) - 1
    while pointer2 >= pointer1:
        #swap values
        #reverse[pointer1], reverse[pointer2] = arr[pointer2], arr[pointer1]
        arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
        pointer1 +=1
        pointer2 -= 1
    #turn back into a string
    print(arr)
    return "".join(arr)    


name = 'Bobkels'

print(ReverseStr(name))

def reverseListRecursion(arr, n=0):
  last = len(arr) - 1
  
  if n == last:
    return 
  arr[n], arr[last] = arr[last], arr[n]
  n += 1
  last -= 1
  return reverseListRecursion(arr, n)

arr = [5,4,6,2,4]
print(reverseListRecursion(arr))
  
  