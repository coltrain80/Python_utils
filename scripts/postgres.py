# postgres_setup.py
"""
This script installs PostgreSQL on Ubuntu, configures it with initial settings,
and creates a generic database.

Usage:
    Run the script with sudo or as a root user to install and configure PostgreSQL.

Example:
    sudo python postgres_setup.py
"""

import os
import subprocess
import sys

def run_command(command):
    """
    Run a system command and handle errors.
    
    :param command: The command to run.
    """
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        sys.exit(1)

def configure_postgres():
    """
    Configure PostgreSQL with initial settings and create a generic database.
    """
    postgres_password = "password123"  # Replace with a secure password
    database_name = "generic_db"
    user_name = "generic_user"
    user_password = "user_password"  # Replace with a secure password

    commands = [
        # Set password for the postgres user
        f"sudo -u postgres psql -c \"ALTER USER postgres PASSWORD '{postgres_password}';\"",
        # Create a new PostgreSQL role with a password
        f"sudo -u postgres psql -c \"CREATE ROLE {user_name} WITH LOGIN PASSWORD '{user_password}';\"",
        # Create a new PostgreSQL database owned by the new role
        f"sudo -u postgres psql -c \"CREATE DATABASE {database_name} OWNER {user_name};\"",
        # Grant all privileges on the database to the user
        f"sudo -u postgres psql -c \"GRANT ALL PRIVILEGES ON DATABASE {database_name} TO {user_name};\""
    ]

    for command in commands:
        run_command(command)

def main():
    if os.geteuid() != 0:
        print("This script must be run as root. Please use sudo.")
        sys.exit(1)

    # Step 1: Update the package list
    run_command("apt-get update")

    # Step 2: Install PostgreSQL
    run_command("apt-get install -y postgresql postgresql-contrib")

    # Step 3: Start PostgreSQL service
    run_command("systemctl start postgresql")

    # Step 4: Enable PostgreSQL service to start on boot
    run_command("systemctl enable postgresql")

    # Step 5: Configure PostgreSQL
    configure_postgres()

    print("PostgreSQL installed and configured successfully.")
    print("Database 'generic_db' created with user 'generic_user'.")

if __name__ == "__main__":
    main()
