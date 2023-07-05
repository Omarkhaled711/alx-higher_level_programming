# Alx tasks: Everything is object

* 0-answer.txt: a function used to get the type of objects in python
* 1-answer.txt: get the variable identifier (which is the memory address in the CPython implementation)
* 2-answer.txt: do a, and b point to the same object: ">>> a = 89, b = 100"
* 3-answer.txt: do a, and b point to the same object: ">>> a = 89, b = 89"
* 4-answer.txt: do a, and b point to the same object: ">>> a = 89, b = a"
* 5-answer.txt: do a, and b point to the same object: ">>> a = 89, b = a + 1"
* 6-answer.txt: print the output of the following code  
```python
s1 = "Best School"
s2 = s1
print(s1 == s2)
```
* 7-answer.txt: print the output of the following code   
```python
s1 = "Best School"
s2 = s1
print(s1 is s2)
```
* 8-answer.txt: print the output of the following code  
```python
s1 = "Best School"
s2 = "Best school"
print(s1 == s2)
```
* 9-answer.txt: print the output of the following code  
```python
s1 = "Best School"
s2 = "Best school"
print(s1 is s2)
```
* 10-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 == l2)
```
* 11-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = [1, 2, 3] 
print(l1 is l2)
```
* 12-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l1
print(l1 == l2)
```
* 13-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l2
print(l1 is l2)
```
* 14-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
* 15-answer.txt: print the output of the following code  
```python
l1 = [1, 2, 3]
l2 = l2
l1 = l1 + [4]
print(l2)
```
* 16-answer.txt: print the output of the following code  
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
* 17-answer.txt: print the output of the following code  
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
* 18-answer.txt: print the output of the following code  
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
* 19-copy_list.py: create a function with max 3-line long
