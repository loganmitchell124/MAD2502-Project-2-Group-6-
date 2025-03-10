
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

print(get_escape_time(2+1j, 5))
print(get_escape_time(1+1j, 10))
print(get_escape_time(0.5+0.5j, 3))
print(get_escape_time(0.5+0.5j, 4))
print(get_escape_time(0.38+0.25j, 100))

#outputs: 0, 1 , none, ****none****, 56

def get_complex_grid(top_left: complex, bottom_right: complex, step: float
) -> np.ndarray:
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
