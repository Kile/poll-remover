import json

from discord import Locale
from typing import Dict

# Load the config from the JSON file
with open("config.json") as f:
    CONFIG = json.load(f)

TOKEN = CONFIG["token"]

PREFIX = "." # Is never used

LANGS: Dict[Locale, Dict[str, str]] = {
    Locale.american_english: {
        "title": "Poll deleted",
        "description": "Hi {user}, I just deleted the poll you posted in the server {server} because it is under Poll Bot Protection:tm:. You are not allowed to create polls in this server without Manage Server permissions!",
        "invite_text": "Invite me to get rid of polls for anyone without Manage Server permissions!",
        "button": "Get Poll Protection for your server",
        "button_short": "Invite me"
    },
    Locale.german: {
        "title": "Poll gelöscht",
        "description": "Hallo {user}, ich habe gerade einen Poll gelöscht, den du im Server {server} gepostet hast, weil dieser unter Poll Bot Protection:tm: steht. Du darfst in diesem Server keine Polls senden, ohne Manage Server Permissions zu haben!",
        "invite_text": "Lade mich in deinen Server ein, um Polls für jeden ohne Manage Server Permissions zu entfernen!",
        "button": "Hol dir Poll Protection für deinen Server",
        "button_short": "Lade mich ein"
    }
}

# Add British English as an alias for American English
LANGS[Locale.british_english] = LANGS[Locale.american_english]