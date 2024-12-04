import requests

url = 'https://api.oasis.ai/internal/providerList,providerList,providerPointsTimeseries,settingsProfile?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22offset%22%3A0%2C%22limit%22%3A100%2C%22sortBy%22%3A%22latest%22%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22offset%22%3A0%2C%22limit%22%3A100%2C%22sortBy%22%3A%22latest%22%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22interval%22%3A%22week%22%7D%7D%2C%223%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D'
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
     #input your token
    'authorization': '#token',
    'content-type': 'application/json',
    'origin': 'https://dashboard.oasis.ai',
    'priority': 'u=1, i',
    'referer': 'https://dashboard.oasis.ai/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url, headers=headers)
data = response.json()

# Function to extract 'id' values
def extract_ids(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'id':
                yield value
            elif isinstance(value, (dict, list)):
                yield from extract_ids(value)
    elif isinstance(data, list):
        for item in data:
            yield from extract_ids(item)

ids = list(extract_ids(data))

# Remove duplicate 'id' values and sort
unique_ids = sorted(set(ids))

# Save unique 'id' values to id.txt
with open('id.txt', 'w') as file:
    for id in unique_ids:
        file.write(id + '\n')

print("Unique IDs have been saved to id.txt.")
