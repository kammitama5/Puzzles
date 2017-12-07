"""
2.
Write code to reverse a C-style string. Name it reverse.
"""

def reverse(string):
  try:
    ## exception handling is done by concatenating input with string
	## will throw type-error mismatch if not a string
    string + ""
	## base case 0 or 1 length 
    if (len(string) <= 1):
      return string
	## pop and push to array, and join the chars of the array
    else:
     stackarr = []
     listofchars = list(string)
     while len(listofchars) > 0:
       stackarr.append(listofchars.pop())
     joinedarray =  "".join(stasckarr)
     return joinedarray
  except:
    return "Exception: Not of type string"
    
    
## what is input, what is output 
## string-> string 
## edge cases -> string is empty, string has one letter, string is not 
## of correct type -> exception handling
## comments and properly name variables 
## what is most efficient? (don't use .reverse)


# tests 
print reverse(0)
print reverse([1,2,3])
print reverse("")
print reverse(" ")
print reverse("a")
print reverse("aheloloo")
print reverse("Hi my name is Krystal")
