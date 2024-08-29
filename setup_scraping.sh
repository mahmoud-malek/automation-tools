#!/bin/bash

# Update package list and install necessary system packages
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install necessary Python packages
pip install requests beautifulsoup4 python-dotenv aiohttp

# Deactivate the virtual environment
deactivate

# Create an alias to run the script
alias get='$(pwd)/venv/bin/python3 $(pwd)/scraping.py'
echo "alias get='$(pwd)/venv/bin/python3 $(pwd)/scraping.py'" >> ~/.bashrc

# Inform the user that the setup is complete
echo "Setup complete. You can now run the script using the command 'get'."