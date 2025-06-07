# pyoverflow3
Complete Rewrite of pyoverflow library from Python 2 to Python 3

A Python Library for Quick Debugging of Errors using StackOverflow
    


## Supported Features
- Quick Search of errors on StackOverflow for Python

## Planned Features
Integration with other languages like:
- Java
- JavaScript
- C
- C++ and many more

## Installation

```sh
$ pip install pyoverflow3
```

## Getting Started

Import the package

```py
from pyoverflow3.pyoverflow3 import pyoverflow3
```
Create a `.py` file and include try-except block where you may expect an error and pass the error and number of solutions into `pyoverflow3.submit_error(err_msg,no_solutions)`

Once an error gets generated, the library gets called and it instantly shows you possible solutions for your error.

## Documentation

### Available Methods
- `pyoverflow3.submit_error(err_msg,no_solution)` 

    Accepted arguments 2: 
    err_msg: pass the error message from try-except block
    no_solution: pass the number of solutions you need to display
    
    **Usage**:
    
    ```py
    #!/usr/bin/env python

     from pyoverflow3.pyoverflow3 import pyoverflow3

    a = int(input("Enter first number"))

    b = int(input("Enter second number"))


    try:
	    div = a/b
	    print(div)

    except Exception as e:
	    #Error message and number of solutions
	    pyoverflow3.submit_error(str(e),2)

    #Wait for the magic :)
    ```
