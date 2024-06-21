# <span style="color:blue">C++ Review</span>

## <span style="color:green">Basics</span>
- <span style="color:purple">**General-purpose programming language.**</span>
- <span style="color:darkorange">Supports **object-oriented**, **procedural**, and **generic programming**.</span>

## <span style="color:blue">Syntax & Operators</span>
- <span style="color:green">Basics: **Variables**, **data types**, and **functions**.</span>
- <span style="color:purple">Operators: **Arithmetic**, **comparison**, and **logical**.</span>

## <span style="color:blue">Object-Oriented Programming</span>
### <span style="color:green">Classes & Objects</span>
- <span style="color:darkorange">Blueprints for creating objects.</span>
- <span style="color:purple">Support **encapsulation**.</span>

### <span style="color:green">Inheritance</span>
- <span style="color:darkorange">Allows inheriting traits from other classes.</span>
- <span style="color:purple">Supports **code reuse**.</span>

### <span style="color:green">Polymorphism</span>
- <span style="color:darkorange">Entities take many forms.</span>
- <span style="color:purple">Through **function overloading** and **overriding**.</span>

### <span style="color:green">Encapsulation</span>
- <span style="color:darkorange">Bundles data and methods.</span>
- <span style="color:purple">Restricts direct component access.</span>

### <span style="color:green">Abstraction</span>
- <span style="color:darkorange">Hides complexities, exposes essentials.</span>

## <span style="color:blue">Memory Management</span>
### <span style="color:green">Dynamic Allocation</span>
- <span style="color:darkorange">Manual management with **new** and **delete**.</span>
- <span style="color:purple">Automated with **smart pointers**.</span>

### <span style="color:green">Resource Management</span>
- <span style="color:darkorange">**RAII pattern** for resource management.</span>

## <span style="color:blue">Templates & STL</span>
### <span style="color:green">Function Templates</span>
- <span style="color:darkorange">Operate with generic types.</span>

### <span style="color:green">Class Templates</span>
- <span style="color:darkorange">Work with any data type.</span>

### <span style="color:green">STL Components</span>
- <span style="color:darkorange">**Containers**, **algorithms**, **iterators**, **functors**.</span>

## <span style="color:blue">Modern C++ Features</span>
### <span style="color:green">Smart Pointers</span>
- <span style="color:darkorange">Automate memory management.</span>

### <span style="color:green">Lambda Expressions</span>
- <span style="color:darkorange">Define inline anonymous functions.</span>

### <span style="color:green">Auto & Decltype</span>
- <span style="color:darkorange">**Auto** for automatic type deduction.</span>
- <span style="color:purple">**Decltype** for expression type deduction.</span>

### <span style="color:green">Move Semantics</span>
- <span style="color:darkorange">Efficient resource transfer.</span>

### <span style="color:green">Range-based Loops</span>
- <span style="color:darkorange">Simplify collection iteration.</span>

## <span style="color:blue">Advanced Concepts</span>
### <span style="color:green">Concurrency</span>
- <span style="color:darkorange">Multi-threading and asynchronous operations.</span>

### <span style="color:green">Templates & Meta-programming</span>
- <span style="color:darkorange">Manipulate code during compilation.</span>

### <span style="color:green">Modules (C++20)</span>
- <span style="color:darkorange">New code organization and compilation method.</span>

## <span style="color:blue">Best Practices</span>
### <span style="color:green">Code Organization</span>
- <span style="color:darkorange">Use **namespaces** to prevent name collisions.</span>

### <span style="color:green">Error Handling</span>
- <span style="color:darkorange">Use **exceptions** for runtime errors.</span>
- <span style="color:purple">Prefer **noexcept** for non-exception cases.</span>

### <span style="color:green">Resource Management</span>
- <span style="color:darkorange">Use **RAII** and **smart pointers** for resources.</span>

## <span style="color:blue">Tools & Techniques</span>
### <span style="color:green">Debugging</span>
- <span style="color:darkorange">Use debuggers and analysis tools.</span>

### <span style="color:green">Performance Optimization</span>
- <span style="color:darkorange">Profile to find bottlenecks.</span>
- <span style="color:purple">Understand time and space complexity.</span>

---

# <span style="color:blue">Tools for Debugging and Performance Analysis</span>

## <span style="color:green">Overview</span>
- <span style="color:darkorange">Focuses on tools like **Valgrind**, **AddressSanitizer**, and others.</span>
- <span style="color:purple">Helps identify runtime errors and optimize performance.</span>

## <span style="color:blue">Valgrind</span>
- <span style="color:green">A tool for **memory debugging**, **memory leak detection**, and **profiling**.</span>
- <span style="color:darkorange">Works by monitoring memory usage of programs in execution.</span>

### <span style="color:purple">Key Features</span>
- <span style="color:green">**Memcheck**: Detects memory-management problems.</span>
- <span style="color:darkorange">**Cachegrind**: Profiles cache and branch-prediction.</span>
- <span style="color:purple">**Callgrind**: Records the call history among functions.</span>

## <span style="color:blue">AddressSanitizer (ASan)</span>
- <span style="color:green">A fast memory error detector.</span>
- <span style="color:darkorange">Part of LLVM/Clang and GCC compilers.</span>

### <span style="color:purple">Key Features</span>
- <span style="color:green">Detects **buffer overflows**, **use-after-free**, and more.</span>
- <span style="color:darkorange">Minimal runtime overhead compared to Valgrind.</span>

## <span style="color:blue">MemorySanitizer (MSan)</span>
- <span style="color:green">Uncovers uninitialized memory reads.</span>
- <span style="color:darkorange">Also part of LLVM/Clang.</span>

## <span style="color:blue">ThreadSanitizer (TSan)</span>
- <span style="color:green">Detects **data races** and **deadlocks** in multi-threaded code.</span>
- <span style="color:darkorange">Available in LLVM/Clang and GCC.</span>

## <span style="color:blue">Best Practices</span>
### <span style="color:green">Regular Use</span>
- <span style="color:darkorange">Integrate these tools into regular testing routines.</span>

### <span style="color:green">Automated Testing</span>
- <span style="color:darkorange">Use in automated tests to catch errors early.</span>

### <span style="color:green">Continuous Integration</span>
- <span style="color:darkorange">Incorporate into CI pipelines for ongoing quality assurance.</span>

## <span style="color:blue">Integration with Development Environments</span>
- <span style="color:green">Many IDEs and editors support integration with these tools.</span>
- <span style="color:darkorange">Enhances debugging and profiling within the development workflow.</span>

## <span style="color:blue">Tips for Effective Usage</span>
### <span style="color:green">Start Early</span>
- <span style="color:darkorange">Use these tools from the beginning of the development cycle.</span>

### <span style="color:green">Focus on Fixing</span>
- <span style="color:darkorange">Prioritize fixing reported issues to improve code quality.</span>

### <span style="color:green">Learn from Mistakes</span>
- <span style="color:darkorange">Use findings to understand and avoid future bugs.</span>

## <span style="color:blue">Conclusion</span>
- <span style="color:green">These tools are essential for maintaining high-quality, performant software.</span>
- <span style="color:darkorange">Regular use and integration into development practices can significantly reduce bugs and improve performance.</span>

---

# <span style="color:blue">CMake Fundamentals</span>

## <span style="color:green">Introduction</span>
- <span style="color:darkorange">**Build system generator** for software projects.</span>
- <span style="color:purple">Supports cross-platform projects.</span>

## <span style="color:blue">Basic Concepts</span>
- <span style="color:green">Uses **CMakeLists.txt** for project configuration.</span>
- <span style="color:darkorange">Defines build processes in a platform-independent manner.</span>

## <span style="color:blue">Configuration</span>
- <span style="color:green">**Out-of-source builds**: Keeps source and build directories separate.</span>
- <span style="color:darkorange">**Variable** usage to manage paths and settings.</span>

## <span style="color:blue">Commands</span>
- <span style="color:green">**add_executable()**: Defines a target executable.</span>
- <span style="color:darkorange">**add_library()**: Defines a library target.</span>
- <span style="color:purple">**find_package()**: Locates external libraries.</span>

## <span style="color:blue">Building a Project</span>
- <span style="color:green">**CMake command**: Generates project files for build tools.</span>
- <span style="color:darkorange">**Make command**: Compiles the project using generated files.</span>

## <span style="color:blue">Best Practices</span>
### <span style="color:green">Directory Structure</span>
- <span style="color:darkorange">Organize source and header files clearly.</span>

### <span style="color:green">Version Control</span>
- <span style="color:darkorange">**CMakeLists.txt** and **.cmake** files should be version-controlled.</span>

### <span style="color:green">Modularization</span>
- <span style="color:darkorange">Use **subdirectories** and **target_link_libraries()** for modular projects.</span>

## <span style="color:blue">Advanced Features</span>
### <span style="color:green">Custom Commands and Targets</span>
- <span style="color:darkorange">Execute additional tasks during the build process.</span>

### <span style="color:green">Testing Support</span>
- <span style="color:darkorange">**enable_testing()** and **add_test()** for project tests.</span>

### <span style="color:green">Exporting Builds</span>
- <span style="color:darkorange">Allows other projects to easily use the library.</span>

## <span style="color:blue">Toolchain Files</span>
- <span style="color:green">Specify compiler and tool options for cross-compiling.</span>

## <span style="color:blue">CMake Variables</span>
- <span style="color:green">Predefined and user-defined for customization.</span>

## <span style="color:blue">Caching</span>
- <span style="color:green">Stores options and settings to speed up reconfiguration.</span>

## <span style="color:blue">Cross-Platform Builds</span>
- <span style="color:green">Simplify building on multiple operating systems.</span>

## <span style="color:blue">Tips</span>
### <span style="color:green">Use CMake GUI</span>
- <span style="color:darkorange">For easier configuration and generation.</span>

### <span style="color:green">Documentation</span>
- <span style="color:darkorange">Refer to official documentation for detailed options and commands.</span>

## <span style="color:blue">Tools & Integration</span>
### <span style="color:green">IDE Support</span>
- <span style="color:darkorange">Integrated support in popular IDEs for easier development.</span>

### <span style="color:green">CTest for Testing</span>
- <span style="color:darkorange">Built-in test management tool.</span>

## <span style="color:blue">Performance Optimization</span>
- <span style="color:green">Techniques to speed up build times and manage dependencies efficiently.</span>

---

# <span style="color:blue">C++23 Multi-threading and Parallel Programming Overview</span>

## <span style="color:green">Concurrency</span>
- <span style="color:darkorange">**Definition**: Ability of a program to handle more than one task at the same time.</span>
  - <span style="color:purple">**Program Structure**: Manage how a program executes tasks concurrently.</span>
  - <span style="color:darkorange">**Dealing with Multiple Things**: Enhance responsiveness by handling various operations simultaneously.</span>

## <span style="color:green">Parallelism</span>
- <span style="color:darkorange">**Definition**: Execution of multiple calculations or execution processes simultaneously.</span>
  - <span style="color:purple">**Simultaneous Execution**: Improve application performance by running tasks in parallel.</span>

## <span style="color:green">Context Switch</span>
- <span style="color:darkorange">**Definition**: Mechanism to switch between different tasks or threads.</span>
  - <span style="color:purple">**Saving and Loading State**: Save the state of a current task and load a new one to efficiently manage multiple tasks.</span>

## <span style="color:green">Thread Management</span>
- <span style="color:darkorange">**Basic Operations**</span>
  - <span style="color:purple">**join()**: Ensures a thread finishes before the main program continues.</span>
  - <span style="color:darkorange">**detach()**: Allows a thread to operate independently of the main program flow.</span>
- <span style="color:green">**Thread IDs and Process IDs**</span>

## <span style="color:green">Synchronization Primitives</span>
- <span style="color:darkorange">**Mutexes and Locks**</span>
  - <span style="color:purple">**std::mutex**: Prevents simultaneous access to shared resources.</span>
  - <span style="color:darkorange">**std::recursive_mutex**, **std::shared_mutex**: Allows locks to be applied in a hierarchical manner.</span>
- <span style="color:green">**Atomic Operations**</span>
  - <span style="color:purple">**std::atomic**: Ensures operations are performed without interference from other threads.</span>
- <span style="color:green">**Condition Variables and Semaphores**</span>
  - <span style="color:purple">**std::condition_variable**: Coordinates the execution sequence between threads.</span>
  - <span style="color:darkorange">**Semaphores (Counting and Binary)**: Manages access to resources by multiple threads.</span>

## <span style="color:green">Deadlocks and Livelocks</span>
- <span style="color:darkorange">**Handling and Avoidance**</span>
  - <span style="color:purple">**Deadlock**: Condition where two or more threads are waiting on each other to release resources.</span>
  - <span style="color:darkorange">**Livelock**: Threads continuously change states in response to each other without making progress.</span>

## <span style="color:green">Performance Metrics</span>
- <span style="color:darkorange">**Efficiency Measures**</span>
  - <span style="color:purple">**Speedup and Efficiency**: Calculations that measure the improvement in performance when using parallel processing.</span>
  - <span style="color:darkorange">**Amdahl's Law**: Theoretical prediction of the possible speedup of program processing.</span>

## <span style="color:green">Design Patterns for Parallelism</span>
- <span style="color:darkorange">**Thread Pool and Futures**</span>
  - <span style="color:purple">**Thread Pool**: Reuses a number of threads for various tasks.</span>
  - <span style="color:darkorange">**Future and Promise**: Manages asynchronous operations and their results.</span>
- <span style="color:green">**Computational Graphs**</span>
  - <span style="color:purple">**DAG (Directed Acyclic Graph)**: Manages task dependencies and execution order.</span>

## <span style="color:green">Communication and Decomposition</span>
- <span style="color:darkorange">**Types and Strategies**</span>
  - <span style="color:purple">**Domain and Functional Decomposition**: Techniques for dividing tasks and data among processors.</span>
  - <span style="color:darkorange">**Communication**: Managing data flow between tasks, either synchronously or asynchronously.</span>

## <span style="color:green">Key Terms</span>
- <span style="color:darkorange">**Process ID, Thread ID**</span>
- <span style="color:purple">**Concurrency**: Ability of a program to be broken into parts that can run independently of each other.</span>
- <span style="color:darkorange">**Parallelism**: Simultaneous execution of tasks.</span>
- <span style="color:purple">**Context Switch**: Storing and loading the state of a process or thread.</span>
- <span style="color:darkorange">**join()**, **detach()**</span>
- <span style="color:purple">**Mutexes**: std::mutex, std::recursive_mutex, std::shared_mutex</span>
- <span style="color:darkorange">**Atomic Operations**: std::atomic</span>
- <span style="color:purple">**Condition Variables**: std::condition_variable</span>
- <span style="color:darkorange">**Semaphores**: std::counting_semaphore, std::binary_semaphore</span>
- <span style="color:purple">**Deadlock, Livelock**: Lock ordering, scoped_lock, this_thread::yield</span>
- <span style="color:darkorange">**Computational Graph**: DAG</span>
- <span style="color:purple">**Thread Pool**, **Future**</span>
- <span style="color:darkorange">**Speedup, Latency, Throughput**</span>
- <span style="color:purple">**Amdahl's Law**: Impact of multiple CPUs on speedup</span>
- <span style="color:darkorange">**Partitioning**: Domain and functional decomposition</span>
- <span style="color:purple">**Communication**: Point-to-point, collective, synchronous, asynchronous</span>
- <span style="color:darkorange">**Agglomeration, Granularity**: Fine-grained, coarse-grained</span>
- <span style="color:purple">**Mapping**</span>
