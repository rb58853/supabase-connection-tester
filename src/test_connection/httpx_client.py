import httpx
import os
import asyncio
from supabase import Client, create_client

# from ..tools.generate_access_token import get_token #Uncomment in production


supabase_api_url: str = "https://suparaul.differential.es"
supabase_access_token: str = os.getenv("USER_ACCESS_TOKEN")
supabase_access_key: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase: Client = create_client(supabase_api_url, supabase_access_key)


def create_httpx_client(supabase_access_token, supabase_api_url) -> httpx.AsyncClient:
    """Create and configure an httpx client for API requests."""
    # try: #Uncomment in production
    #     user = supabase.auth.get_user(supabase_access_token)
    #     print(user)
    # except:
    #     supabase_access_token = get_token()

    headers = {
        "Authorization": f"Bearer {supabase_access_token}",
        "apikey": supabase_access_key,
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
            response = await client.get("/features/call_auth_admin_method/access")
            print(
                "✓ HTTPX GET '/features/call_auth_admin_method/access' connection established successfully"
                if response.status_code == 200
                else f"✗ HTTPX GET '/features/call_auth_admin_method/access', connection established error: {response.text}"
            )

            response = await client.get("/rest/v1/users")
            print(
                "✓ HTTPX GET '/rest/v1/users' connection established successfully"
                if response.status_code == 200
                else f"✗ HTTPX GET '/rest/v1/users', connection established error: {response.text}"
            )

            # request = client.build_request(
            #     method="GET",
            #     url="/features/call_auth_admin_method/access",
            #     params={},
            #     # json={},
            # )
            # response = await client.send(request)
            # print(
            #     "✓ HTTPX GET '/features/call_auth_admin_method/access' connection established successfully"
            #     if response.status_code == 200
            #     else f"✗ HTTPX GET '/features/call_auth_admin_method/access', connection established error: {response.text}"
            # )

    asyncio.run(test_users_table())


test()
