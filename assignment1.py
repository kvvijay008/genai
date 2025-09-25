
import requests
import json

def get_github_user(user_data):
    not_found_user = []
    for user_id in user_data:
        url = f'https://github.com/{user_id}/genai/blob/main/assignment1.py'
        response = requests.get(url)
        if response.status_code == 200:
            print(user_id, 'submitted the file')
            filename = f"{user_id}.py"
            with open(filename, "w") as f:
                f.write("" + response.text)
            print(f"File saved for {user_id} -> {filename}")
        else:
            not_found_user.append(user_id)
    return not_found_user
            
 

user_data = ['kvvijay008', 'bbb', 'aaa']
not_found_user = get_github_user(user_data)
print("Users id's or file not found for users: ", not_found_user)
