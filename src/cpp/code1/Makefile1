TARGET = ./main
SRCS := $(wildcard ./src/*.cpp ./*.cpp)
OBJS := $(patsubst %cpp,%o,$(SRCS))
CFLG = -g -Wall -I/usr/local/Cellar/opencv/4.7.0_1/include/opencv4 -Iinc -I./ -std=c++17
LDFG = -Wl, $(shell pkg-config opencv --cflags --libs)
CXX = g++
$(TARGET) : $(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LDFG)
%.o:%.cpp
	$(CXX) $(CFLG) -c $< -o $@ 
clean:
	-rm ./*.o