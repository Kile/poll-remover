import json

# Load the config from the JSON file
with open("config.json") as f:
    CONFIG = json.load(f)

TOKEN = CONFIG["token"]

PREFIX = "." # Is never used