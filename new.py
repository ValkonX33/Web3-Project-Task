import json

with open('ethereum.json', 'r') as file:
    ethereum_data = json.load(file)

# Extracting  URLs and names from specified sections
sections = ['data_aggregator', 'explorers', 'bridges', 'bounty', 'grants', 'faucets', 'rpcs', 'wallets', 'oracles']
polygon = []

for section in sections:
    for entry in ethereum_data.get(section, []):
        name = entry.get('name')
        url = entry.get('url')
        if name and url:
            polygon.append({'name': name, 'url': url})


with open('polygon.json', 'w') as outfile:
    json.dump(polygon, outfile, indent=4)
