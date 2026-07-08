---
title: Basics
date: 2026-07-08
author: Your Name
cell_count: 11
score: 10
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
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def subract(a,b):
    return a-b
print (add(2,3))
print (add(2.3,0))
print (multiply(12.3,4))

```

    5
    2.3
    49.2
    


```python
def display_profile(**kwargs):
    for k, value in kwargs.items():
        print(f"{k}: {value}")

display_profile(name="Alice", role="Engineer")
```

    name: Alice
    role: Engineer
    


```python
def complete_profile(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

complete_profile("Python", level="Advanced", year=2025)
```

    Positional: ('Python',)
    Keyword: {'level': 'Advanced', 'year': 2025}
    


```python
def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

print(factorial(12))  
```

    479001600
    


```python

```


---
**Score: 10**