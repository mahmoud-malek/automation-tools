
# ALX Scraping Tool

![alx Scraping Tool](https://img.icons8.com/ios-filled/50/000000/web-scraping.png)

A powerful and efficient web scraping tool written in Python. This tool allows you to scrape data from alx website and process it as needed. The setup script installs all necessary dependencies and sets up an alias for easy usage.

## Features

- Easy to install and use
- Scrapes data from websites efficiently
- Supports multiple Python packages for web scraping

## Installation

Follow these steps to install and set up the scraping tool:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/mahmoud-malek/automation-tools.git
   cd automation-tools
   ```

2. **Run the Setup Script**:
   ```sh
   ./setup_scraping.sh
   ```

3. **Reload the Shell** (if necessary):
   If the alias is not immediately available, you can manually reload the shell:
   ```sh
   source ~/.bashrc
   ```

## Usage

After installation, you can use the scraping tool with the alias `get`. Here is an example of how to use it:

```sh
get <project_url>
or 
get <project_url> readme

```
Note: using readme requires an api key to use ai generated readme
get your api key from: https://rapidapi.com/haxednet/api/chatgpt-api8
use basic plan for free

the tool is interactively ask you for your user & password for the alx projct
and also for the api key (if you want to use readme generator)

Replace `<project_url>` with the URL of the project or website you want to scrape.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

![GitHub](https://img.icons8.com/ios-filled/50/000000/github.png)