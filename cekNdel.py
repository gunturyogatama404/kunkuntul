import requests

# Set headers and base URL
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': '', #input token
    'content-type': 'application/json',
    'origin': 'https://dashboard.oasis.ai',
    'referer': 'https://dashboard.oasis.ai/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
}
url_fetch = 'https://api.oasis.ai/internal/providerList,providerList,providerPointsTimeseries,settingsProfile?batch=1&input=%7B%220%22%3A%7B%22json%22%3A%7B%22offset%22%3A0%2C%22limit%22%3A100%2C%22sortBy%22%3A%22latest%22%7D%7D%2C%221%22%3A%7B%22json%22%3A%7B%22offset%22%3A0%2C%22limit%22%3A100%2C%22sortBy%22%3A%22latest%22%7D%7D%2C%222%22%3A%7B%22json%22%3A%7B%22interval%22%3A%22week%22%7D%7D%2C%223%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D'

# Fetch data and extract IDs
response = requests.get(url_fetch, headers=headers)
data = response.json()

def extract_ids(data):
    """ Recursively extract all 'id' values from nested JSON. """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'id':
                yield value
            elif isinstance(value, (dict, list)):
                yield from extract_ids(value)
    elif isinstance(data, list):
        for item in data:
            yield from extract_ids(item)

# Extract unique IDs and save them to a file
unique_ids = sorted(set(extract_ids(data)))
with open('id.txt', 'w') as file:
    file.writelines(f'{id}\n' for id in unique_ids)

print("Unique IDs saved to id.txt.")

# Read IDs from file and delete them
with open('id.txt', 'r') as file:
    ids = [line.strip() for line in file]

url_delete = 'https://api.oasis.ai/internal/providerDelete?batch=1'
for id_value in ids:
    data = {"0": {"json": {"id": id_value}}}
    response = requests.post(url_delete, headers=headers, json=data)
    print(f'Response for ID {id_value}: {response.text}')
