# New Features in Python Versions 3.5 to 3.12

| Version | New Features | Brief Explanation |
|---------|--------------|-------------------|
| 3.5 | Async/Await Syntax | Introduced `async` and `await` keywords for asynchronous programming. |
| | Type Hints (PEP 484) | Added optional type annotations for static type checking. |
| | Matrix Multiplication Operator | Introduced the `@` operator for matrix multiplication. |
| 3.6 | Formatted String Literals (f-Strings) | Introduced f-Strings for easier string formatting using `{}` placeholders. |
| | Underscores in Numeric Literals | Allowed underscores for digit grouping in numeric literals (e.g., `1_000_000`). |
| | Variable Annotations (PEP 526) | Added syntax for annotating variable types. |
| | Asynchronous Generators | Enabled `async def` functions to use `yield` expressions. |
| | Asynchronous Comprehensions | Support for `async for` in list, set, dict comprehensions, and generator expressions. |
| 3.7 | Data Classes (PEP 557) | Introduced `@dataclass` decorator for automatic generation of class methods. |
| | Context Variables (PEP 567) | Added `contextvars` module for context-local state management. |
| | Built-in `breakpoint()` Function | Simplified debugging with the new `breakpoint()` function. |
| | Time Functions with Nanosecond Resolution | Enhanced time functions to support nanosecond precision. |
| 3.8 | Assignment Expressions (PEP 572) | Introduced the `:=` operator (walrus operator) for inline assignments within expressions. |
| | Positional-Only Parameters (PEP 570) | Allowed specification of positional-only parameters using `/` in function definitions. |
| | f-String Debug Support | f-Strings can include `=` for easy debugging (e.g., `f'{variable=}'`). |
| | `math.prod()` Function | Added `math.prod()` to calculate the product of an iterable. |
| 3.9 | Dictionary Merge & Update Operators (PEP 584) | Introduced `|` and `|=` for merging and updating dictionaries. |
| | Type Hinting Generics in Standard Collections (PEP 585) | Built-in collection types are now generic (e.g., `list[int]`). |
| | String Methods `removeprefix()` and `removesuffix()` | Added methods to remove prefixes and suffixes from strings. |
| | ZoneInfo Module (PEP 615) | Introduced `zoneinfo` module for IANA time zone support. |
| 3.10 | Structural Pattern Matching (PEP 634) | Added `match` and `case` statements for pattern matching similar to switch-case. |
| | Improved Error Messages | Provided more informative and precise syntax error messages. |
| | Parameter Specification Variables (PEP 612) | Enhanced typing for decorators and higher-order functions with `ParamSpec`. |
| 3.11 | Exception Groups (PEP 654) | Enabled raising and handling multiple exceptions simultaneously with `ExceptionGroup`. |
| | Fine-Grained Error Locations | More precise error locations in tracebacks and error messages. |
| | Performance Improvements | Significant speed enhancements in the CPython interpreter. |
| 3.12 | Python Zero-Cost Exceptions (PEP 709) | Reduced overhead of exceptions when they are not raised. |
| | Buffer Protocol Enhancements (PEP 688) | Added context management to the buffer protocol for safer resource handling. |
| | Deprecation of `wstr` in Unicode (PEP 623) | Simplified Unicode internals by removing the deprecated `wstr` member. |
| | Safe Path Joining (PEP 708) | Introduced safer methods for joining filesystem paths to prevent directory traversal vulnerabilities. |





https://realpython.com/async-io-python/
name of fucntion is call coroutine



import asyncio
async def foo():
    print("1")
    await asyncio.sleep(2)
    print("2")
async def another():
    print("another")
async def main():
    await asyncio.gether(foo(),another())

asyncio.run(main())

---
def foo()->int:
    try:
        raise Exception
    except Exception:
        print("Exception!")
        return 0

    finally:
        return 1

always return 1 :)

---




# Pandas: Hands-On Data Science: Sales Analysis in Python
- some times need to use encoding to read cvs file
- def.info()
- describe()
- .to_csv(""....)
- .tail(10)
- .plot(kind='hist',bins=10)
- 


# jupyter
clear output
do not use all one line pythonism code use many line easy to use other people and easy to fallow and easy to debug

[python coding x.com](https://x.com/clcoding/status/1793539716165284046)
[type hint](https://arash-hatami.ir/python-advance-type-hints/)

###  Powerful Python Features
- 

This mind map provides an organized overview of Python programming, covering basics, OOP, libraries, modern features, best practices, and tools.

### Python

#### Review Python

##### Basics
- Versatility
    - flexibility and ease of use
- Cross-platform Compatibility
- Community Support
- Open Source
- **High-level, interpreted programming language.**
- Emphasizes **readability** and **simplicity**.

##### Syntax & Operators
- Basics: **Variables**, **data types**, and **functions**.
- Operators: **Arithmetic**, **comparison**, and **logical**.

##### Object-Oriented Programming
###### Classes & Objects
- Structures for creating objects.
- Encourages **encapsulation**.

###### Inheritance
- Facilitates inheritance of properties from other classes.
- Promotes **code reusability**.

###### Polymorphism
- Supports different forms of functions.
- Through **method overriding**.

###### Encapsulation
- Groups related data and functions.
- Controls access to the internals of the class.

###### Abstraction
- Simplifies complex reality by modeling classes appropriate to the problem.

##### Memory Management
###### Garbage Collection
- Automatic memory management through **garbage collection**.

###### Resource Management
- Context managers (`with` statement) for managing resources.

##### Libraries & Frameworks
###### Standard Library
- Rich in-built modules and functions.

###### Popular Frameworks
- **Django** for web applications.
- **Flask** for lightweight web services.
- **Pandas** for data analysis.

##### Modern Python Features
###### Generators
- Simplify creation of iterators.

###### Decorators
- Enhance functions without permanent modifications.

###### Context Managers
- Manage resources with `with` statements.

###### Comprehensions
- Concise syntax for lists, dictionaries, and sets.

##### Advanced Concepts
###### Asynchronous Programming
- **asyncio** library for writing concurrent code.

###### Decorators & Generators
- Advanced use cases for functional enhancements.

###### Typing Support
- Static typing with **type hints**.

##### Best Practices
###### Code Style
- Follow **PEP 8** for style guidelines.

###### Error Handling
- Use **exceptions** for managing errors effectively.

###### Resource Management
- Utilize context managers for reliable resource handling.

##### Tools & Techniques
###### Debugging
- Use tools like **pdb** for debugging Python code.

###### Performance Optimization
- Use **profiling tools** to identify bottlenecks.

##### Testing
###### Unit Testing
- **unittest** framework for testing individual units of source code.

###### Integration Testing
- Combine modules logically and test as a group.

##### Packaging & Distribution
###### Setuptools & Pip
- Tools for packaging and distributing Python projects.

###### Virtual Environments
- **virtualenv** to manage dependencies for different projects.

##### Continuous Integration and Deployment
- Automate testing and deployment using CI/CD tools like Jenkins, GitHub Actions.

##### Conclusion
- Python's simplicity and vast ecosystem make it ideal for a wide range of applications from web development to data science.
