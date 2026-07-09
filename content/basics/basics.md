---
title: Basics
date: 2026-07-09
author: Your Name
cell_count: 27
score: 25
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
sq = lambda x: x ** 2
print(sq(97))  # Output: 25
```

    9409
    


```python
def disp(name,age,department):
    print(f"name:{name},age:{age},department:{department}")
disp(name="raksh",department="cse",age=19)
```

    name:raksh,age:19,department:cse
    


```python
def login(username, password):
    print(f"User: {username}")

login("admin", "1234")

```

    User: admin
    


```python
def user(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user(name="raksh", role="Developer", level="junior")
user(name="raksh", role="Developer", level="junior")

```

    name: raksh
    role: Developer
    level: junior
    name: raksh
    role: Developer
    level: junior
    


```python
def full_profile(name, *skills, **info):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", info)

full_profile("Alice", "Python", "ML", age=30, city="Toronto")
```

    Name: Alice
    Skills: ('Python', 'ML')
    Details: {'age': 30, 'city': 'Toronto'}
    


```python
def configure(mode="light"):
    print(f"Mode: {mode}")

configure(mode="dark")
```

    Mode: dark
    


```python
def add(a,b,c):
    return a+b+c
values={"a":2,"b":12,"c":43}
print(add(**values))
```

    57
    


```python
count = 10

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```

    11
    


```python
val=12
def local():
    val=10
    return 
print(local())
print(val)
```

    10
    12
    


```python
def outer():
    message = "Hello"
    def inner():
        print(message)  
    inner()
outer()
```


```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 9
        print(count)
    inner()
outer()
```

    9
    


```python
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        nonlocal x 
        x= "Local"
        print(x)

    inner()

outer()

```

    Local
    


```python
for i in range(9):
    a = i

print(a)  # Accessible outside loop
```

    8
    


```python
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)
    inner()
    print(x)
outer()
print(x)
```

    Local
    Enclosing
    Global
    


```python
value = 5

def update():
   value+= 1
   print(value)
```


```python
x = 100

def outer():
    def inner():
        global x
        x = 200
    inner()
    print(x)

outer()
print(x)
```

    200
    200
    


```python

```


---
**Score: 25**