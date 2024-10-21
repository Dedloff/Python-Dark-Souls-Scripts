import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://darksouls.fandom.com/wiki/Rings_(Dark_Souls)'

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Check the content within the main body section of the wiki page
content_section = soup.find('div', {'class': 'mw-parser-output'})

# Initialize a list to hold ring data
rings = []

# Search for the specific section(s) containing ring information
# Look for headers or sections indicating each ring's data, sometimes within <h3>, <h2>, or <div> tags
for item in content_section.find_all(['h3', 'h2', 'div', 'p']):  # Adjust based on correct HTML tags
    ring_name = item.find('a').text if item.find('a') else 'Unknown'
    description = item.text.strip() if item else 'No description'
    
    # Add extracted ring data to the list
    if ring_name and description:
        rings.append([ring_name, description])

# Create a DataFrame using Pandas
df = pd.DataFrame(rings, columns=['Ring Name', 'Description'])

# Save the DataFrame to a CSV file
df.to_csv('dark_souls_rings.csv', index=False)

print("CSV exported successfully!")
