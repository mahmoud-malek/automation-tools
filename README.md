# ALX Scraping Tool

A powerful and efficient web scraping tool written in Python. This tool allows you to scrape data from the ALX website and process it as needed. The setup script installs all necessary dependencies and sets up an alias for easy usage.

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

Note: Using the [`readme`](command:_github.copilot.openSymbolFromReferences?%5B%22readme%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmahmoudmalek%2Fautomation-tools%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmahmoudmalek%2Fautomation-tools%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmahmoudmalek%2Fautomation-tools%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A39%2C%22character%22%3A18%7D%7D%5D%5D "Go to definition") option requires an API key to use AI-generated README. Get your API key from: [https://rapidapi.com/haxednet/api/chatgpt-api8](https://rapidapi.com/haxednet/api/chatgpt-api8). Use the basic plan for free.

The tool will interactively ask you for your username and password for the ALX project, and also for the API key (if you want to use the README generator).

Replace `<project_url>` with the URL of the project or website you want to scrape.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

![GitHub](https://img.icons8.com/ios-filled/50/000000/github.png)