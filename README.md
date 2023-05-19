# Steam Market Price Notifier

Steam Market Price Notifier is a Python script that allows you to track and receive notifications about price changes for items on the Steam market. It utilizes web scraping with Selenium to fetch the current price of a specified item and sends notifications via the Pushover API when the price exceeds a predefined limit.

## Features

- Fetches the current price of a specific item on the Steam market.
- Periodically checks the price at a defined interval.
- Sends notifications to your mobile device when the price exceeds a set limit.
- Supports multiple Chrome profiles for simultaneous tracking (optional).
- Customizable user data path for Chrome profiles (optional).

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Selenium
- Chrome web driver

## Getting Started

1. Clone this repository to your local machine or download the source code.
2. Install the required dependencies by running the following command:
`pip install selenium`
3. Download the Chrome web driver and place it in a directory accessible by the script.
4. Modify the script's configuration variables according to your requirements (URL, API keys, time interval, etc.).
5. Run the script:
`python item_price.py`

## Configuration

The script includes several configuration options that you can modify:

- `url`: The URL of the Steam market listing for the item you want to track.
- `api_token` and `user_key`: Your API token and user key from Pushover for sending notifications.
- `loop_sec`: The time interval (in seconds) between price checks.
- `limitPrice`: The price limit for triggering notifications.
- `plural`: Set to `True` if you have multiple Chrome profiles, otherwise set to `False`.
- `user_data_dir`: The path to the Chrome user data directory (required if `plural` is `True`).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Selenium](https://www.selenium.dev/) - Web scraping library
- [Pushover](https://pushover.net/) - Notification service

## Disclaimer

This script is provided as-is with no warranty or guarantee. Use it at your own risk.
