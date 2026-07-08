---
title: Basics
date: 2026-07-08
author: Your Name
cell_count: 7
score: 5
---

```python
print("hello")
```

    hello
    


```python
print(2+3)
```

    5
    


```python
def add(x,y):
    return(x+y)
add(2,4)    
```




    6




```python
def greet(name="guest"):
    print(f"Hello{name}!")
greet()
greet("preet")
```

    Helloguest!
    Hellopreet!
    


```python
age=int(input("age:"))
if age>18:
    print("eligible to vote")
else:
    print("not valid")
```

    age: 12
    

    not valid
    


```python
score=int(input("Score:"))
if score>90:
    print("A grade")
elif score>80:
    print("B grade")
else:
    print("c grade")
```

    Score: 34
    

    c grade
    


```python

```


---
**Score: 5**