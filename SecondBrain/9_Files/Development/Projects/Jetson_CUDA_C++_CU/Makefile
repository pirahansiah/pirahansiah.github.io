farshid: 
	nvcc -std=c++11 -o f farshid.cu $(pkg-config --cflags --libs opencv4) 

# Compiler
NVCC = nvcc

# Compiler flags
# CFLAGS = -std=c++11 \
#          -I/usr/include/opencv4/opencv \
#          -I/usr/include/opencv4 \
#          -lopencv_dnn -lopencv_gapi -lopencv_highgui -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_stitching -lopencv_video -lopencv_calib3d -lopencv_features2d -lopencv_flann -lopencv_videoio -lopencv_imgcodecs -lopencv_imgproc -lopencv_core


# Target executable
TARGET = farshid

# Source file
SRC = farshid.cu

# Default target
all: $(TARGET)
	./$(TARGET) # This line will run the program after it is built

# Compilation rule
$(TARGET): $(SRC)
	$(NVCC) $(CFLAGS) -o $@ $<

# Clean rule
clean:
	rm -f $(TARGET)

.PHONY: all clean
