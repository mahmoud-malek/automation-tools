#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import asyncio
import aiohttp
import sys
import os

# Load the environment variables
load_dotenv()

# Colors for the terminal


class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

# Send a GET request to get the HTML of the project page


async def get_project_data(project_url, cookies):
    async with aiohttp.ClientSession(cookies=cookies) as session:
        loading_event = asyncio.Event()

        async def loading_effect():
            print(colors.YELLOW, "Loading project data ", colors.END, end="")
            while not loading_event.is_set():
                for i in range(5):
                    if loading_event.is_set():
                        break
                    await asyncio.sleep(0.5)
                    print("." * i, end="", flush=True)
            print()  # Move to the next line after loading effect

        loading_task = asyncio.create_task(loading_effect())

        async with session.get(project_url) as response:
            loading_event.set()  # Signal the loading effect to stop
            await loading_task  # Wait for the loading effect to finish
            return await response.text()

# Get login credentials from environment variables or user input


def get_login_credentials():
    email = os.getenv('ALX_EMAIL')
    password = os.getenv('ALX_PASSWORD')
    if not email or not password:
        while True:
            email = input(colors.YELLOW + "Enter your email: " + colors.END)
            password = input(
                colors.YELLOW + "Enter your password: " + colors.END)
            if email and password:
                with open('.env', 'w') as f:
                    f.write(f'ALX_EMAIL={email}\n')
                    f.write(f'ALX_PASSWORD={password}\n')
                break
            else:
                print("Please enter your email and password")
    return email, password

# Perform login and return the session and cookies


def login(email, password):
    session = requests.Session()
    response = session.get('https://intranet.alxswe.com/auth/sign_in')
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    login_data = {
        'user[email]': email,
        'user[password]': password,
        'authenticity_token': csrf_token
    }

    response = session.post(
        'https://intranet.alxswe.com/auth/sign_in', data=login_data)
    if response.url == 'https://intranet.alxswe.com/auth/sign_in':
        print(
            colors.RED + "Login failed. Please check your email and password" + colors.END)
        os.remove('.env')
        sys.exit()

    print(colors.GREEN + "Login successful" + colors.END)
    return session, session.cookies.get_dict()

# Main function


def main():
    email, password = get_login_credentials()
    session, cookies = login(email, password)

    if len(sys.argv) < 2:
        print(colors.RED, "Please enter the project url", colors.END)
        sys.exit(1)

    project_url = sys.argv[1]
    print(project_url)

    response = asyncio.run(get_project_data(project_url, cookies))
    # Parse the HTML of the project page
    soup = BeautifulSoup(response, 'html.parser')

    if soup.select_one('h1') is None:
        print(colors.RED, "Invalid project URL", colors.END)
        sys.exit(1)

    repo_name = soup.select_one('li:-soup-contains("GitHub repository:") code')
    dir_name = soup.select_one('li:-soup-contains("Directory:") code')
    file_names = [
        code.text for code in soup.select('li:-soup-contains("File:") code')
    ]

    if not repo_name or not dir_name:
        print(colors.RED +
              "Required information not found on the project page." +
              colors.END)
        sys.exit(1)

    repo_name = repo_name.text
    dir_name = dir_name.text

    if not os.path.exists(repo_name):
        os.makedirs(repo_name)
        print('Created a new directory with the name of the repository')

    if not os.path.exists(os.path.join(repo_name, dir_name)):
        os.makedirs(os.path.join(repo_name, dir_name))
        print(colors.GREEN, f'Created a new directory: {dir_name}', colors.END)

    for File in file_names:
        sections = [section.strip() for section in File.split(',')]
        for section in sections:
            if '/' in section:
                dirs = section.split('/')
                new_dir = os.path.join(repo_name, dir_name, *dirs[:-1])
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                    print(
                        colors.GREEN,
                        f'Created directory: {new_dir}',
                        colors.END)
                file_path = os.path.join(new_dir, dirs[-1])
            else:
                file_path = os.path.join(repo_name, dir_name, section)

            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write('')
                    print(f'Created file: {file_path}')

    if len(sys.argv) > 2 and sys.argv[2] == 'readme':
        API_KEY = os.getenv('RAPIDAPI_KEY')
        if not API_KEY:
            print(colors.RED, "API key not found", colors.END)
            API_KEY = input("Enter the API key: ")
            with open('.env', 'a') as f:
                f.write(f'RAPIDAPI_KEY={API_KEY}\n')

        url = "https://chatgpt-api8.p.rapidapi.com/"
        payload = [{
            "content":
                f"create a professional README.md file for: {soup.select_one('h1').text}",
                "role": "user"
        }]
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
        # check if the response is successful
        if response.status_code != 200:
            print(colors.RED, "Failed to get the README content from the API",
                  colors.END)
            sys.exit(1)

        response_content = response.json().get('text')

        readme_path = os.path.join(repo_name, dir_name, 'README.md')
        if not os.path.exists(readme_path) or os.path.getsize(
                readme_path) == 0:
            with open(readme_path, 'w') as f:
                if response_content:
                    f.write(response_content)
                    print(colors.GREEN, 'Created a README.md file', colors.END)
                else:
                    print(
                        colors.RED,
                        'No content to write to README.md',
                        colors.END)
        else:
            print(colors.BLUE, 'README.md file already exists', colors.END)

    print(
        colors.BLUE,
        f'\nyour current dir is: :) {os.path.join(repo_name, dir_name)}',
        colors.END)
    os.chdir(os.path.join(repo_name, dir_name))
    os.system('/bin/bash')


if __name__ == "__main__":
    main()
