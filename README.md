# Puzzles
notes involving interview stuff, graphs, algorithms, etc
I hope that I can have this as a life-long reference for interviewing and generally breaking
things down / problem-solving

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




