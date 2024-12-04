import json
from cryptography.fernet import Fernet
def decrypt_location(indices, words_file):
    """
    Decrypt the location using indices and the UCEnglish.txt file.

    Args:
        indices (list of str): List of indices to decrypt.
        words_file (str): Path to the UCEnglish.txt file.

    Returns:
        str: The decrypted location.
    """
    try:
        # Load words from UCEnglish.txt
        with open(words_file, 'r') as file:
            words = file.read().splitlines()
        
        # Validate indices
        max_index = len(words)
        for index in indices:
            if not index.isdigit() or int(index) < 1 or int(index) > max_index:
                raise ValueError(f"Index {index} is out of bounds for the UCEnglish.txt file.")
        
        # Decrypt location using the provided indices
        decrypted_location = ' '.join([words[int(index) - 1] for index in indices])  # Adjust for 1-based indexing
        
        return decrypted_location
    except FileNotFoundError:
        return "Error: UCEnglish.txt file not found. Check the file path."
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def decrypt_movie_title(encrypted_file, key):
    """
    Decrypt the movie title using the Fernet encryption method.
    
    :param encrypted_file: Path to the file containing the encrypted message.
    :param key: The decryption key provided (Fernet format).
    :return: The decrypted movie title.
    """
    try:
        # Load the encrypted movie title (Assuming it's in JSON format)
        with open(encrypted_file, 'r') as file:
            encrypted_data = json.load(file)
        
        # Example: Assuming the movie title is stored under the key 'encrypted_movie'
        encrypted_message = encrypted_data.get('encrypted_movie')
        if not encrypted_message:
            return "Error: Movie title not found in the file."

        # Initialize the Fernet object with the provided key
        fernet = Fernet(key)
        
        # Decrypt the message
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()

        return decrypted_message
    except FileNotFoundError as e:
        return f"Error: File not found - {e}"
    except json.JSONDecodeError as e:
        return f"Error: JSON decoding error - {e}"
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    # File path for location decryption
    words_file = 'data/UCEnglish.txt'  # Path to UCEnglish.txt
    
    # Indices for "BeautifulPuppy"
    indices = ["30942", "46342", "42061", "103568", "5040", "41700", "31066"]
    
    # Decrypt the location
    decrypted_location = decrypt_location(indices, words_file)
    print(f"Decrypted Location: {decrypted_location}")
    
    # File path for encrypted movie title
    encrypted_file = 'data/TeamsAndEncryptedMessagesForDistribution.json'  # Path to the encrypted movie file
    decryption_key = 'your-fernet-key-here'  # Replace with the actual Fernet key
    
    # Decrypt the movie title
    movie_title = decrypt_movie_title(encrypted_file, decryption_key)
    print(f"Decrypted Movie Title: {movie_title}")
