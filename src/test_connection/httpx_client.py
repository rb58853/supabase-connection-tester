import httpx
import os
import asyncio

supabase_access_key: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase_access_token: str = os.getenv("USER_ACCESS_TOKEN")
supabase_api_url: str = "https://suparaul.differential.es"


def create_httpx_client(supabase_access_token, supabase_api_url) -> httpx.AsyncClient:
    """Create and configure an httpx client for API requests."""
    headers = {
        "Authorization": f"Bearer {supabase_access_key}",
        "apikey": supabase_access_key,
        "Content-Type": "application/json",
        "X-API-Key": f"{supabase_access_key}",
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
                "✓ HTTPX GET connection established successfully"
                if response.status_code == 200
                else f"✗ HTTPX GET connection established error: {response.text}"
            )
            request = client.build_request(
                method="GET",
                url="/features/call_auth_admin_method/access",
                params={},
                # json={},
            )

            response = await client.send(request)
            print(
                "✓ HTTPX SEND REQUEST connection established successfully"
                if response.status_code == 200
                else f"✗ HTTPX SEND REQUEST connection established error: {response.text}"
            )

    asyncio.run(test_users_table())


test()
