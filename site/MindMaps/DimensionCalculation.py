'''
# Summary of notation

If layer l is a convolution layer:

- `f^[l]` = filter size
- `p^[l]` = padding
- `s^[l]` = stride
- `n_c^[l]` = number of filters

Each filter is: `f^[l] x f^[l] x n_c^[l-1]`

Activations: `a^[l]` -> `n_H^[l] x n_W^[l] x n_c^[l]`.

Weights: `f^[l] x f^[l] x n_c^[l-1] x n_c^[l]`

bias: `n_c^[l]` -> `(1, 1, 1, n_c^[l])` # of filters in layer l.

Input: `n_H^[l-1] x n_W^[l-1] x n_c^[l-1]`

Output: `n_H^[l] x n_W^[l] x n_c^[l]`

`n_H^[l] = floor((n_H^[l-1] + 2p^[l] - f^[l]) / s^[l] + 1)`

`n_W^[l] = floor((n_W^[l-1] + 2p^[l] - f^[l]) / s^[l] + 1)`

`A^[l]` -> `m x n_H^[l] x n_W^[l] x n_c^[l]`

`n_c^[l] x n_H^[l] x n_W^[l]`

'''
# Convolution Layer Output Dimension Calculation

# The function `conv_output_shape` calculates the output height and width for a given convolution layer.

# ## Parameters:
# - `h_w`: Tuple (height, width) of the input image.
# - `f`: Filter size.
# - `p`: Padding.
# - `s`: Stride.
# - `n_c`: Number of filters.

# ## Returns:
# - A tuple containing the output dimensions (height, width) of the convolution layer.

# ## Python Function:

# ```python
def conv_output_shape(h_w, f=3, p=0, s=1, n_c=None):
    """
    Function to calculate the dimensions of the output of a convolution layer.
    :param h_w: Tuple (height, width) of the input image.
    :param f: Filter size.
    :param p: Padding.
    :param s: Stride.
    :param n_c: Number of filters.
    :return: Tuple (height, width) representing the output dimensions.
    """
    if n_c is not None:  # if number of filters is provided, print it
        print(f"Number of filters: {n_c}")
    
    # Calculate output height and width
    h = (h_w[0] - f + 2 * p) // s + 1
    w = (h_w[1] - f + 2 * p) // s + 1
    return h, w

# Example input
input_dimensions = (64, 64)  # Height and Width of input image
filter_size = 3
padding = 1
stride = 1
number_of_filters = 32

# Calculate output dimensions
output_dimensions = conv_output_shape(input_dimensions, filter_size, padding, stride, number_of_filters)
print(f"Output dimensions: Height = {output_dimensions[0]}, Width = {output_dimensions[1]}")
