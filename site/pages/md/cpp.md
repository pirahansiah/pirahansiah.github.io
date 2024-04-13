# CPP 

## Review C++ 

### Basics
- **General-purpose programming language.**
- Supports **object-oriented**, **procedural**, and **generic programming**.

### Syntax & Operators
- Basics: **Variables**, **data types**, and **functions**.
- Operators: **Arithmetic**, **comparison**, and **logical**.

### Object-Oriented Programming
#### Classes & Objects
- Blueprints for creating objects.
- Support **encapsulation**.

#### Inheritance
- Allows inheriting traits from other classes.
- Supports **code reuse**.

#### Polymorphism
- Entities take many forms.
- Through **function overloading** and **overriding**.

#### Encapsulation
- Bundles data and methods.
- Restricts direct component access.

#### Abstraction
- Hides complexities, exposes essentials.

### Memory Management
#### Dynamic Allocation
- Manual management with **new** and **delete**.
- Automated with **smart pointers**.

#### Resource Management
- **RAII pattern** for resource management.

### Templates & STL
#### Function Templates
- Operate with generic types.

#### Class Templates
- Work with any data type.

#### STL Components
- **Containers**, **algorithms**, **iterators**, **functors**.

### Modern C++ Features
#### Smart Pointers
- Automate memory management.

#### Lambda Expressions
- Define inline anonymous functions.

#### Auto & Decltype
- **Auto** for automatic type deduction.
- **Decltype** for expression type deduction.

#### Move Semantics
- Efficient resource transfer.

#### Range-based Loops
- Simplify collection iteration.

### Advanced Concepts
#### Concurrency
- Multi-threading and asynchronous operations.

#### Templates & Meta-programming
- Manipulate code during compilation.

#### Modules (C++20)
- New code organization and compilation method.

### Best Practices
#### Code Organization
- Use **namespaces** to prevent name collisions.

#### Error Handling
- Use **exceptions** for runtime errors.
- Prefer **noexcept** for non-exception cases.

#### Resource Management
- Use **RAII** and **smart pointers** for resources.

### Tools & Techniques
#### Debugging
- Use debuggers and analysis tools.

#### Performance Optimization
- Profile to find bottlenecks.
- Understand time and space complexity.





## Tools for Debugging and Performance Analysis

### Overview
- Focuses on tools like **Valgrind**, **AddressSanitizer**, and others.
- Helps identify runtime errors and optimize performance.

### Valgrind
- A tool for **memory debugging**, **memory leak detection**, and **profiling**.
- Works by monitoring memory usage of programs in execution.

#### Key Features
- **Memcheck**: Detects memory-management problems.
- **Cachegrind**: Profiles cache and branch-prediction.
- **Callgrind**: Records the call history among functions.

#### Usage
- Run programs with `valgrind --tool=tool_name your_program`.

### AddressSanitizer (ASan)
- A fast memory error detector.
- Part of LLVM/Clang and GCC compilers.

#### Key Features
- Detects **buffer overflows**, **use-after-free**, and more.
- Minimal runtime overhead compared to Valgrind.

#### Usage
- Compile programs with `-fsanitize=address` flag.

### MemorySanitizer (MSan)
- Uncovers uninitialized memory reads.
- Also part of LLVM/Clang.

#### Usage
- Compile with `-fsanitize=memory` to enable.

### ThreadSanitizer (TSan)
- Detects **data races** and **deadlocks** in multi-threaded code.
- Available in LLVM/Clang and GCC.

#### Usage
- Compile with `-fsanitize=thread` to use.

### Best Practices
#### Regular Use
- Integrate these tools into regular testing routines.

#### Automated Testing
- Use in automated tests to catch errors early.

#### Continuous Integration
- Incorporate into CI pipelines for ongoing quality assurance.

### Integration with Development Environments
- Many IDEs and editors support integration with these tools.
- Enhances debugging and profiling within the development workflow.

### Tips for Effective Usage
#### Start Early
- Use these tools from the beginning of the development cycle.

#### Focus on Fixing
- Prioritize fixing reported issues to improve code quality.

#### Learn from Mistakes
- Use findings to understand and avoid future bugs.

### Conclusion
- These tools are essential for maintaining high-quality, performant software.
- Regular use and integration into development practices can significantly reduce bugs and improve performance.






## CMake Fundamentals

### Introduction
- **Build system generator** for software projects.
- Supports cross-platform projects.

### Basic Concepts
- Uses **CMakeLists.txt** for project configuration.
- Defines build processes in a platform-independent manner.

### Configuration
- **Out-of-source builds**: Keeps source and build directories separate.
- **Variable** usage to manage paths and settings.

### Commands
- **add_executable()**: Defines a target executable.
- **add_library()**: Defines a library target.
- **find_package()**: Locates external libraries.

### Building a Project
- **CMake command**: Generates project files for build tools.
- **Make command**: Compiles the project using generated files.

### Best Practices
#### Directory Structure
- Organize source and header files clearly.

#### Version Control
- **CMakeLists.txt** and **.cmake** files should be version-controlled.

#### Modularization
- Use **subdirectories** and **target_link_libraries()** for modular projects.

### Advanced Features
#### Custom Commands and Targets
- Execute additional tasks during the build process.

#### Testing Support
- **enable_testing()** and **add_test()** for project tests.

#### Exporting Builds
- Allows other projects to easily use the library.

### Toolchain Files
- Specify compiler and tool options for cross-compiling.

### CMake Variables
- Predefined and user-defined for customization.

### Caching
- Stores options and settings to speed up reconfiguration.

### Cross-Platform Builds
- Simplify building on multiple operating systems.

### Tips
#### Use CMake GUI
- For easier configuration and generation.

#### Documentation
- Refer to official documentation for detailed options and commands.

### Tools & Integration
#### IDE Support
- Integrated support in popular IDEs for easier development.

#### CTest for Testing
- Built-in test management tool.

### Performance Optimization
- Techniques to speed up build times and manage dependencies efficiently.




## Code
``` cpp
- rm -rf build/
- clang -fsanitize=address -g main.cpp
- for (const auto& value: container){}
-   std::map<char,int> my_dict{{'a',27},{'b',22}};
    for (const auto& [key,value]:my_dict){ key , value}
- std::array<int, 3> arr={1,2,3};
- references = & = avoid copy, faster
    - best **"const"** : by reference change the orginal value if you do not want (and not using pass by value which is slow) you can use **const**
        - void DoSmth(const std::string& huge_string);
- overloading: use different type but the name is same

- int main(int argc, char const *argv[])
- auto [a,b,c]= make_tuple(4,2.2,"farshid");
``` 

-nameing
    - variables, function arguments,  = snake_case
    - constants, functions, = CamelCase
    - 