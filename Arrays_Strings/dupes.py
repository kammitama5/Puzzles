"""
1.
Implement an algorithm uniquestr to determine if a string has all 
unique characters
"""

def uniquestr(string):
  # test to make sure is a string 
  try:
    arr = []
    ## edge cases return true
    if (len(string) == 0) or (len(string) == 1):
      return True
    else:
      # loop through string and get count, push to array
      for i in string:
        b = arr.append(string.count(i))
      # check that array doesn't contain a 1 / unique value
      # if it does, there is a non-unique value in array
      # if it contains only 1s, the values are unique 
      for i in arr:
        if not (i == 1):
          #print "contains a non-unique value"
          print False
          break;
        else:
          #print "all values are unique"
          print True
          break;
    return
  except:
    #print "This is not a valid string"
    print False
    return 
    
## there is a problem with this in that the array value is being 
## judged as a string 
## also, there should be a forall function to minimize 
## checking 
## also, can use a dictionary 
## all(type i is 1 in array )

print uniquestr([1,2,3])
print uniquestr(2)
print uniquestr("a")
print uniquestr("")
print uniquestr("araefearerae")
print uniquestr("bbb")
print uniquestr("ljwljerljerljeljwrw")
print uniquestr("abc")

# input string, output bool-> true or false -> write stubs!
# think about edge cases
# is the string empty
# is the string one letter long?
# how to get count?
# traverse land push to array count?
# dictionary?
# what has best time complexity?
# hash map vs array?
# anything eg itertools that can help?


