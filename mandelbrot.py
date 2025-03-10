
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

