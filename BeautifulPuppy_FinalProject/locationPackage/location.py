# Name: Mahika Gunjkar, Nandini Agarwal, Ishani Roy Choudhary, Cheikh Abdoul
# email:  gunjkamg@mail.uc.edu, agarwand@mail.uc.edu, roychoii@mail.uc.edu, abdoulch@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  We worked on extracting and ecoding our image location and movie through decrypted json files. We also used PIL to add images to our python file

# Brief Description of what this module does: This is the location.py, it provides a code to decrypt a precise location based on a list of indices and a word list stored in the file UCEnglish.txt
# Citations: used chatgpt for a few functions
# Anything else that's relevant:

# location.py

def decrypt_location(indices, words_file):
    """
    Decrypts the location using indices and the UCEnglish.txt file.

    Args:
        indices (list of str): List of indices to decrypt.
        words_file (str): Path to the UCEnglish.txt file.

    Returns:
        str: The decrypted location.
    """
    try:
        with open(words_file, 'r') as file:
            words = file.read().splitlines()
       
        decrypted_location = ' '.join([words[int(index)] for index in indices if index.isdigit()])
        return decrypted_location
    except FileNotFoundError:
        return "Error: UCEnglish.txt file not found."
    except IndexError as e:
        return f"Error: An index is out of bounds - {e}"
    except Exception as e:
        return f"Error decrypting location: {e}"