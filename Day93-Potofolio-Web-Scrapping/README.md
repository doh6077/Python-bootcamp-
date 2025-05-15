# Audiobook Ranking Scraper

This project scrapes the latest audiobook rankings from Audible using BeautifulSoup and sends a daily update to users via SMS using Twilio.

## Features

- Scrapes audiobook titles from Audible's search results page.
- Sends the list of book titles as an SMS notification to a specified phone number.
- Uses environment variables for sensitive information (Twilio credentials and phone numbers).

## How It Works

1. **Web Scraping:**  
   The script fetches Audible's search results page and extracts audiobook titles using BeautifulSoup.

2. **SMS Notification:**  
   The extracted book list is sent as an SMS message using the Twilio API.

3. **Environment Variables:**  
   - Twilio credentials and phone numbers are loaded from a `.env` file for security.

## Requirements

- `beautifulsoup4`
- `requests`
- `python-dotenv`
- `twilio`