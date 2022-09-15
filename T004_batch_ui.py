# Milestone 3 - P5
# Group: T004
# Date of Submission: 04 / 09 / 2021
# Authors: Hashanpreet Singh Dhaliwal 101187722 | Noah Staudte 101189750
# Description: Batch-Based UI for filters

# Import Statements
from T004_image_filters import *

# Function Definitions
def execute_command(command: tuple) -> Image:
    """ 
    Authors: Hashanpreet Singh Dhaliwal 101187722 and Noah Staudte 101189750

    Performs operation of the given command tuple,
    in the form (input_path, output_path, image_function[])
    
    Returns None if the command is not valid.
    """
    INPUT_PATH, OUTPUT_PATH, operations = command
    
    try: 
        image = copy(load_image(INPUT_PATH)) # A copy of origninal image is created.
    except:
        return None  # In case the command is invalid.
    
    
    for image_filter in operations:
        # Get corresponding function from given key (command)
        func = functions.get(image_filter) 
        
        if func == three_tone: # three tone takes additional three parameters.
            image = func(image,"aqua", "blood", "lemon")
        else: 
            try:
                image = func(image) # For functions(posterize, Tint sepia, Extreme contrast)
            except:
                pass #Skip to next iteration if function is invalid
            
    image.write_to(OUTPUT_PATH)
    return Image


def get_command(file: str) -> list:
    """
    Authors: Hashanpreet Singh Dhaliwal 101187722 and Noah Staudte 101189750
    
    Get the commands written in the batch file, and compiles them into a
    list of tuples, in the form of [(input_path, output_path, command_list[])]


    >>> get_command('batch_sample.txt')
    [('miss_sullivan.jpg', 'test1.jpg', ['3', 'X', 'P']), ('miss_sullivan.jpg', 'test2.jpg', ['V', 'T']), ('miss_sullivan.jpg', 'test3.jpg', ['V', 'E', 'H'])]
    """
    infile = open(file, "r")
    commands = [] # empty list
    
    for line in infile: #Add each command to a list of command
        linelist = line.split() #split the string into a list
        commands.append((linelist[0], linelist[1], linelist[2:]))
        
    infile.close()
    return commands    


# Main Script
if __name__ == "__main__":
    #(For ex: enter "batch_user.txt")
    FILE = input("Enter the batch file: ") 

    # Dictionary containing all filter functions.
    functions = {
        '3': three_tone, 
        'X': extreme_contrast, 
        'T': sepia, 
        'P': posterize,
        'E': detect_edges, 
        'V': flip_vertical, 
        'H': flip_horizontal
    } 

    commands = get_command(FILE)

    for command in commands:
        execute_command(command)