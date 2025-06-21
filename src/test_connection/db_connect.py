import os
import asyncpg
import asyncio

SUPABASE_DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
DATABASE_USER = os.getenv("DATABASE_USER")
CONTAINER_EXPOSE_IP = os.getenv("CONTAINER_EXPOSE_IP")
POOLER_PROXY_PORT_TRANSACTION = os.getenv("POOLER_PROXY_PORT_TRANSACTION")
POOLER_TENANT_ID = os.getenv("POOLER_TENANT_ID")
DATABASE_NAME = os.getenv("DATABASE_NAME")

db_url = f"postgresql://{DATABASE_NAME}.{POOLER_TENANT_ID}:{SUPABASE_DB_PASSWORD}@{CONTAINER_EXPOSE_IP}:{POOLER_PROXY_PORT_TRANSACTION}/{DATABASE_USER}"


async def create_pool():
    # Create the pool with optimal settings
    pool = await asyncpg.create_pool(
        db_url,
        min_size=2,  # Minimum connections to keep ready
        max_size=10,  # Maximum connections allowed (same as current)
        statement_cache_size=0,
        command_timeout=30.0,  # Command timeout in seconds
        max_inactive_connection_lifetime=300.0,  # 5 minutes
    )
    # Test the connection with a simple query
    async with pool.acquire() as conn:
        await conn.execute("SELECT 1")

    print("✓ Database connection established successfully")
    return pool


def test():
    asyncio.run(create_pool())
