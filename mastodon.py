import random
from mastodon import Mastodon

# Load Mastodon API credentials
mastodon = Mastodon(
    access_token='your_access_token',
    api_base_url='https://botsin.space'  # Replace with your instance
)

# Read the lines from the text file
with open('toots.txt', 'r') as file:
    toots = file.readlines()

# Choose a random toot
toot = random.choice(toots).strip()

# Send the toot
mastodon.status_post(toot)
