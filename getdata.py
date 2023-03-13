import requests
import csv
import time

# Define the base URL with a placeholder for the number
base_url = 'https://libad5343.net/libad/{}'

# Generate a list of sequentially increasing URLs with numbers ranging from x to y (format as x,y) So by default this
# is set to 1 through 1000
with open('metadata-results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, ['id', 'url', 'name', 'description', 'image', 'animation_url', 'key', 'attributes'])
    writer.writeheader()
    for i in range(1, 1000):
        # Use string formatting to insert the current number into the base URL
        url = base_url.format(i)
        # Print the URL being processed
        print(f"Processing {url}...")

        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.HTTPError as e:
            print(f"Failed processing {url}: {e}")
            continue

        respMap = resp.json()
        respMap['url'] = url
        keyList = [x for x in respMap['attributes'] if x.get('trait_type') == 'Key']
        respMap['key'] = keyList[0]['value'] if keyList else None

        writer.writerow(respMap)

        # Add a 500 millisecond delay between requests to avoid being rate limited.
        # This should probably be safe, to be extra certain you can change it to a 1.
        time.sleep(0.5)
