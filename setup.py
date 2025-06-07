# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="pyoverflow3",
    version="1.0.0",
    description="A Python3 Library for Quick Debugging of Errors using StackOverflow",
    long_description="""A Python Library for Quick Debugging of Errors using StackOverflow
    
    A complete rewritten library in Python3 based on pyoverflow library which was based on Python2

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
import pyoverflow3
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

     import pyoverflow3

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
                     """

    ,
    long_description_content_type="text/markdown",
    url="https://github.com/SpaciousCoder78/pyoverflow3",
    author="Aryan Karamtoth",
    author_email="aryankmmiv@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent"
    ],
    packages=["pyoverflow3"],
    include_package_data=True,
    install_requires=["googlesearch-python"]
)