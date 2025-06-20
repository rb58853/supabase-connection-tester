import httpx
import os
import asyncio

supabase_access_token: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase_api_url: str = "https://suparaul.differential.es"


def create_httpx_client(supabase_access_token, supabase_api_url) -> httpx.AsyncClient:
    """Create and configure an httpx client for API requests."""
    headers = {
        "Authorization": f"Bearer {supabase_access_token}",
        "apikey": supabase_access_token,
        "Content-Type": "application/json",
    }

    return httpx.AsyncClient(
        base_url=supabase_api_url,
        headers=headers,
        timeout=30.0,
    )


def test():
    async def test_users_table():
        async with create_httpx_client(
            supabase_access_token, supabase_api_url
        ) as client:
            # Cambia 'users' por el nombre real de una de tus tablas
            response = await client.get("/rest/v1/users")
            print(
                "✓ HTTPX connection established successfully"
                if response.status_code == 200
                else "✗ HTTPX connection established error"
            )
            # print("Status code:", response.status_code)
            # print("Response JSON:", response.json())

    asyncio.run(test_users_table())
