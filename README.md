# Supabase Connection Tester

This project is a simple tool designed to test connections with Supabase hosted on Docker or a VPS. It also integrates with environments like Kong for API gateway management. Additionally, the project includes utilities such as an Access Token Generator.

## Features

- Test connectivity with Supabase instances.
- Support for Docker and VPS-hosted environments.
- Access Token Generator for secure authentication.
<!-- - Integration with Kong for API gateway testing. -->

## Prerequisites

- Docker installed on your system.
- Python 3.8 or higher.
- Supabase instance (hosted locally or on a VPS).
- Optional: Kong API Gateway setup.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/rb58853/supabase-connection-tester.git
    cd supabase-connection-tester
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    Create a `.env` file in the root directory and configure the following:

    ```env
    # Required for remote Supabase projects (optional for local development)
    SUPABASE_PROJECT_REF=http://HOSTNAME:PORT/ or https://subdomain.domain.ext
    SUPABASE_DB_PASSWORD=your-postgres-password
    SUPABASE_REGION=us-east-1
    
    # Optional configuration
    SUPABASE_ACCESS_TOKEN=your-supabase-access-token
    SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
    
    # Docker Container Environment
    CONTAINER_EXPOSE_IP=xxx.xx.xx.xx
    USER_ACCESS_TOKEN=your-user-access-token
    
    ## DATABASE
    DATABASE_NAME=postgres
    DATABASE_USER=postgres
    
    ## POOLER
    POOLER_PROXY_PORT_TRANSACTION=6543
    POOLER_TENANT_ID=your-tenant-id

    # LOGING
    EMAIL=example@gmail.com
    PASSWORD=supabase_user_password
    ```

## Usage

### Running the Connection Tester

To test the connection with your Supabase instance:

```bash
python test_connection.py
```

### Generating an Access Token

To generate an access token:

```bash
python src.tools.generate_access_token.py
```
It is mandatory to create a user in your auth user list of your Supabase instance.
![alt text](Doc/image.png)

## Contact

For questions or support, please open a Issue in this repositorie.
