import os
import random
from mastodon import Mastodon

# Load Mastodon API credentials from environment variables
access_token = os.getenv('ACCESS_TOKEN')
api_base_url = os.getenv('API_BASE_URL')

# Initialize Mastodon API
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=api_base_url
)

# Read the lines from the text file
with open('toots.txt', 'r') as file:
    toots = file.readlines()

# Choose a random toot
toot = random.choice(toots).strip()

# Send the toot
mastodon.status_post(toot)
