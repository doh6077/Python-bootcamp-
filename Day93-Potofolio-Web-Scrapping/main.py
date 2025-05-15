from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

# Scraping Audible website 
response = requests.get("https://www.audible.com/search?keywords=book&node=18573211011&overrideBaseCountry=true&ipRedirectOverride=true&ref_pageloadid=not_applicable&pf_rd_p=97a1c91a-2694-43e4-ad66-256f5ac11479&pf_rd_r=F9RMKBR8PMAM4VM3XHWC&plink=2C9gPIFJK0X9yOoZ&pageLoadId=nLVcNR8KvLZVf2MN&creativeId=292d6343-f11b-4bbe-a8a5-d4b7272abf61")
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all(class_="bc-link bc-color-link")
book_names = [book.getText().strip() for book in books if len(book.getText().strip()) > 1]
print(book_names)