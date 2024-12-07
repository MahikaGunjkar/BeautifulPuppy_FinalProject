# Name: Mahika Gunjkar, Nandini Agarwal, Ishani Roy Choudhary, Cheikh Abdoul
# email:  gunjkamg@mail.uc.edu, agarwand@mail.uc.edu, roychoii@mail.uc.edu, abdoulch@mail.uc.edu
# Assignment Number: Final Assignment
# Due Date:  12/10/2024
# Course #/Section:  IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  We worked on extracting and ecoding our image location and movie through decrypted json files. We also used PIL to add images to our python file

# Brief Description of what this module does. This module groupimage.py handles the display of an image file. 
                                                # It uses the Pillow (PIL) library to open and display the image. 
                                               # If the image file is missing or an error occurs, the module provides an appropriate error message.
# Citations:
# Anything else that's relevant:

# Image.py

from PIL import Image

def display_photo(photo_path):
    """
    Displays the photo taken at the decrypted location.

    Args:
        photo_path (str): Path to the photo file.
    """
    try:
        image = Image.open(photo_path)
        image.show()
    except FileNotFoundError:
        print(f"Error: Photo not found at {photo_path}.")
    except Exception as e:
        print(f"Error displaying photo: {e}")

