#recursive function
#given number n, sums all non- negative numbers up to n.

#1. Base case - simplist possible input. We provide and explicit answer on base case
#2. Play around with examples
#3. Relate larger examples with smaller ones
#4. Generalize a pattern
#5. Write code combine recursive pattern with base case
def sumNum(n):
    print(n)
    sum = 0
    if n < 0:
        return 
    elif n == 0:
        return 0
    else:
        sum += n
        print('sum',sum)
    # if I know the answer to a previous case, could I solve the next case.
    # small ex. n = 2 + n-1 = 3
    return n + sumNum(n-1)

print(sumNum(2))

#f() take n and m 
#output number of unique paths from top of left corner to bottom
#right corner of a n X m grid
#can only move down or right 1 unit at a time.

def grid(n, m):
    #base case
    if n == 1 or m == 1:
        return 1
    else:
        return grid(n, m-1) + grid(n-1, m)



#examples
#n = 1  m = 1  = 1path
#n = 1 amd m = 2  = 1path

# n, m = n, m-1 + n-1, m


#write a f() that counts the number of ways you can partition n objects
#using parts up to m(assuming m >= 0)

def part(n, m):
    #base
    if n == 0:
        return 1
    if m == 0:
        return 0
    