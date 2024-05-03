#############################################################################################
# Usage:                                                                                    #
#     This script creates an ASCII art box to prepend to the top of source files,           #
#     providing an elaboration on the functionality of the program.                         #
#                                                                                           #
# How to use:                                                                               #
#     Argument 1: 'Infile' -> .txt file that you want the box around                        #
#     Argument 2: 'Outfile' -> name of the file you want the decorated box to be written to #
#                                                                                           #
#     Note: Doesn't support write to a specific directory.                                  #
#           Assumes the input and output files will be in the same directory as main.py     #
#                                                                                           #
# Example:                                                                                  #
#     python3 main.py example.txt dec.txt                                                   #
#############################################################################################

import sys

def decorate_content(content):
    decorated_content = ""
    lines = content.split("\n")
    max_length = max(len(line) for line in lines)
    
    # Top Line
    decorated_content += "#" * (max_length + 4) + "\n"

    # Everything in-between
    for line in lines:
        decorated_content += "# " + line + " " * (max_length - len(line)) + " #\n"
    
    # Bottom Line
    decorated_content += "#" * (max_length + 4) + "\n"

    return decorated_content

def decorate_file(infile, outfile):
    try:
        with open(infile, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'Error: File Path -> Infile')
    
    decorated_content = decorate_content(content)

    with open(outfile, 'w') as file:
        file.write(decorated_content)

if __name__ == "__main__":
    decorate_file(sys.argv[1], sys.argv[2])
