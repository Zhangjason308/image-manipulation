CONTACT INFORMATION
---------------------------------------------------------------------
Name: Jason Zhang (101191526)
Team: T004
Phone: +1 (613)-981-2838
Website: carleton.ca
Email: jasonzhang9@cmail.carleton.ca

SOFTWARE INFORMATION
---------------------------------------------------------------------
Date: 04 / 10 / 2021

Image Manipulation Software(R) version 1.0

Description:
  This program contains two different user interfaces one text-based, and one batch-based.
  These user interfaces contain a multitude of colourful filters that can be applied to a
  selected image. Multiple filters can be applied to the same image.

INSTALLATION
---------------------------------------------------------------------
1.  First, a version of Python is needed to run this program. To download Python,
    Head over to https://www.python.org/ and click on downloads scroll to the
    bottom of the page and find the installer that fits your current operating 
    system (e.q. Windows installer (64-bit)).

2.  Next, the program requires 2 libraries: Pillow, and Cimpl. Cimpl will be included
    with the download of the software. To download Pillow, open the command prompt, or
    terminal on macOS or Linux, and type: "pip install Pillow".

3.  You know have all you need to run the program successfully. 


GENERAL USAGE NOTES
---------------------------------------------------------------------

Interactive Text-Based UI:
  1.  Double click on "T004_interactive_ui.py" Python file to start the program
  
  2.  You'll see a menu inside the terminal or command prompt looking like this:
        L)oad image S)ave-as X)treme contrast 3)-tone P)osterize T)int sepia E)dge detect D)raw curve 
        V)ertical flip H)orizontal flip Q)ui
  
  3. To manipulate an image you first have to load an image by typing in the "l" command.
  
  4.  Once loaded, you can manipulate the image by applying filter with every command
      except for "l", "s", and "q".
  
  5. Once the image has been filtered. You can save the image with "s".
  
  6. You can also quit the program by typing the "q" command or just closing the terminal.

Batch-Based UI:
  1.  First, make sure to create a txt file containing your manipulations.

  2.  Run the program by double clicking on the "T004_batch_ui.py" Python file.

  3. The program will ask you for a batch file containing the manipulations.

  4. Make sure the images to be manipulated are in the same folder as the program.

  5. In your manipulation text file. The format is the following:
      IMAGE_NAME.EXTENSION SAVE_IMAGE_NAME.EXTENSION FILTER1 FILTER2 FILTER3
    
    A given batch_sample file will be provided for better understanding.

CREDITS
---------------------------------------------------------------------

Bellow is a list of all the developed components of this software and its developer:
Jason Zhang 101191526:
  * Interactive Text-Based UI
  * red_channel filter
  * sepia tinting filter
  * flip_vertical filter
  * test_three_tone test
  * test_detect_edges test

Noah Staudte 101189750:
  * Batch-Based UI
  * blue_channel filter
  * three_tone filter
  * detect_edges filter
  * test_sepia test
  * test_flip_vertical test

Hashanpreet Singh Dhaliwal 101187722:
  * Batch-Based UI
  * green_channel filter
  * extreme_contrast filter
  * flip_horizontal filter
  * test_adjust_component test
  * test_posterize test
  * test_draw_curve test
  * test_get_user_point_list test
  * test_interpolation test
  * test_image_border_finding test
  * test_evaluate test
  * test_exhaustive_search test

Dereck Guay 101126382
  * Interactive Text-Based UI
  * posterize filter
  * _adjust_component function
  * draw_curve filter
  * _get_user_point_list function
  * _interpolation function
  * _image_border_finding function
  * _evaluate function
  * _exhaustive_search function
  * test_extreme_contrast test
  * test_flip_horizontal test

LICENSE
---------------------------------------------------------------------
Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
