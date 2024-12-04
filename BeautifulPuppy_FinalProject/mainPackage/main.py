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


# Example usage
if __name__ == "__main__":
    # File path
    words_file = 'data/UCEnglish.txt'
    
    # Indices for "BeautifulPuppy"
    indices = ["30942", "46342", "42061", "103568", "5040", "41700", "31066"]
    
    # Decrypt the location
    decrypted_location = decrypt_location(indices, words_file)
    print(f"Decrypted Location: {decrypted_location}")
