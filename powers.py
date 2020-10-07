# given a and b, return a ** b, without using the inbuilt operator

# understand
## one way: a single number being multiplied by itself
## Valid and invalid inputs
### invalid: letters
### valid: any number whatsoever
### maybe no negative numbers for b? 2 ** -2 = 1/4
#### 1/( 2 ** 2 )

### Square root with a power: raise to 1/2, 0.5
### i = sqrt(-1) == (-1)**0.5

## Anything to the power of 0 = 1
### Let's not handle decimal numbers for b

## Plan
### We have two numbers, one or both may be negative

### Iterative or recursive?

### 2^3
### a = 2, b = 3
### Iterative pseudocode
#### Check if b == 0, if so return 1
#### Have a total = 0
#### While loop: while b isn't 1
##### multiply a by itself
##### decrement b to approach 1
#### return total

def iter_power_v1(a, b):
	if b == 0:
		return 1
	total = a
	while b != 1:
		total *= a
		b -= 1
	return total

# print(iter_power_v1(2, 3) == (2 ** 3))
# print(iter_power_v1(10, 2) == (10 ** 2))
# print(iter_power_v1(5, 7) == (5 ** 7))
# print(iter_power_v1(10, 0) == (10 ** 0))
# print(iter_power_v1(2, 1) == 2)
# print(iter_power_v1(100, 1) == 100)

## Review
### Handled values for a and b successfully
### And values of 0 for b!
### But not negative

## negative values for b
## decimal value for b

### Iterative pseudocode
#### Check if b is integer, otherwise return error message
#### Check if b == 0, if so return 1
#### check if b < 0: if so, multiply by -1 and set invert to true

#### Have a total == a
#### While loop: while b isn't 1
##### multiply a by itself
##### decrement b to approach 1
#### return total

def iter_power_v2(a, b):
	invert = False
	if type(b) is not int:
		return "Sorry, we don't handle decimals."
	if b == 0:
		return 1
	if b < 0:
		b *= -1
		invert = True
	total = a
	while b != 1:
		total *= a
		b -= 1

	if invert:
		return 1 / total
	else:
		return total

print(iter_power_v2(2, 3) == (2 ** 3))
print(iter_power_v2(10, 2) == (10 ** 2))
print(iter_power_v2(5, 7) == (5 ** 7))
print(iter_power_v2(10, 0) == (10 ** 0))
print(iter_power_v2(2, -2) == (2 ** -2))
print(iter_power_v2(2, 1) == 2)
print(iter_power_v2(100, 1) == 100)
