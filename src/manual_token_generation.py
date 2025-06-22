from tools.generate_access_token import get_token
from tools.update_env import update_env_variable

# Call the function to update the .env file
update_env_variable("USER_ACCESS_TOKEN", get_token())
print("User access token obtained successfully.")
