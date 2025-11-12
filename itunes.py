import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python itunes.py <artist_name>")

# Get artist name from command line
artist = sys.argv[1]

# Make API request to iTunes Search API
response = requests.get(
    "https://itunes.apple.com/search",
    params={"entity": "song", "limit": 5, "term": artist}
)

# Parse JSON response
data = response.json()

# Print results
for result in data["results"]:
    print(f"{result['trackName']} : '{result['artistName']}'")