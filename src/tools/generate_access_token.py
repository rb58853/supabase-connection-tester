from supabase import create_client
from update_env import update_env_variable
import os

"""
Para obtener el token debes crear un usuario en la tabla auth.users en tu dashboard de supabase.
"""

SUPABASE_PROJECT_REF = os.getenv("SUPABASE_PROJECT_REF")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

supabase = create_client(SUPABASE_PROJECT_REF, SUPABASE_SERVICE_ROLE_KEY)
user = supabase.auth.sign_in_with_password({"email": EMAIL, "password": PASSWORD})
jwt = user.session.access_token

# Call the function to update the .env file
update_env_variable("USER_ACCESS_TOKEN", jwt)
print("User access token obtained successfully.")
