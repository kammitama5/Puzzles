def minim(list1):
  # set up function so that you are only sorting integers
  # return element, which is an int 
  ## first we check to ensure we are only sorting ints 
  try:
    num = list1[0] ## started with value being beginning value of list
    for i in list1: ## traverse list 
	## algorithm
      if i < num:
        num = i 
    #print num -> used for testing while debugging
    return num
  ## exception handling
  except:
    return "Not an int"
  ##return -> I didn't need this. 

minim([2,1,4,9,10])
minim([30,50,3])

## write a minim function as though being asked via an interview 
## write clear variable names 