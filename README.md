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




