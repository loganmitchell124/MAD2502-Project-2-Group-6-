import numpy as np
#   PART !
def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """
    author: Logan Mitchell
    param c: complex number
    param max_iterations: int number
    return: iterations or none
    determines the amount of iterations it takes for a complex number to escape under the Mandelbrot iteration
    """
    z_val = 0
    for i in range(max_iterations+1): #loops through max iterations (+1 so it accounts for every value)
        z_val = z_val * z_val + c #iteration formula
        if abs(z_val) > 2: #check magnitude
            return i #return iterations before escaping
    return None #if no escape, return none

#PART 2
def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
    """
        Author: Santiago Otoya
        This function will compute a grid of complex numbers representing a grid for the Mandelbrot set
        Params:
           top_left: The top left corner of the grid
           bottom_right: The bottom right corner of the grid
           step: The step size of the grid
        Return: np.ndarray
    """
    #Using bounds for real and imaginary values and generating their values
    real_vals = np.arange(top_left.real, bottom_right.real, step)
    imag_vals = np.arange(top_left.imag, bottom_right.imag, -step)

    #Creating the 2d grid for each
    grid_real_vals = np.meshgrid(real_vals, imag_vals)[0]
    grid_imag_vals = np.meshgrid(real_vals, imag_vals)[1]

    #Creating final complex grid by combining both grids
    final_complex_grid = 1j * grid_imag_vals + grid_real_vals

    return final_complex_grid

#PART 3
def get_escape_time_color_arr(
    c_arr: np.ndarray,
    max_iterations: int
    ) -> np.ndarray:
    """
    Author: Logan Mitchell
    param: c_arr (np.array)
    param max_iterations: (int)
    return: a value that normalizes the greyscale
    initializes an array, checks for points that have escaped, then returns
    the normalized greyscale, which can be used to plot a mandelbrot set
    """
    #initialize arrays that we will alter below based on escape times
    z = np.copy(c_arr)
    escape_time = np.empty(c_arr.shape, dtype=int)
    escape_time.fill(max_iterations + 1)
    #remaining = points that have not escaped
    remaining = np.ones(c_arr.shape, dtype=bool)
    #checks and records value that are escaping
    for i in range(1, max_iterations + 1):
        z[remaining] = z[remaining] * z[remaining] + c_arr[remaining]
        escaped_points = np.abs(z) > 2
        escape_time[escaped_points & remaining] = i
        remaining[escaped_points] = False

    return (max_iterations - escape_time + 1) / (max_iterations + 1)

#PART 4
def get_julia_color_arr(
        c_arr: np.ndarray,
        c: complex,
        max_iterations: int
) -> np.ndarray:
    """
    Author: Timothy Streetman
    param: c_arr (np.array)
    param: c (complex)
    param max_iterations: (int)
    return: a julia set that can be plotted visually
    """
    z = np.copy(c_arr) #get complex grid
    julia = np.empty(c_arr.shape, dtype=int)
    julia.fill(max_iterations + 1)
    remaining = np.ones(c_arr.shape, dtype=bool) #boolean for which ones havent escaped
    for i in range(1, max_iterations + 1): #iterate tgrough escape time calculations
        z[remaining] = z[remaining] * z[remaining] + c
        escaped_points = np.abs(z) > 2
        julia[escaped_points & remaining] = i
        remaining[escaped_points] = False

    return (max_iterations - julia + 1) / (max_iterations + 1)
