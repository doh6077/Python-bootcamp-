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


# Header Example for my reference 

Adding a header—especially the User-Agent—to your HTTP request makes your script appear as if it’s coming from a real web browser instead of a bot or automated script. Many websites block or restrict requests that don’t have a User-Agent or have one that looks suspicious, to prevent scraping or abuse. By including headers, you increase the chances that your request will be accepted and processed like a normal user visit.

{
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,it-IT;q=0.8,it;q=0.7,fr-CA;q=0.6,fr;q=0.5,es-MX;q=0.4,es;q=0.3,ko;q=0.2",
    "Host": "httpbin.org",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-682755f9-6cf532f66c4e44c30ef70735"
  }
}

# Check header in this link 

https://myhttpheader.com/