import requests
from bs4 import BeautifulSoup
import csv
import time

# Define the base URL with a placeholder for the number
base_url = 'https://libad5343.net/libad/{}'

# Create an empty list to store the URLs
url_list = []

# Generate a list of sequentially increasing URLs with numbers ranging from x to y (format as x,y) So by default this is set to 1 through 1000
for i in range(1, 1000):
    # Use string formatting to insert the current number into the base URL
    url = base_url.format(i)

    # Add the URL to the list
    url_list.append(url)

# Create an empty list to store the results
results = []

# Loop through the URLs and extract the text content
for url in url_list:
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the raw text content from the HTML using the get_text() method
    text = soup.get_text()

    # Print the URL being processed
    print(f"Currently processing URL: {url}")

    # Add the URL and text content to the results list
    results.append([url, text])

    # Add a 500 millisecond delay between requests to avoid being rate limited.  This should probably be safe, to be extra certain you can change it to a 1.
    time.sleep(0.5)

# Export the results to a CSV file
with open('metadata-results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Text'])

    for result in results:
        writer.writerow(result)
