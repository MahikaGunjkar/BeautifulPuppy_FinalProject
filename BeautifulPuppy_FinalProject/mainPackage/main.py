# Name: Mahika Gunjkar, Nandini Agarwal, Ishani Roy Chowdhury, Cheikh Abdoul
# email:  gunjkamg@mail.uc.edu, agarwand@mail.uc.edu, roychoii@mail.uc.edu, abdoulch@mail.uc.edu
# Assignment Number: Final Assignment
# Due Date:  12/10/2024
# Course #/Section:  IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  We worked on extracting and ecoding our image location and movie through decrypted json files. We also used PIL to add images to our python file

# Brief Description of what this module does. This is the main.py file, it extracts the correct data from the all the other files and helps to run it.It also has all the description keys 
# Citations:
# Anything else that's relevant:


#main.py
import json
from locationPackage.location import *
from moviePackage.movie import *
from groupimagePackage.groupimage import display_photo

if __name__ == "__main__":
    # Files and inputs
    location_file = "data/EncryptedGroupHints Fall 2024 Section 001.json"
    words_file = "data/UCEnglish.txt"
    movie_file = "data/TeamsAndEncryptedMessagesForDistribution.json"
    photo_path = "data/group_image.jpg"
    decryption_key = ""
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
