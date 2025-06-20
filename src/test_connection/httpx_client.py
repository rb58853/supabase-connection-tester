import httpx
import os

supabase_access_token: str = os.getenv("SUPABASE_ACCESS_TOKEN")
supabase_api_url: str = "https://api.supabase.io"


def create_httpx_client(supabase_access_token, supabase_api_url) -> httpx.AsyncClient:
    """Create and configure an httpx client for API requests."""
    headers = {
        "Authorization": f"Bearer {supabase_access_token}",
        "Content-Type": "application/json",
    }

    return httpx.AsyncClient(
        base_url=supabase_api_url,
        headers=headers,
        timeout=30.0,
    )


def test():
    create_httpx_client(supabase_access_token, supabase_api_url)
