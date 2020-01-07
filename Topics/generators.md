Generators and Lists 
Generators optimize memory and are represented by the () around a generator expression.
Having [] instead of () will generate a list instead.
Yield Statement 
unlike the return statement, the yield statement suspends the function execution but doesn't stop the function from continuing execution like the return statement

After the *next* has been exhausted from the iterator, a StopIteration Error is thrown.
Forexample.
    letters = iter(['a','b','c','d','e'])
    while True:
        try:
            letter = next(letters)
        except StopIteration:
            break
        print(letter)
            
Advanced generator methods include:
    - .throw()
    - .send()
    - .close()

A simple function to demonstrate all the three functions
def is_palindrome(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num*10)+(temp%10)
        temp = temp//10
    if num == reversed_num:
        return True
    else:
        return False

``` Infinite Sequence Generator```
def infinite_palindromes():
    nums = 0
    while True:
        if is_palindrome(nums):
            i = (yield nums)
            if i is not None:
                num = 1
        nums+=1

pal_gen = infinite_palindromes()

for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))    
