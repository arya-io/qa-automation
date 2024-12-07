# QA Automation Assignment - Python + Selenium

This repository contains an automated test script built using **Python** and **Selenium WebDriver**. The script automates interactions with a demo website, extracting category and product details, simulating cart actions, and searching for items.

## Features

- Extracts category items from the website and counts occurrences
- Simulates scrolling and loading dynamic content
- Adds items to the cart and manipulates cart quantities
- Performs a search operation and captures search suggestions
- Takes screenshots of key interactions (cart page, search suggestions)

## Requirements

- Python 3.9.9
- Selenium WebDriver
- Chrome WebDriver (managed by `webdriver_manager`)
- Other dependencies listed in `requirements.txt`

## Running the Script

1. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:
    ```bash
    python main.py
    ```

## Screenshots

The script captures key interactions in the following screenshots:
- `Cart_Page.png`
- `Removed_Cart.png`
- `Search_suggestions.png`

## Note

This script is designed to work with the [Zilly WordPress theme demo](https://www.radiustheme.com/demo/wordpress/themes/zilly/).
