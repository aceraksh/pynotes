---
title: Basics
date: 2026-07-11
author: Your Name
cell_count: 47
score: 45
---

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
x =3

def outer():
    x = 1
    
    def inner():
        global x
        x = 2

    inner()
    print("Outer x:", x)

outer()
print("Global x:", x)
```

    Outer x: 1
    Global x: 2
    


```python
value = 5

def update():
    value = value + 1  
print(value)
```

    5
    


```python
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
    
print_numbers(5)
```

    1
    2
    3
    4
    5
    


```python
def fact(n):
    if n==0 and n>=0:
        return 1
    else:
        return n*fact(n-1)
print(fact(12))
```

    479001600
    


```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

    8
    


```python
def infinite_recursion():
    return infinite_recursion()
print(infinite_recursion)

```

    <function infinite_recursion at 0x0000021C9C66BEC0>
    


```python
def rev(text):
    if len(text)==0:
        return text
    return rev(text[1:])+text[0]
print(rev("pope"))
```

    epop
    


```python
import sys

print(sys.getrecursionlimit())  # Default ~1000
```

    3000
    


```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))
```

    832040
    


```python
import math

help(math)

```

    Help on built-in module math:
    
    NAME
        math
    
    DESCRIPTION
        This module provides access to the mathematical functions
        defined by the C standard.
    
    FUNCTIONS
        acos(x, /)
            Return the arc cosine (measured in radians) of x.
            
            The result is between 0 and pi.
        
        acosh(x, /)
            Return the inverse hyperbolic cosine of x.
        
        asin(x, /)
            Return the arc sine (measured in radians) of x.
            
            The result is between -pi/2 and pi/2.
        
        asinh(x, /)
            Return the inverse hyperbolic sine of x.
        
        atan(x, /)
            Return the arc tangent (measured in radians) of x.
            
            The result is between -pi/2 and pi/2.
        
        atan2(y, x, /)
            Return the arc tangent (measured in radians) of y/x.
            
            Unlike atan(y/x), the signs of both x and y are considered.
        
        atanh(x, /)
            Return the inverse hyperbolic tangent of x.
        
        cbrt(x, /)
            Return the cube root of x.
        
        ceil(x, /)
            Return the ceiling of x as an Integral.
            
            This is the smallest integer >= x.
        
        comb(n, k, /)
            Number of ways to choose k items from n items without repetition and without order.
            
            Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
            to zero when k > n.
            
            Also called the binomial coefficient because it is equivalent
            to the coefficient of k-th term in polynomial expansion of the
            expression (1 + x)**n.
            
            Raises TypeError if either of the arguments are not integers.
            Raises ValueError if either of the arguments are negative.
        
        copysign(x, y, /)
            Return a float with the magnitude (absolute value) of x but the sign of y.
            
            On platforms that support signed zeros, copysign(1.0, -0.0)
            returns -1.0.
        
        cos(x, /)
            Return the cosine of x (measured in radians).
        
        cosh(x, /)
            Return the hyperbolic cosine of x.
        
        degrees(x, /)
            Convert angle x from radians to degrees.
        
        dist(p, q, /)
            Return the Euclidean distance between two points p and q.
            
            The points should be specified as sequences (or iterables) of
            coordinates.  Both inputs must have the same dimension.
            
            Roughly equivalent to:
                sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
        
        erf(x, /)
            Error function at x.
        
        erfc(x, /)
            Complementary error function at x.
        
        exp(x, /)
            Return e raised to the power of x.
        
        exp2(x, /)
            Return 2 raised to the power of x.
        
        expm1(x, /)
            Return exp(x)-1.
            
            This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
        
        fabs(x, /)
            Return the absolute value of the float x.
        
        factorial(n, /)
            Find n!.
            
            Raise a ValueError if x is negative or non-integral.
        
        floor(x, /)
            Return the floor of x as an Integral.
            
            This is the largest integer <= x.
        
        fmod(x, y, /)
            Return fmod(x, y), according to platform C.
            
            x % y may differ.
        
        frexp(x, /)
            Return the mantissa and exponent of x, as pair (m, e).
            
            m is a float and e is an int, such that x = m * 2.**e.
            If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
        
        fsum(seq, /)
            Return an accurate floating point sum of values in the iterable seq.
            
            Assumes IEEE-754 floating point arithmetic.
        
        gamma(x, /)
            Gamma function at x.
        
        gcd(*integers)
            Greatest Common Divisor.
        
        hypot(...)
            hypot(*coordinates) -> value
            
            Multidimensional Euclidean distance from the origin to a point.
            
            Roughly equivalent to:
                sqrt(sum(x**2 for x in coordinates))
            
            For a two dimensional point (x, y), gives the hypotenuse
            using the Pythagorean theorem:  sqrt(x*x + y*y).
            
            For example, the hypotenuse of a 3/4/5 right triangle is:
            
                >>> hypot(3.0, 4.0)
                5.0
        
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
            Determine whether two floating point numbers are close in value.
            
              rel_tol
                maximum difference for being considered "close", relative to the
                magnitude of the input values
              abs_tol
                maximum difference for being considered "close", regardless of the
                magnitude of the input values
            
            Return True if a is close in value to b, and False otherwise.
            
            For the values to be considered close, the difference between them
            must be smaller than at least one of the tolerances.
            
            -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
            is, NaN is not close to anything, even itself.  inf and -inf are
            only close to themselves.
        
        isfinite(x, /)
            Return True if x is neither an infinity nor a NaN, and False otherwise.
        
        isinf(x, /)
            Return True if x is a positive or negative infinity, and False otherwise.
        
        isnan(x, /)
            Return True if x is a NaN (not a number), and False otherwise.
        
        isqrt(n, /)
            Return the integer part of the square root of the input.
        
        lcm(*integers)
            Least Common Multiple.
        
        ldexp(x, i, /)
            Return x * (2**i).
            
            This is essentially the inverse of frexp().
        
        lgamma(x, /)
            Natural logarithm of absolute value of Gamma function at x.
        
        log(...)
            log(x, [base=math.e])
            Return the logarithm of x to the given base.
            
            If the base not specified, returns the natural logarithm (base e) of x.
        
        log10(x, /)
            Return the base 10 logarithm of x.
        
        log1p(x, /)
            Return the natural logarithm of 1+x (base e).
            
            The result is computed in a way which is accurate for x near zero.
        
        log2(x, /)
            Return the base 2 logarithm of x.
        
        modf(x, /)
            Return the fractional and integer parts of x.
            
            Both results carry the sign of x and are floats.
        
        nextafter(x, y, /)
            Return the next floating-point value after x towards y.
        
        perm(n, k=None, /)
            Number of ways to choose k items from n items without repetition and with order.
            
            Evaluates to n! / (n - k)! when k <= n and evaluates
            to zero when k > n.
            
            If k is not specified or is None, then k defaults to n
            and the function returns n!.
            
            Raises TypeError if either of the arguments are not integers.
            Raises ValueError if either of the arguments are negative.
        
        pow(x, y, /)
            Return x**y (x to the power of y).
        
        prod(iterable, /, *, start=1)
            Calculate the product of all the elements in the input iterable.
            
            The default start value for the product is 1.
            
            When the iterable is empty, return the start value.  This function is
            intended specifically for use with numeric values and may reject
            non-numeric types.
        
        radians(x, /)
            Convert angle x from degrees to radians.
        
        remainder(x, y, /)
            Difference between x and the closest integer multiple of y.
            
            Return x - n*y where n*y is the closest integer multiple of y.
            In the case where x is exactly halfway between two multiples of
            y, the nearest even value of n is used. The result is always exact.
        
        sin(x, /)
            Return the sine of x (measured in radians).
        
        sinh(x, /)
            Return the hyperbolic sine of x.
        
        sqrt(x, /)
            Return the square root of x.
        
        tan(x, /)
            Return the tangent of x (measured in radians).
        
        tanh(x, /)
            Return the hyperbolic tangent of x.
        
        trunc(x, /)
            Truncates the Real x to the nearest Integral toward 0.
            
            Uses the __trunc__ magic method.
        
        ulp(x, /)
            Return the value of the least significant bit of the float x.
    
    DATA
        e = 2.718281828459045
        inf = inf
        nan = nan
        pi = 3.141592653589793
        tau = 6.283185307179586
    
    FILE
        (built-in)
    
    
    


```python
import math
print(dir(math))
```

    ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
    


```python
import datetime

today = datetime.date.today()
print(today)
```

    2026-07-10
    


```python
import datetime

today = datetime.date.today()
print(today)
```

    2026-07-10
    


```python
def main():
    print("Main function executed")

if __name__ == "__main__":
    main()
```

    Main function executed
    


```python
# main.py
import calculator

print(calculator.multiply(4, 5))  # Output: 20
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[29], line 2
          1 # main.py
    ----> 2 import calculator
          3 
          4 print(calculator.multiply(4, 5))  # Output: 20
    

    ModuleNotFoundError: No module named 'calculator'



```python
import math as o

print(o.pi)     # Output: 3.141592653589793
```

    3.141592653589793
    


```python
import math as r

print(r.sqrt(256)) 
```

    16.0
    


```python
import sys
print(sys.path)
```

    ['C:\\Users\\raksh_hp2y5k\\miniconda3\\envs\\test12\\python311.zip', 'C:\\Users\\raksh_hp2y5k\\miniconda3\\envs\\test12\\DLLs', 'C:\\Users\\raksh_hp2y5k\\miniconda3\\envs\\test12\\Lib', 'C:\\Users\\raksh_hp2y5k\\miniconda3\\envs\\test12', '', 'C:\\Users\\raksh_hp2y5k\\miniconda3\\envs\\test12\\Lib\\site-packages']
    


```python
# my_package/module1.py
def greet():
    return "Hello from module1"
```


```python
from setuptools import setup, find_packages
```


```python
def main():
    print("Main function executed")

if __name__ == "__main__":
    main()
print(__name__)
```

    Main function executed
    __main__
    


```python

```


---
**Score: 45**