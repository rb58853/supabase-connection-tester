from supabase import create_client
import os

"""
Para obtener el token debes crear un usuario en la tabla auth.users en tu dashboard de supabase.
"""

SUPABASE_PROJECT_REF = os.getenv("SUPABASE_PROJECT_REF")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

EMAIL = os.getenv("EMAIL")  # CREATE .ENV VAR
PASSWORD = os.getenv("PASSWORD")  # CREATE .ENV VAR


def get_token():
    supabase = create_client(SUPABASE_PROJECT_REF, SUPABASE_SERVICE_ROLE_KEY)
    user = supabase.auth.sign_in_with_password({"email": EMAIL, "password": PASSWORD})
    return user.session.access_token
