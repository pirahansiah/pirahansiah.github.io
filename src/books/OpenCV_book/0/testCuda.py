import numba.cuda as cuda

# Check if CUDA is available
if cuda.is_available():
    print("CUDA is available.")
    print("CUDA devices:", cuda.list_devices())
else:
    print("CUDA is not available.")
