If you are reading this you probably need a simpler clearer explanation for the bunary to string problem. I came across this in the Cracking the coding interview book and found it to be abit a little bit confusing bit finally got the gist of it and that's what i want to share with you. 

#### Binary to String: 
Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters, print"ERROR:'

#### Solution.
Note: we are required to convert a double decimal number to binary representation
Check if the number is greater than 1 or less than 0. If so, return an Error.

We can convert double decimal integers in many ways. 
Method One:
Multiply the decimal number by 2. Forexample, If the number we are supposed to convert is 0.625, we do the following steps. 
r = 2*0.625
r = 1.25

if r is greater than or equal to 1, we add 1 after the decimal point in our answer. hence answer will be updated to look like this for the 0.1 since r is greater than 1.
we then subtract one from r and n becomes r.
Now r will be 1.25-1 and so we repeat the steps above.
2*0.25= 0.5
Now that r is 0.5, which is less than 1, we append 0 to the answer string hence answer becoming 0.10. Since r is less than 0, we don't subtract anything from r. so n = r and we return back to the top of the loop untill we break out of the loop. 

If r is less than 1, we add 0 to the answer(string) hence for the case of 0.

###### Step One:


###### Step Two:
###### Step Three:




```python
def binTostring(num):
    result = "0."
    if num > 1 or num < 0:
        return "Error"
    while num!=0:
        if len(result) > 32:
            return "Error"
        num*=2
        if num >= 1:
            result+="1"
            num-=1
        else:
            result+="0"
    return result
```