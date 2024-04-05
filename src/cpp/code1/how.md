cmake -DCMAKE_PREFIX_PATH=/Users/farshid/farshid/2024/libtorch ..
 cmake --build . --config Release       ||  make


rm -rf *     
export DYLD_LIBRARY_PATH=/Users/farshid/farshid/2024/libtorch/lib:$DYLD_LIBRARY_PATH

xattr -dr com.apple.quarantine /Users/farshid/farshid/2024/libtorch
