"""
  This function takes the lengths of the three sides of a triangle
  Calculate the area of a triangle using Heron's formula.
"""

def area_triangle_Heron(a, b, c) -> float: 
    s = (a + b + c) / 2

    """    Parameters:
    a : Length of the first side of the triangle.
    b : Length of the second side of the triangle.
    c : Length of the third side of the triangle """

    area_squared = s*(s-a)*(s-b)*(s-c)
    area = area_squared ** 0.5

    """ Returns:
    Calculated area of the triangle """

    return area

print(area_triangle_Heron(5, 6, 7))


