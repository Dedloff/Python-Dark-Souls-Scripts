import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://darksouls.fandom.com/wiki/Rings_(Dark_Souls)'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all sections that might contain the rings (In fandom pages, lists are often in 'li' tags)
ring_sections = soup.find_all('div', {'class': 'mw-parser-output'})

# Extract information from these sections
rings = []

for section in ring_sections:
    items = section.find_all('li')  # This will find each list item
    for item in items:
        ring_name = item.find('a').text if item.find('a') else 'Unknown'  # Some items may not have a link
        description = item.text.strip()  # The text inside the <li>
        rings.append([ring_name, description])

# Convert extracted data to a Pandas DataFrame
df = pd.DataFrame(rings, columns=['Ring Name', 'Description'])

# Save the DataFrame to a CSV file
df.to_csv('dark_souls_rings.csv', index=False)

print("CSV exported successfully!")
