def printPattern(targetNumber) :
  
  if (targetNumber <= 0) :
    print(targetNumber)
    return

  print(targetNumber)
  printPattern(targetNumber - 5)
#   print(targetNumber, "lll")

# Driver Program 
n = 10
# printPattern(n)

def reversestr(string):
    length  = len(string)
    if length == 0:
        return string
    return reversestr(string[1:]) + string[0]

# print(reversestr("powers"))

def countVowels(s, count=0):
    vowels = "aeiou"
    if not len(s):
        return count
    if s[0].lower() in vowels:
        count += 1
    return countVowels(s[1:], count)

print(countVowels("Educative"))