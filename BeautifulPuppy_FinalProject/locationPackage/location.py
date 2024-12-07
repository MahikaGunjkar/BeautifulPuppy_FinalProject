
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