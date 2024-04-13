
/*
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


*/