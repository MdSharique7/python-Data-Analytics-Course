
#     Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,


def calculate_area1(dim1,dim2,shape="triangle"):
    

    if shape == "triangle":
     area1 = (1/2)*dim1*dim2
    return(area1) 
def calculate_area2(dim1,dim2,shape="rectangle"):

     if shape == "rectangle":
      area2 = dim1*dim2
     else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None 
     return(area2) 

x = calculate_area1(3,6)
y = calculate_area2(3,6)
print(f'Area of tiangle {x} , Area of rectangle {y}')
#     Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,

# rectangle area=length*width

