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

