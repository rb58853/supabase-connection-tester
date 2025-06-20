from supabase import create_client, Client
import asyncio
import os

SUPABASE_PROJECT_REF = os.getenv("SUPABASE_PROJECT_REF")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")


def basic_connection(url: str, key: str) -> Client:
    # Crear cliente
    supabase: Client = create_client(url, key)
    return supabase


def from_table(supabase: Client):
    try:
        # Verificar la conexión
        response = supabase.table("users").select("*").execute()
        print("✓ Supabase connection established successfully")
    except Exception as e:
        print(f"Error en la conexión: {str(e)}")
        pass


def test():
    supabase = basic_connection(url=SUPABASE_PROJECT_REF, key=SUPABASE_SERVICE_ROLE_KEY)
    from_table(supabase)
