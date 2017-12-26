# Puzzles
notes involving interview stuff, graphs, algorithms, etc
I hope that I can have this as a life-long reference for interviewing and generally breaking
things down / problem-solving

## Basics

```
// - bitwise operation => divides one int by another, rounding the answer down to an integer
     Also rounds down even if the answer is negative.
```
```
.title() -> "Happy Birthday"
.islower() -> Boolean value
```

## Docstrings/ Documentation

```
Functions

def double(number):
    """Calculate the double of a number.

    number: int. The number to be doubled
    
    """
    return number
```
## Sets
- remove duplicates ```set(list1)```
- add to set ```list1.add("Mad Hatter")```
- pop ```list1.pop()```

## Dictionaries 

- if ```dict = {}```
  dict.get('elem') returns ```None```
  instead of ```KeyError```
 
## Use of * with lists, dictionaries and .format

- star operator is [unpacking value](https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean)
- Also, see Python documentation [here](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)
```
(*value) will split a list into sliced formatting when using a list
eg value = [1,2,3]
"{:21} {:13} {:8}".format(*value) - read up on this
```

## Tuples
- immutable
- can't sort in place

## File I/O

```
def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename) as f:
    # use the for loop syntax to process each line        
    # and add the actor name to cast_list
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list
# takes data, gets each line
# splits by ,
# appends first value
```

## WebScraping

```
html = urlopen("")
- two possible exceptions:
     1. Page not found on server (or error in retrieving it)
     2. Server not found
```

## Modules
- import multiple modules at once 

```from collections import defaultdict, namedtuple```
- import as 
```import pandas as pd```
- then access such as ```pd.read()```

## Topics

- Eulerian Path 
  - degree is the number of edges connected to that node.
  - first and last have to be odd and the rest even.
- Eulerian Tour 
  - start and return to same node
  ![et.png](et.png)
  ![et_path.png](et_path.png)
- Min-max
- Perms and Combs
- Divide and Conquer
- Recurrence relation 
- Linked Lists
- Binary Trees
- Tries
- Stacks
- Queues
- Vectors/ ArrayLists
- Hash Tables 
- Regex


## Jupyter Notebook

```
%pdb - Python debugger
```

[Built-in magic commands](http://ipython.readthedocs.io/en/stable/interactive/magics.html)

## Convert Jupyter notebook to HTML, etc 

- [nbconvert](https://nbconvert.readthedocs.io/en/latest/usage.html)

## Slideshow 

- make notebook into slideshow : ```jupyter nbconvert notebook.ipynb --to slides```

## Lambdas
- filter => ```list(filter(lambda x: x < 1, list1)```
- map => ```(list(map(lamda x: x**2,items)```
- reduce => ```from functools import reduce => reduce((lambda x, y: x * y), [1,2,3,4]) => outputs 24```

## LinkedLists
- stack pop, dequeue 

## Time Complexity 
- O(n) and all that good stuff

## Sorting and Searching
- Bubble, Heap, Merge, etc 
- tuple sort vs list sort 
- sort by abs ``` s = sorted(list1, key=abs) # would return [1,2,3,-4,-5]```
- sort reverse ```s = sorted(list1, reverse=True)```

## Other 

- random -> ```import random, random.choice([1,2,3])```
  ```
  import random
  random.seed(20)
  random.randint(1,100)
  ```
- Parsing Files in JSON
- File I/O
```
myFile = open(filename, 'w')
myFile.read
myFile.write('Yo mamma\n')

bool-> myFile.closed ## should return True

for line in myFile:
    print line   
```
- list comprehension

```
nums = [1,2,3,4]
my_list = [n*2 for n in nums]
print my_list # prints [2,4,6,8]

nums = [1,2,3,4]
my_list = [n*n for n in nums if n*n > 3]
print my_list # prints [4, 9, 16]

```
- Dicts (ugh)
  - If you need an ordered list -> ```collections.OrderedDict data``` documentation is your friend.
  
- Zip

```
names = ["a", "b","c","d"]
nums = [1,2,3,4]

my_dict = {}
for names, nums in zip(names, nums):
  my_dict[names] = nums
  
print my_dict # prints {a:1, b:2, etc}
```

- using list comprehension
```
my_dict = {names: nums for names, nums in zpi(names, nums)}
print my_dict # prints {a:1, b:2, etc}
```
  
- Generators -> ```yield```

```
def fib(num):
  a, b = 0, 1 
  for i in range(0, num):
    yield "{}: {}".format(i+1, a)
    a, b = b, a + b 
    
for item in fib(10):
  print item
```
- parson JSON
```
import json
json.loads(var) # load
json.dumps(var) # delete
loop through
indents-> json.dumps(var, indent=2) # indent twice

with open('file.json') as f:
  data = json.load(f) # load json file into python object
  
for i in data['key']:
  print i # print out object for each key
```
  
## OOP
  
- Classes and Methods

```
## class -> blueprint for creating instances

# class
class Employee:
  def __init__(self, first, last, email, pay):
    self.first = first
    self.last = last
    self.email = email
    self.pay = pay
  
  # method
  def fullname(self):
    return "name = {}, {}".format(self.last, self.first)
    
emp_1 = Employee("Krystal","Maughan","krystal.maughan@gmail.com",120000)
print "name : " + emp_1.first +  " " + emp_1.last # name : Krystal Maughan
print "email :" + emp_1.email # email :krystal.maughan@gmail.com
print "pay: ${}".format(emp_1.pay) # pay: $120000
print emp_1.fullname() # name = Maughan, Krystal
```
- super (is different in Python2 vs Python3..argh)

```
def __init__(self, first, last, pay, prog_lang):
    Employee.__init__(self,first, last, pay)## lets base class instantiate
    ## similar to C++ derived classes :D
```

- decorators -> ```@property```
```
@property
  def email(self):
    return '{}.{}@email.com'.format(self.first, self.last)
    
call -> print emp_1.email instead of emp_1.email() # dope!
```

- isinstance(instance, classname)

## Good advice
- Go slowly
- Input (what given), Output (what need to return)
- Write stubs first eg if it's a bool to check if true or false, do like C++ stubs 
- Write tests for edge cases (0, negatives, not of type requested etc)
- Ask for details (size of data, how contained, what type)
- Remember to be specific and clear when naming variables
- Comment code as needed
- If you find a bug, don't randomly try to fix output. Try to trace *why* it occurrs
- Break each verbal question into: 1. situation, 2. action, 3. response 

## Other Resources

- [Python Exercism](http://exercism.io/languages/python/about)




