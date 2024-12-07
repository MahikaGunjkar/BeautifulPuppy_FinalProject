# Name: Mahika Gunjkar, Nandini Agarwal, Ishani Roy Chowdhury, Cheikh Abdoul
# email:  gunjkamg@mail.uc.edu, agarwand@mail.uc.edu, roychoii@mail.uc.edu, abdoulch@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  We worked on extracting and ecoding our image location and movie through decrypted json files. We also used PIL to add images to our python file

# Brief Description of what this module does. In the movie.py file, we are decrypting the movie title for our team using the team key, data file, and decryption key.
# Citations: used chatgpt for a few functions
# Anything else that's relevant:

# movie.py

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




