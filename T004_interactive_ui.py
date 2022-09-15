# Milestone 3 - P5
# Group: T004
# Date of Submission: 04 / 09 / 2021
# Authors: Jason Zhang 101191526 | Dereck Guay 101126382
# Description: Text-Based Interactive UI for filters

# Import statements
from T004_image_filters import *

# Function Definitions
def interactive_user_interface():
  """
  Authors: Dereck Guay 101126382 and Jason Zhang 101191526

  Prompts the user for different image related manipulation utilizing the T004_image_filters module. This function displays
  an interactive user interface to apply filters to a loaded image, and save the filtered image.
  """
  image = None
  command = None
  while True:
    (command, command_function) = get_command()

    # Quit
    if command == "q": break

    # NO IMAGE LOADED
    if command != "l" and image == None:
      print("No image loaded")
    
    # Load Image
    elif command == "l":
      image = load_image(choose_file())
    
    # IMAGE IS LOADED
    # Save image
    elif command == "s":
      save_name = input("Save image as: ")
      save_as(image,  save_name + ".png")
    
    # 3 Tones
    elif command == "3":
      image = command_function(image, "aqua", "blood", "lemon")
    
    # Edge Detection
    elif command == "e":
      image = command_function(image, int(input("Threshold for Edge Detection: ")))
    
    # Draw Curve
    elif command == "d":
      image = command_function(image)[0] # Need only the image.
    
    # Other Filters
    else:
      image = command_function(image)


def get_command():
  """
  Authors: Dereck Guay 101126382 and Jason Zhang 101191526

  Returns a tuple containing a valid user input and the function linked to the string entered by the user.

  >>> get_command()
  L)oad image S)ave-as X)treme contrast 3)-tone P)osterize T)int sepia E)dge detect D)raw curve V)ertical flip H)orizontal flip Q)ui
  Command: l
  ('l', <function load_image at 0x00000274EC867310>)

  >>> get_command()
  L)oad image S)ave-as X)treme contrast 3)-tone P)osterize T)int sepia E)dge detect D)raw curve V)ertical flip H)orizontal flip Q)ui
  Command: l
  ('P', <function posterize at 0x000002A9BC503C10>)

  >>> get_command()
  L)oad image S)ave-as X)treme contrast 3)-tone P)osterize T)int sepia E)dge detect D)raw curve V)ertical flip H)orizontal flip Q)ui
  Command: allo
  No such command.
  L)oad image S)ave-as X)treme contrast 3)-tone P)osterize T)int sepia E)dge detect D)raw curve V)ertical flip H)orizontal flip Q)ui
  Command: x
  ('x', <function extreme_contrast at 0x000002920DE93AF0>)
  """
  commands = {
    "l": load_image,        "s": save_as,
    "e": detect_edges,      "d": draw_curve,
    "v": flip_vertical,     "h": flip_horizontal,
    "x": extreme_contrast,  "3": three_tone,
    "p": posterize,         "t": sepia,
    "q": "quit"
  }

  user_input = None
  command_function = None
  while command_function == None:
    print("L)oad image S)ave-as X)treme contrast 3)-tone P)osterize T)int sepia E)dge detect D)raw curve V)ertical flip H)orizontal flip Q)ui")
    user_input = str.lower(input("Command: "))
    command_function = commands.get(user_input)
    
    # Validates that the command exists.
    if command_function == None:
      print("No such command.")
  
  return (user_input, command_function)

# Maint Script    
if __name__ == "__main__":
  interactive_user_interface()