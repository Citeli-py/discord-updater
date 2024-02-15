# Discord Updater for Ubuntu

This simple program automates the process of updating Discord on Ubuntu. Instead of manually downloading and installing the updates from the Discord website, this script does the job for you. It downloads the latest Discord package and installs it on your system effortlessly.

## Dependencies

Before using the Discord Updater, ensure that you have the following dependencies installed:

- Python 3
- Requests library (can be installed via pip: `pip install requests`)
- Apt

## Usage

1. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```
    git clone https://github.com/Citeli-py/discord-updater.git
    ```

2. **Navigate to the Directory**: Enter the directory where you cloned the repository:

    ```
    cd discord-updater
    ```

3. **Set Permissions**: Ensure that the script file (`discord-updater.sh`) has executable permissions. You can do this by running the following command:

    ```
    chmod +x discord-updater.sh
    ```

4. **Run the Updater**: Execute the script to update Discord:

    ```
    sudo ./discord-updater.sh
    ```

## Notes

- Make sure you have administrative privileges (`sudo`) to install the Discord package.
- This script is specifically designed for Ubuntu systems.
- Ensure that you have sufficient disk space and a stable internet connection while running the updater.

## Disclaimer

This script is provided as-is and without warranty. Use it at your own risk. The developers are not responsible for any damage caused by the misuse of this script.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.
