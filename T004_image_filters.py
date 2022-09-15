# Milestone 3 - P5
# Group: T004
# Date of Submission: 04 / 09 / 2021
# Authors: Hashanpreet Noah Staudte 101189750 | Singh Dhaliwal 101187722 | Jason Zhang 101191526 | Dereck Guay 101126382
# Description: Filters of all milestones.

# Import Statements
from Cimpl import *
import numpy

# Function Definitions

# Red Channel
def red_channel(image: Image) -> Image:
    """ 
    Author: Jason Zhang
    Student ID: 101191526

    Return image with removal of green and blue RGB components
    
    >>> image = load_image(choose_file())
    >>> red_image = red_channel(image)
    >>> show(red_image)
    """
    
    filtered_image = copy(image) # A copy of the image will be used for maniuplation 
    for i in iter(image): # identify every pixel (i) in the image
        x,y,(r,g,b) = i # identify the location and rgb components the pixel (i)
        red=create_color(r,0,0) # remove the green and blue components of each pixel (i)
        set_color(filtered_image,x,y,red) # set each pixel color in the filtered image to "red"
        
    return filtered_image

# Green Channel
def green_channel(Image) -> Image:
    """ 
    Author: Hashanpreet Singh Dhaliwal
    Student ID: 101187722

    Returns the copy of the Image with red and blue rgb components removed
    and keeping only the green rbg value.
        
    >>> image = load_image(choose_file())
    >>> green_image = green_channel(image)
    >>> show(green_image)
    """
    new_image = copy(Image) # A copy of the original image will be created.
    for pixel in Image:
        x,y,(r,g,b) = pixel
        green_color = create_color(0,g,0)
        set_color(new_image,x,y,green_color) # set the color of new_image at x,y points to green.
    
    return new_image

# Blue Channel
def blue_channel (image):
    """ 
    Author: Noah Staudte
    Student ID: 101189750

    (Cimpl.Image) -> Cimpl.Image
    
    Returns a copy of an image, keeping only the blue rgb values, 
    while removing the red and green ones.
    """
    new_image = copy(image)
    
    for pixel in image:
        x,y, (r,g,b) = pixel
        new_color = create_color(0,0,b)
        set_color(new_image, x, y, new_color)    
    
    return new_image

# Extreme Contrast Filter Function
def extreme_contrast(Image)-> Image:
    """ 
    Author: Hashanpreet Singh Dhaliwal
    Student ID: 101187722

    Returns a copy of an image in which the contrast between the pixels has 
    been maximized.
    >>> image = load_image(choose_file())
    >>> contrast_image = extreme_contrast(image)
    >>> show(contrast_image)
    """
    new_image = copy(Image) # A copy of the Image is created
    
    for pixel in Image:
        x,y,(r,g,b) = pixel
        
        if  r <= 127:         # conditon for checking components value.
            r = 0
        elif r <= 255:
            r = 255
        if  g <= 127:
            g = 0
        elif g <= 255:
            g = 255
        if b <= 127:
            b = 0
        elif b <= 255:
            b = 255
        new_color = create_color(r,g,b)
        set_color(new_image,x,y,new_color) # sets the colour of new_image at x,y pixels to new component values.
        
    return new_image

# Three Tones Filter Function
def three_tone(image: Image, color1: str, color2: str, color3: str) -> Image:
  """
  Author: Noah Staudte
  Student ID: 101189750

  Applies a three_tone filter to an image, composed of color1, color2, and color3.
  Three_tone expects color1, color2, & color3 to be one of the following parameters:
      "black", "white", "blood", "green", "blue", "lemon", "aqua", "pink", or "gray".
      
  >>> three_tone(load_image("p2-original.png"), "white", "lemon", "aqua")
  <Cimpl.Image object at 0x00...> (image with white, lemon, and aqua colors)
  
  >>> three_tone(load_image("p2-original.png"), "black", "black", "black")
  <Cimpl.Image object at 0x00...> (all-black image)
  """
  
  color_list = { # Assign each color a corresponding color code
    "black": Color(0, 0, 0),
    "white": Color(255, 255, 255),
    "blood": Color(255, 0, 0),
    "green": Color(0, 255, 0),
    "blue": Color(0, 0, 255),
    "lemon": Color(255, 255, 0),
    "aqua": Color(0, 255, 255),
    "pink": Color(255, 0, 255),
    "gray": Color(128, 128, 128),
  }
  
  three_tone_image = copy(image) #Create copy of image to avoid altering original
  
   # According to brightness of each pixel, assign a designated color
  for x, y, (r, g, b) in three_tone_image:
    brightness = (r + g + b) / 3 
    if brightness < 85:
      set_color(three_tone_image, x, y, color_list[color1])
    elif brightness < 171:
      set_color(three_tone_image, x, y, color_list[color2])
    else:
      set_color(three_tone_image, x, y, color_list[color3])
  
  return three_tone_image

# Posterize Filter Functions
def posterize(image: Image) -> Image:
  """
  Author: Dereck Guay
  Student ID: 101126382

  Returns an image where the color components have been set to the midpoint of a quadrant
  Quandrant are defined by dividing the range of RBG color value which is 255.
  These quandrants are: 0 - 63, 64 - 126, 127 - 190, and 191 - 255 inclusive. The midpoint of each quadrant
  is 31, 95, 159, and 223 respectively

  >>> image = load_image(file)
  >>> posterize(image)
  <Cimpl.Image object at 0x0000026FA5078FA0>
  """
  posterized_image = copy(image)

  for x, y, (r, g, b) in posterized_image:
    set_color(posterized_image, x, y, Color(
      _adjust_component(r),
      _adjust_component(g),
      _adjust_component(b)
    ))

  return posterized_image

def _adjust_component(component: int) -> int:
  """
  Author: Dereck Guay
  Student ID: 101126382
  
  Returns the quadrant midpoint in which a component lies and returns the midpoint value of that quadrant.
  When we divide the range 0...255 into four equal-size quadrants, the ranges of the quadrants 
  are 0...63, 64...127, 128...191, and 192...255. 

  The argument "component" is an integer of the Red, Green or Blue component of a color to be ajusted.

  >>> _adjust_component(54)
  31
  >>> _adjust_component(100)
  95
  >>> _adjust_component(127)
  159
  >>> _adjust_component(240)
  223
  """
  if component < 64:
    return 31
  elif component < 128:
    return 95
  elif component < 192:
    return 159
  else:
    return 223

# Sepia Tinting Filter Function
def sepia(image: Image) -> Image:
  """
  Author: Jason Zhang
  Student ID: 101191526

  Returns an image where each pixel is slightly yellow tinted giving the impression that
  the image is old.

  >>> image = load_image(choose_file())
  >>> sepia(image)
  """
  sepia_tinted_image = copy(image)

  for x, y, (r, g, b) in sepia_tinted_image:
    average = (r + g + b) // 3

    new_pixel_color = None
    if average < 63:
      new_pixel_color = Color(average * 1.1, average, average * 0.9)
    elif average < 192:
      new_pixel_color = Color(average * 1.15, average, average * 0.85)
    else:
      new_pixel_color = Color(average * 1.08, average, average * 0.93)

    set_color(sepia_tinted_image, x, y, new_pixel_color)

  return sepia_tinted_image

# Detect Edges Filter Function
def detect_edges(image: Image, threshold: float) -> Image:
    """
    Author: Noah Staudte
    Student ID: 101189750
    
    Returns a copy of an image already loaded by Cimpl, changing each pixel color
    to white if the contrast between itself and the one below it is lower than,
    the threshold, otherwise changing it to black, creating a sketch-like image.
    
    >>>detect_edges(load_image(IMAGE_PATH, 15.0))
    <Cimpl.Image object at 0x00...>
    """
    
    WHITE = create_color(255,255,255)
    BLACK = create_color(0,0,0)    
    
    new_image = copy(image)
    image_width = image.get_width()
    image_height = image.get_height()
    
    for y in range(image_height):
        for x in range(image_width):
            if (y != (image_height - 1)):
                (r1,g1,b1) = new_image.get_color(x,y)
                (r2,g2,b2) = new_image.get_color(x,y+1)
                brightness1 = (r1+g1+b1)/3
                brightness2 = (r2+g2+b2)/3
                
                #debug statement
                #print(brightness1, brightness2, abs(brightness2-brightness1))
                
                if abs(brightness2 - brightness1) > threshold:
                    new_image.set_color(x, y, BLACK)
                else:
                    new_image.set_color(x, y, WHITE)
            else: #Set pixel to white if in last row
                new_image.set_color(x, y, WHITE)    
                
    return new_image

# Draw Curve Filter Functions
def draw_curve(image: Image, color: str = "lemon", point_lst: [(int, int)] = None) -> (Image, [(int, int)]):
  """
  Author: Dereck Guay
  Student ID: 101126382

  Returns a tuple containing an image on which a curve has been drawn has the first element and a list of all the
  points that intersects with the borders of the image.

  The image parameter is the base image (Cimpl.Image class) on which a curve will be drawn.

  The color is a string that matches the colors dictionairy. If the color is "Black" the color used to draw the curve on the
  given image will be Color(0, 0, 0).

  The point_lst is a list that can be passed to the function or None. If none the function will ask the user to enter a list of points
  for which a polynomial interpolation or least squares interpolation coefficients will be calculated to draw the curve on the image.

  >>> image = load_image(choose_file())
  >>> draw_curve(image, "lemon", [(0, 380), (250, 500), (500, 1000), (750, 500), (1000, 380)])
  <Cimpl.Image object at 0x0000025B119B59D0>

  >>> image = load_image(choose_file())
  >>> draw_curve(image, "blood")
  <Cimpl.Image object at 0x0000025B119B59D0>

  Show the resulting image with curve:
  >>> image = load_image(choose_file())
  >>> image_with_curve = draw_curve(image, "blood")
  >>> show(image_with_curve)
  """
  # Recongnized colors
  colors = {
    "black": Color(0, 0, 0),
    "white": Color(255, 255, 255),
    "blood": Color(255, 0, 0),
    "green": Color(0, 255, 0),
    "blue": Color(0, 0, 255),
    "lemon": Color(255, 255, 0),
    "aqua": Color(0, 255, 255),
    "pink": Color(255, 0, 255),
    "gray": Color(128, 128, 128)
  }

  width = get_width(image)
  height = get_height(image)

  # If not passed, prompt user for point_lst
  if not point_lst:
    print("The Image is {0}px wide and {1}px high.".format(width, height))
    point_lst = _get_user_point_list()

  # Calculate the coefficients and border intersects.
  coefficients = _interpolation(point_lst)
  curve_border_cross_points = _image_border_finding((width, height), coefficients)

  new_image = copy(image)

  # Draws the curve 
  for x in range(width - 1):
    y = _evaluate(x, coefficients)
    if y < height: # Makes sure to draw only the curve parts that are on the image
      y = height - y # Set the bottom left pixel as (0, 0) 
      # Draws a square of +- 2 around the pixel for the line thickness
      for i in range(-4, 5, 1):
        for j in range(-4, 5, 1):
          pixel_x = int(x + i)
          pixel_y = y + j
          # Check if pixel is in the image
          if pixel_x < width and pixel_x >= 0 and pixel_y < height and pixel_y >= 0:
            set_color(new_image, pixel_x, pixel_y, colors[color])

  return (new_image, curve_border_cross_points)

def _get_user_point_list() -> [(int, int)]:
  """ 
  Author: Dereck Guay
  Student ID: 101126382

  Asks the user how many points will be used to draw a curve on the image. Then the user is prompt to enter
  each individual components for each points.

  Return a sorted set of integer points entered by the user as inputs.

  >>> _get_user_point_list()
  How many points (There should be at least 2 points to properly draw a curve on the image): 3
  Point 1 | X = 4
  Point 1 | Y = -1
  ---------------
  Point 2 | X = 2
  Point 2 | Y = 0
  ---------------
  Point 3 | X = 3
  Point 3 | Y = 10
  ---------------
  [(2, 0), (3, 10), (4, -1)]
  """
  num_points = int(input("How many points (There should be at least 2 points to properly draw a curve on the image): "))

  point_lst = []
  for i in range(1, num_points + 1):
    x = int(input("Point {0} | X = ".format(i)))
    y = int(input("Point {0} | Y = ".format(i)))
    print("---------------")
    point_lst.append((x, y))
    
  point_lst.sort()

  return point_lst

def _interpolation(point_lst: [(int, int)]) -> [float]:
  """ 
  Author: Dereck Guay
  Student ID: 101126382
  
  Returns a list of coefficients of an interpolation polynomial thats fits the list of given points .

  The list of coefficients in the example below would represent: 1 * x**2 - 5 * x + 8.
  The length of the list returned minus one reprensents the degree of the interpolation polynomial.

  >>> _interpolation([(1, 4), (3, 2), (5, 8)])
  [1. -5.  8.]

  >>> _interpolation([(2, 0), (40, 10), (50, 15), (100, 31)])
  [-0.1031746   1.49206349 -4.75396825  7.36507937]
  """
  if len(point_lst) <= 2: 
    # # 2 or 3 points:
    # Linear Interpolation
    x_values_matrix = []
    y_values_vector = []
    for (x, y) in point_lst:
      x_values_row = []
      for i in range(len(point_lst) - 1, -1, -1):
        x_values_row.append(x**i)
      x_values_matrix.append(x_values_row)
      y_values_vector.append(y)
    numpy_coefficients = numpy.linalg.solve(x_values_matrix, y_values_vector)
  else:
    # More than 3 points: 
    # Regression (Least Squares Fit Quadratic)
    pixels_x = []
    pixels_y = []
    for (x, y) in point_lst:
      pixels_x.append(x)
      pixels_y.append(y)
    numpy_coefficients = numpy.polyfit(pixels_x, pixels_y, 2)

  # Numpy returns type Float64 coefficients, for testing changing it back to Float
  coefficients_float = []
  for coefficient in numpy_coefficients:
    coefficients_float.append(float(coefficient))

  return coefficients_float    

def _image_border_finding(image_size: (int, int), coefficients: [float]) -> [(int, int)]:
  """ 
  Author: Dereck Guay
  Student ID: 101126382
  
  Returns the points where the the curve defined by the coefficients parameter crosses the vertical
  and horizontal borders of the image.

  >>> _image_border_finding((1000, 1000), [1.09375000e-05 -1.83593750e-02  7.94140625e+00 -1.02539063e+02])
  [(999, 412)]

  >>> _image_border_finding((1000, 1000), [-3.04922893e-21 -2.77777778e-03  2.77777778e+00  1.18055556e+02])
  [(0, 118), (999, 120)]

  >>> _image_border_finding((1000, 1000), [ 1.40625000e-05 -2.28906250e-02  9.49609375e+00 -1.69335938e+02])
  [(999, 492), (759, 0), (260, 999)]
  """
  curve_border_cross_points = []

  # Horizontal Borders
  for x in [0, image_size[1] - 1]:
    y = _evaluate(x, coefficients)
    if y < image_size[0] and y > 0: # Crosses only if in the actual y range of the image.
      curve_border_cross_points.append((x, y))

  # Vertical Borders
  # Only finds one point.
  for y in [0, image_size[0] - 1]:
    x = _exhaustive_search(image_size[0] - 1, coefficients, y)
    if x != None:
      curve_border_cross_points.append((x, y))

  return curve_border_cross_points
  
def _evaluate(x: float, coefficients: [float]) -> int:
  """ 
  Author: Dereck Guay
  Student ID: 101126382
  
  Returns the y integer value at a given x value of the curve defined by the coefficients parameter.

  >>> _evaluate(0, [1., -5., 8.])
  8

  >>> _evaluate(49, [1., -5., 8.])
  2164
  """
  y_value = 0
  for i in range(len(coefficients) - 1, 0, -1):
    y_value += coefficients[-i - 1] * x**i
  return int(y_value + coefficients[-1])

def _exhaustive_search(max_x: int, coefficients: [float], val: int) -> int:
  """ 
  Author: Dereck Guay
  Student ID: 101126382
  
  Solves f(x)-val=0 for x between 0 and max_x where coefficients contains the coefficients of f,
  using EPSILON of 1 (as we only need ints for pixels).  Returns None if there is no solution between the bounds.

  >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
  253
  
  >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
  590
  
  >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
  None
  """
  EPSILON = 0.5
  guess = 0
  func_sol = _evaluate(guess, coefficients)
  while abs(func_sol - val) >= EPSILON and guess <= max_x:
    guess += EPSILON
    func_sol = _evaluate(guess, coefficients)

  if guess < max_x:
    return int(guess)
  return None

# Horizontal Flipping Filter Function
def flip_horizontal(Image) ->Image:
    """ 
    Author: Hashanpreet Singh Dhaliwal
    Student ID: 101187722
    
    Returns a copy of flipped Image.
    
    >>> image = load_image(choose_file())
    >>> flipped = flip_horizontal(image)
    >>> show(flipped)
    """
    new_image = copy(Image)           # A copy of Image is created.
    width = new_image.get_width()     # used to get the width of new_image.
    height = new_image.get_height()   # used to get the height of new_image.
                           # displays the original image.
    for y in range(height):           # iterates over ecah pixel in the height.
        for x in range(width):        # iterates over each pixel in the width.
            new_wid = width-(x+1)     # used to get the opposite width pixel.
            new_color = get_color(Image,new_wid,y)  # get the colour of the opposite pixel
            set_color(new_image,x,y,new_color)      # cahnges the colour of original pixel to the opposite pixel.
    
    return new_image

# Vertical Flipping Filter Function
def flip_vertical(image: Image) -> Image:
    """
    Author: Jason Zhang
    Student ID: 101191526

    Returns an image with pixels reflected across the horizontal midline
    
    >>> image = load_image(choose_file())
    >>> flipped_image = flip_vertical(image)
    >>> show(image)
    """
    image_copy = copy(image)
    width = image_copy.get_width() # Get the number of pixels horizontally
    height = image_copy.get_height() # Get the number of pixels vertically
   
    for x in range(width): # iterate through each pixel in the width
        for y in range(height): # iterate through each pixel in the height
            new_y = height-y-1 # identifies the y coordinate of pixel in the flipped image
            new_color = get_color(image,x,new_y) # get the color of the new pixel
            set_color(image_copy,x,y,new_color) # set the color of the new pixel to the original pixel
                 
    return image_copy

# Main Script
if __name__ == "__main__":
  image = load_image(choose_file())

  # P3 Filters
  contrast_image = extreme_contrast(image)
  show(contrast_image)

  three_tone_image = three_tone(image, "black", "blood", "aqua") 
  show(three_tone_image)

  posterized_image = posterize(image)
  show(posterized_image)

  sepia_tinted_image = sepia(image)
  show(sepia_tinted_image)

  # P4 Filters
  edge_image = detect_edges(image, 15.0)
  show(edge_image)  

  image_curve = create_image(1000, 1000, Color(0, 0, 0))
  (image_with_curve, curve_border_intersecting_points) = draw_curve(image_curve, "aqua", [(50, 250), (600, 700),(950, 100)])
  print(curve_border_intersecting_points)
  show(image_with_curve)

  flipped_image = flip_horizontal(image)
  show(flipped_image) 

  vertically_flipped_image = flip_vertical(image)
  show(vertically_flipped_image)

  print("Program executed successfully.")