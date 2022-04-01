    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
     str = input.upper()
     if str[-2:] == 'PY':
          return True
     else:
         return False

print(endsPy('ilovepy'))
print(endsPy('welovepy'))
print(endsPy('welovepyforreal'))
print(endsPy('pyiscool'))

    
# <QUESTION 2>

# Given a list of items, return a dictionary mapping items to the amount
# of times they appear in the list

# Note: the order of this dictionary does not matter

# <EXAMPLES>

# one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) → {'apple':3, 'orange':2, 'banana':1}
# one(['tic', 'tac', 'toe']) → {'tic':1, 'tac':1, 'toe':1}

list = ['apple', 'banana', 'orange', 'orange', 'apple', 'apple']

def one(items):
 if type(items) is list:
    items_set = set(items)
    items_dict = dict()
    for i in items_set: 
     item_dict[i] = items.count(i)
    return item_dict
 else: 
        return "Please enter a list"

print(one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']))

      

# <QUESTION 3>

# Given two numbers, a & b, and an operator, evaluate the operation between a & b
# using the given operator

# The operator will be a string, and will only be +, -, *, or /. 

# <EXAMPLES>

# two(2, 4, '+') → 6
# two(7, 3, '-') → 4
# two(3, 1.5, '*') → 4.5
# two(-5, 2, '/') → -2.5

# def two(a, b, operator):
#   result = eval(a + operator + b)
#   return result
   
# print(two(2,4,'+'))

def two(a, b, operator):

 user_result = eval(str(a) + operator + str(b))

 return user_result

print(two(2, 4, "+"))
print(two(7,3 ,'-'))
print(two(3,1.5,'*'))
print(two(-5,2,'/'))



# <QUESTION 4>

# Given a positive integer, return the next integer below it that has an
# integer square root (is the square of another integer)

# If the number has a square root, just return the number

# <EXAMPLES>

# three(7) → 4          # 4 is the square of 2
# three(64) → 64        # 64 is the square of 8 already
# three(32) → 25

# <HINT>

# We can use `x ** 0.5` to get the square root of `x`

def three(num):
 while (num ** 0.5) % 1 != 0:
  num = num - 1
  return (num)

print(three(7))

# <QUESTION 5>

# Given two integers, return the greatest common factor of the two numbers

# <EXAMPLES>

# four(32, 24) → 8
# four(18, 11) → 1
# four(10, 50) → 10


def four(a, b):
 (a,b) = (max(a,b), min(a,b))
 while b > 0:
  (a,b) = (b, a % b)
 return a


print(four(32,24))
print(four(18,11))
print(four(10,50))
    

# <QUESTION 6>

# Given a string, return a string where each letter is the previous letter in the alphabet
# in comparison to the original string

# For a or A, use z or Z respectively

# Ignore characters that aren't in the alphabet, such as whitespace or numbers

# <EXAMPLES>

# five('wxyz') → 'vwxy'
# five('abc') → 'zab'
# five('aAbB') → 'zZaA'
# five('hello world') → 'gdkkn vnqkc'
# five('54321') → '54321'

# def five(string):
#     pass
