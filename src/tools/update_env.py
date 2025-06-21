import os


def update_env_variable(key, value, file_path=".env"):
    lines = []
    key_found = False

    # Read the existing .env file if it exists
    if os.path.exists(file_path):
        with open(file_path, "r") as env_file:
            lines = env_file.readlines()

    # Update the key if it exists, otherwise add it
    with open(file_path, "w") as env_file:
        for line in lines:
            if line.startswith(f"{key}="):
                env_file.write(f"{key}={value}\n")
                key_found = True
            else:
                env_file.write(line)
        if not key_found:
            env_file.write(f"{key}={value}\n")
