#########################################################
# Usage:                                                #
#   Converts all jpgs in a directory to pngs            #
#                                                       #
# How to use:                                           #
#   Argument 1: Folder path containing all the jpgs     #
#   Argument 2: Folder path to place all pngs           #
#       Note: Relative to jpg_to_png.py path            #
#                                                       #
#   Example:                                            #
#       python3 jpg_to_png.py Pokedex/ Pokedex_PNG/     #
#                                                       #
#########################################################

from PIL import Image
import sys
import os

def main(jpg_folder_path, png_folder_path) -> None:
    # Compress a list of all the images in the jpg_folder
    jpg_images = os.listdir(jpg_folder_path)

    if(len(jpg_images) == 0):
        print("jpg folder path is empty")
        return None

    for image in jpg_images:
        image_name, *others, im_format = image.split('.')

        if(im_format == 'jpg'):
            try:
                with Image.open(jpg_folder_path + image) as curr_image:
                    curr_image.save(png_folder_path + image_name + '.png', 'png')

            except FileNotFoundError:
                print(f"Can't find image: {image}")
            
            except Exception:
                print(f"Skipping image: {image}")
        
        # Skips non-jpg files
        else:
            print(f"Skipping file: {image}")


if __name__ == '__main__':
    # User didn't pass right args in CLI
    if len(sys.argv) != 3:
        print(f"Usage Error: <path_to_images> <path_to_deposit_png_dir>")

    else:
        *others, jpg_folder_path, png_folder_path = sys.argv[1], sys.argv[2]
        
        # Standardizes arguments
        if not jpg_folder_path.startswith('./'):
            jpg_folder_path = './' + jpg_folder_path

        if not png_folder_path.startswith('./'):
            png_folder_path = './' + png_folder_path

        if not jpg_folder_path.endswith('/'):
            jpg_folder_path += '/'
        
        if not png_folder_path.endswith('/'):
            png_folder_path += '/'

        # Can't find directory with jpgs -> No images to convert
        if(not os.path.exists(jpg_folder_path)):
            print('Path Error: {} does not exist.'.format(jpg_folder_path))

        else:
            # Create PNG dir if not there already
            if(not os.path.exists(png_folder_path)):
                os.makedirs(png_folder_path)

            main(jpg_folder_path, png_folder_path)