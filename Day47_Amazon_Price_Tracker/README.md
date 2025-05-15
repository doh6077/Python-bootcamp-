# Amazon Price Tracker Bot

This Python bot checks the price of a specified Amazon product at regular intervals and sends a notification to the user when the price drops to the desired threshold.

## Features

- Automatically checks the price of a product on Amazon.
- Sends a notification (e.g., email or SMS) when the price hits or drops below your target.
- Can be scheduled to run at specific times.

## How It Works

1. The script scrapes the product page on Amazon to get the current price.
2. Compares the current price with your target price.
3. If the price is equal to or lower than your target, it sends you a notification.

## Requirements

- `requests`
- `beautifulsoup4`
- `python-dotenv` (if using environment variables for credentials)
- (Optional) `smtplib` or `twilio` for notifications


