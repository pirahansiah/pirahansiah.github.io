


### Test-driven development (TDD) & Unit Testing & Google Test, TDD




<!-- C++23 keywords for parallel programming: Reviewing multi-threading features including concurrency, parallelism, thread management, mutexes, atomic operations, condition variables, semaphores, deadlocks, livelocks, performance metrics, and thread pools.

# C++23 Multi-threading and Parallel Programming Overview

- **Concurrency**
    - *Definition*: Ability of a program to handle more than one task at the same time.
        - **Program Structure**
             - Manage how a program executes tasks concurrently.
        - **Dealing with Multiple Things**
             - Enhance responsiveness by handling various operations simultaneously.

- **Parallelism**
    - *Definition*: Execution of multiple calculations or execution processes simultaneously.
        - **Simultaneous Execution**
            - Improve application performance by running tasks in parallel.

- **Context Switch**
    - *Definition*: Mechanism to switch between different tasks or threads.
        - **Saving and Loading State**
            - Save the state of a current task and load a new one to efficiently manage multiple tasks.

- **Thread Management**
    - *Basic Operations*
        - **.join()**
            - Ensures a thread finishes before the main program continues.
        - **.detach()**
            - Allows a thread to operate independently of the main program flow.
    - *Thread IDs and Process IDs*
        - Example Code:
            ```cpp
            printf(" Process ID: %d\n", getpid());
            printf(" Thread ID: %d\n", std::this_thread::get_id());
            ```

- **Synchronization Primitives**
    - *Mutexes and Locks*
        - **std::mutex**
            - Prevents simultaneous access to shared resources.
        - **std::recursive_mutex, std::shared_mutex**
            - Allows locks to be applied in a hierarchical manner.
    - *Atomic Operations*
        - **std::atomic**
            - Ensures operations are performed without interference from other threads.
    - *Condition Variables and Semaphores*
        - **std::condition_variable**
            - Coordinates the execution sequence between threads.
        - **Semaphores (Counting and Binary)**
            - Manages access to resources by multiple threads.

- **Deadlocks and Livelocks**
    - *Handling and Avoidance*
        - **Deadlock**
            - Condition where two or more threads are waiting on each other to release resources.
        - **Livelock**
            - Threads continuously change states in response to each other without making progress.

- **Performance Metrics**
    - *Efficiency Measures*
        - **Speedup and Efficiency**
            - Calculations that measure the improvement in performance when using parallel processing.
        - **Amdahl's Law**
            - Theoretical prediction of the possible speedup of program processing.

- **Design Patterns for Parallelism**
    - *Thread Pool and Futures*
        - **Thread Pool**
            - Reuses a number of threads for various tasks.
        - **Future and Promise**
            - Manages asynchronous operations and their results.
    - *Computational Graphs*
        - **DAG (Directed Acyclic Graph)**
            - Manages task dependencies and execution order.

- **Communication and Decomposition**
    - *Types and Strategies*
        - **Domain and Functional Decomposition**
            - Techniques for dividing tasks and data among processors.
        - **Communication**
            - Managing data flow between tasks, either synchronously or asynchronously. -->





<!-- # CPP 2023: Parallel and Concurrent Programming with C++
## create markdown format to copy .md file about below review keywords of c++ 23 for multi thread/multi cores/parallel programming
- example: 
Process ID, Thread ID
printf(" Process ID: %d\n", getpid());
printf(" Thread ID: %d\n", std::this_thread::get_id());

- concurrency: ability of a program to be broken into parts that can run independently of each other. 
  - program structure
  - **dealing** with multiple things at once
- parallelism
    - simultaneous execution
    - **doing** multiple things at once
- context switch
  - storing the state of a process or thread to resume later
  - loading the saved state for the new process or thread to run
- .join()
- std::thread th1(f); printf("  th1 is joinable? %s\n", th1.joinable() ? "true" : "false");
- .detached()
- std::mutex a1; a1.lock(); ... a1.unlock()
- std::atomic<unsigned int> a1(0); printf("%u",a1.locad())
- std::recursive_mutex a1;
- .try_lock()
- std::shared_mutex a1; .lock_shared(); .unlock_shared();
- deadlock: lock ordering, std::scoped_lock
- abandoned lock: std::scoped_lock(a1);
- starvation, livelock, std::this_thread::yield
- std::condition_variable a1;
- std::queue<int> a1;
- semaphore; std::counting_semaphore ; std::binary_semaphore;
- heisenbug; Race condition
- barrier; std::experimental::barrier
- latch; 
- Computational graph
  - DAG: directed acyclic graph 
- Thread pool
- future; std::future<int> result= std::async(std::launch::async, func1);
- Speedup, latency, and throughput
- amdahl's law: 1000 cpu only incread up to 20x faster!
  - printf("Average Sequential Time: %.1f ms\n", sequential_time.count()*1000);
    printf("  Average Parallel Time: %.1f ms\n", parallel_time.count()*1000);
    printf("Speedup: %.2f\n", sequential_time/parallel_time);
    printf("Efficiency %.2f%%\n", 100*(sequential_time/parallel_time)/std::thread::hardware_concurrency());
- paritioning 
    - domain competiion: block decomposition, cyclic decomposition, 
    - functional decompostion: 
- communication
  - point-to-point communication
  - collective communication: broadcast, scatter, gather 
  - synchronous: blocking 
  - asynchronous: nonblocking
- agglomeration; granularity; fine-grained parallelism; coarse-grained parallelism; 
- mapping;  -->


<!-- # C++ 

## CPP
- ## Review C++
  - ### Basics
    - **General-purpose programming language.**
    - Supports **object-oriented**, **procedural**, and **generic programming**.

  - ### Syntax & Operators
    - Basics: **Variables**, **data types**, and **functions**.
    - Operators: **Arithmetic**, **comparison**, and **logical**.

- ## Object-Oriented Programming
  - ### Classes & Objects
    - Blueprints for creating objects.
    - Support **encapsulation**.

  - ### Inheritance
    - Allows inheriting traits from other classes.
    - Supports **code reuse**.

  - ### Polymorphism
    - Entities take many forms.
    - Through **function overloading** and **overriding**.

  - ### Encapsulation
    - Bundles data and methods.
    - Restricts direct component access.

  - ### Abstraction
    - Hides complexities, exposes essentials.

- ## Memory Management
  - ### Dynamic Allocation
    - Manual management with **new** and **delete**.
    - Automated with **smart pointers**.

  - ### Resource Management
    - **RAII pattern** for resource management.

- ## Templates & STL
  - ### Function Templates
    - Operate with generic types.

  - ### Class Templates
    - Work with any data type.

  - ### STL Components
    - **Containers**, **algorithms**, **iterators**, **functors**.

- ## Modern C++ Features
  - ### Smart Pointers
    - Automate memory management.

  - ### Lambda Expressions
    - Define inline anonymous functions.

  - ### Auto & Decltype
    - **Auto** for automatic type deduction.
    - **Decltype** for expression type deduction.

  - ### Move Semantics
    - Efficient resource transfer.

  - ### Range-based Loops
    - Simplify collection iteration.

- ## Advanced Concepts
  - ### Concurrency
    - Multi-threading and asynchronous operations.

  - ### Templates & Meta-programming
    - Manipulate code during compilation.

  - ### Modules (C++20)
    - New code organization and compilation method.

- ## Best Practices
  - ### Code Organization
    - Use **namespaces** to prevent name collisions.

  - ### Error Handling
    - Use **exceptions** for runtime errors.
    - Prefer **noexcept** for non-exception cases.

  - ### Resource Management
    - Use **RAII** and **smart pointers** for resources.

- ## Tools & Techniques
  - ### Debugging
    - Use debuggers and analysis tools.

  - ### Performance Optimization
    - Profile to find bottlenecks.
    - Understand time and space complexity.

- ## Tools for Debugging and Performance Analysis
  - ### Overview
    - Focuses on tools like **Valgrind**, **AddressSanitizer**, and others.
    - Helps identify runtime errors and optimize performance.

  - ### Key Tools
    - **Valgrind**, **AddressSanitizer (ASan)**, **MemorySanitizer (MSan)**, **ThreadSanitizer (TSan)**.

  - ### Best Practices
    - Integrate these tools into regular testing routines.
    - Use in automated tests to catch errors early.
    - Incorporate into CI pipelines for ongoing quality assurance.

  - ### Integration with Development Environments
    - Many IDEs and editors support integration with these tools.
    - Enhances debugging and profiling within the development workflow.

  - ### Conclusion
    - These tools are essential for maintaining high-quality, performant software.
    - Regular use and integration into development practices can significantly reduce bugs and improve performance.

- ## CMake Fundamentals
  - ### Introduction
    - **Build system generator** for software projects.
    - Supports cross-platform projects.

  - ### Configuration
    - **Out-of-source builds**: Keeps source and build directories separate.
    - **Variable** usage to manage paths and settings.

  - ### Commands
    - **add_executable()**, **add_library()**, **find_package()**.

  - ### Best Practices
    - Organize source and header files clearly.
    - Use **subdirectories** and **target_link_libraries()** for modular projects.

  - ### Advanced Features
    - Custom Commands and Targets, Testing Support, Exporting Builds.

  - ### Toolchain Files
    - Specify compiler and tool options for cross-compiling.

  - ### Tips
    - Use CMake GUI for easier configuration and generation.
    - Refer to official documentation for detailed options and commands.

  - ### Tools & Integration
    - Integrated support in popular IDEs for easier development.
    - CTest for Testing, Techniques to speed up build times and manage dependencies efficiently.










---


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



 -->
