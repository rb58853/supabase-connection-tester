from supabase import create_client, Client
import asyncio

import os

PUBLIC_SUPABASE_URL = f'https://{os.getenv("DNS")}'
PUBLIC_SUPABASE_ANON_KEY = os.getenv("PUBLIC_SUPABASE_ANON_KEY")
SERVICE_ROLE_KEY = os.getenv("SERVICE_ROLE_KEY")
JWT_KEY = os.getenv("JWT_KEY")


def basic_connection() -> Client:
    # Crear cliente
    url = PUBLIC_SUPABASE_URL
    key = PUBLIC_SUPABASE_ANON_KEY
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
    supabase = basic_connection()
    from_table(supabase)
