import requests

# Read all IDs from the file id.txt
with open('id.txt', 'r') as file:
    ids = file.readlines()

# Remove any whitespace characters like `\n` at the end of each line
ids = [id.strip() for id in ids]

url = 'https://api.oasis.ai/internal/providerDelete?batch=1'
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

for id_value in ids:
    data = {
        "0": {
            "json": {
                "id": id_value
            }
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(f'Response for ID {id_value}: {response.text}')
