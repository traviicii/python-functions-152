# Lecture Notes - Python Functions

## Built-in Functions

### `print()` and Special Characters
- `print()`: Used to output text to the console.
- Special Characters:
  - `\n`: New line
  - `\t`: Tab
  - `\\`: Backslash
  - `sep`: Separator between values
  - `end`: End character

```python
print("Hello, world!")  # Simple print
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab
print("Hello\\World")   # Backslash
print("Hello", "World", sep="-")  # Separator
print("Hello", end="!!!\n")  # End character
```

### String Concatenation

**Combining strings using the + operator**
```python
greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message)  # Output: Hello Alice
```

### Formatted Strings

- Using f-strings and `.format()` for string formatting

```python
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # f-string
print("Name: {}, Age: {}".format(name, age))  # .format()
```

### `input()`
- Used to take input from the user.
- Always returns a `string`!

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### `type()`
- Returns the type of the variable.

```python
num = 10
print(type(num))  # Output: <class 'int'>
```

### `len()`
- Returns the length of an object.

```python
message = "Hello"
print(len(message))  # Output: 5
```

### `isinstance(var, type)` Returns `bool`
- Checks if a variable is of a specific type.

```python
num = 10
print(isinstance(num, int))  # Output: True
```

### `abs()`
- Returns the absolute value.

```python
number = -5
print(abs(number))  # Output: 5
```

### `round()`
- Rounds a number to the nearest integer or specified number of decimal places.

```python
number = 4.567
print(round(number))  # Output: 5
print(round(number, 2))  # Output: 4.57
```

### `sum()`
- Returns the sum of all items in an iterable.

```python
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Output: 10
```

### `min()`
- Returns the smallest item in an iterable.

```python
numbers = [1, 2, 3, 4]
print(min(numbers))  # Output: 1
```

### `max()`
- Returns the largest item in an iterable.

```python
numbers = [1, 2, 3, 4]
print(max(numbers))  # Output: 4
```

### `pow()`
- Returns the power of a number.

```python
print(pow(2, 3))  # Output: 8
```

### `divmod()`
- Returns a tuple containing the quotient and remainder.

```python
print(divmod(10, 3))  # Output: (3, 1)
```

## Type Casting

### `int()`
- Converts a value to an integer.

```python
print(int("10"))  # Output: 10
```

### `str()`
- Converts a value to a string.

```python
print(str(10))  # Output: "10"
```

### `float()`
- Converts a value to a float.

```python
print(float("10.5"))  # Output: 10.5
```

### `bool()`
- Converts a value to a boolean.

```python
print(bool(0))  # Output: False
print(bool(1))  # Output: True
```

## User Functions

### Syntax

```python
def function_name():
    # code block
    pass
```

### Call the Function by Name to Execute its Code

```python
def greet():
    print("Hello, world!")

greet()  # Output: Hello, world!
```

### Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### Default Parameters

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
```

### `*args`
- Unknown number of arguments, brought into the function as a tuple
```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6
```

### `**kwargs`
- Unknown amount of keyword arguments, brought into the function as a Dictionary
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
# Output:
# name: Alice
# age: 30
```

### `return`

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5
```

### Scope (Local vs. Global)

```python
x = "global"

def test():
    x = "local"
    print(x)  # Output: local

test()
print(x)  # Output: global
```

### `pass`

```python
def placeholder():
    pass
```

## Debugging

### Print Statements

```python
def add(a, b):
    print(f"a: {a}, b: {b}")  # Debugging print
    return a + b

result = add(2, 3)
print(result)  # Output: 5
```

