import json
from cryptography.fernet import Fernet

def decrypt_movie_title(team_key, data_file, decryption_key):
    """
    Decrypts the movie title for a specific team.

    Args:
        team_key (str): The team identifier (e.g., 'BeautifulPuppy').
        data_file (str): Path to the JSON data file.
        decryption_key (str): The Fernet decryption key.

    Returns:
        str: The decrypted movie title for the team.
    """
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)

        encrypted_message = data.get(team_key, [None])[0]
        if not encrypted_message:
            return f"Error: No message found for team '{team_key}'."
       
        fernet = Fernet(decryption_key)
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        return decrypted_message
    except FileNotFoundError:
        return "Error: Teams JSON file not found."
    except Exception as e:
        return f"Error decrypting movie title: {e}"




