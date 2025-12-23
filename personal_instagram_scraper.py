"""
# ============================================

# Personal Instagram Scraper
# Author: Lily Gates
# Created: 12/22/2025
# Last Updated 12/22/2025

1. Set up Instagram Basic Display API
    1a. Go to Facebook for Developers -> Create an app -> choose Consumer.
    1b. Add Instagram Basic Display product.
    1c. Generate an Access Token (long-lived if possible).
    1d. Make sure the token has permission to read your own media (user_media).

2. Install dependencies
pip install requests pandas


# ============================================
"""

import os
import requests
import pandas as pd
import yaml
from datetime import datetime

# -----------------------------
# CONFIG & PATHS
# -----------------------------
BASE_DIR = "personal_instagram_scraper"
MEDIA_DIR = os.path.join(BASE_DIR, "media")
ARCHIVE_DIR = os.path.join(BASE_DIR, "instagram_archive")

os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")

# Load username and access token from YAML
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

USERNAME = config["username"]
ACCESS_TOKEN = config["access_token"]

# -----------------------------
# GET USER MEDIA
# -----------------------------
BASE_URL = "https://graph.instagram.com/me/media"
FIELDS = "id,caption,media_type,media_url,timestamp,children{media_type,media_url}"

media_list = []
url = f"{BASE_URL}?fields={FIELDS}&access_token={ACCESS_TOKEN}"

while url:
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"Failed to fetch media: {resp.status_code} {resp.text}")
    data = resp.json()
    media_list.extend(data.get("data", []))
    url = data.get("paging", {}).get("next")  # handle pagination

print(f"Found {len(media_list)} posts.")
