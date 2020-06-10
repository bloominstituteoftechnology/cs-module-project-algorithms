# goal: code a factorial function

# Understand
## Google! What is a factorial?
## What is our goal?
## Get a visual representation

## n!
## n * (n - 1)...1

# Plan
## recursively or iteratively?
## what language is best to use here?

## recursive

## Define the base case
### return if we are at n = 1
## Move toward the base case
## Call itself
## call with each number, then -1 and multiply it to previous until we hit the base case

# execute
def factorial(n):
	### return if we are at n = 1
	if n == 1:
		return 1
	## Move toward the base case
	## Call itself
	## call with each number, then -1 and multiply it to previous until we hit the base case
	return n * factorial(n - 1)

print(factorial(3) == 6)
print(factorial(4) == 24)

## Review
### Time complexity?
### Space complexity?

## Iterative solution
## Plan
### Go from 1 to n, or n to 1

### make a tracker: total
### make a while loop, and decrement n as we go
### multiply our tracker at every step
### return tracker

# execute
def iter_factorial(n):
	### make a tracker: total
	total = 1

	### make a while loop, and decrement n as we go
	while n != 1:
		### multiply our tracker at every step
		total *= n
		n -= 1
	### return tracker
	return total

print(iter_factorial(3) == 6)
print(iter_factorial(4) == 24)

## Review
### Iterative vs recursive?
### Space complexity: iterative
### Time complexity: 0(n) for both
### Readability: subjective
