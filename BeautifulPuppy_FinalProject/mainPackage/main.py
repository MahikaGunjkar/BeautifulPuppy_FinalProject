#main.py
import json
from locationPackage.location import *
from moviePackage.movie import *
from display_photo.photo import display_photo

if __name__ == "__main__":
    # Files and inputs
    location_file = "data/EncryptedGroupHints.json"
    words_file = "data/UCEnglish.txt"
    movie_file = "data/TeamsAndEncryptedMessagesForDistribution.json"
    photo_path = "photo/group_photo.jpg"
    decryption_key = ""  # Replace with actual key
    team_key = "BeautifulPuppy"

    # Decrypt location
    try:
        with open(location_file, 'r') as file:
            location_data = json.load(file)
            indices = location_data.get(team_key, [])
        if indices:
            decrypted_location = decrypt_location(indices, words_file)
            print(f"Decrypted Location for {team_key}: {decrypted_location}")
        else:
            print(f"No indices found for {team_key}.")
    except FileNotFoundError:
        print("Error: Location JSON file not found.")
        indices = []

    # Decrypt movie title
    decrypted_movie_title = decrypt_movie_title(team_key, movie_file, decryption_key)
    print(f"Decrypted Movie Title for {team_key}: {decrypted_movie_title}")

    # Display the photo
    display_photo(photo_path)
