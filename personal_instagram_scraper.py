# ============================================
# Personal Instagram Scraper
# Author: Lily Gates
# Created: 12/22/2025
# Last Updated 12/22/2025
# ============================================

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
# GET USER ID
# -----------------------------
me_url = f"https://graph.instagram.com/me?fields=id,username&access_token={ACCESS_TOKEN}"
resp = requests.get(me_url)
if resp.status_code != 200:
    raise Exception(f"Failed to fetch user info: {resp.status_code} {resp.text}")

user_data = resp.json()
USER_ID = user_data["id"]
print(f"Found user: {user_data['username']} (ID: {USER_ID})")

# -----------------------------
# GET USER MEDIA
# -----------------------------
BASE_URL = f"https://graph.instagram.com/{USER_ID}/media"
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

# -----------------------------
# DOWNLOAD MEDIA & BUILD METADATA
# -----------------------------
metadata = []

for post in media_list:
    post_dt = datetime.fromisoformat(post["timestamp"].replace("Z", "+00:00"))
    caption = post.get("caption", "")

    # Handle carousel
    if post["media_type"] == "CAROUSEL_ALBUM":
        children = post.get("children", {}).get("data", [])
        for idx, child in enumerate(children, start=1):
            media_url = child["media_url"]
            ext = media_url.split("?")[0].split(".")[-1]
            filename = f"{post_dt.strftime('%Y-%m-%d_%H-%M-%S')}_{idx:02d}.{ext}"
            path = os.path.join(MEDIA_DIR, filename)
            with open(path, "wb") as f:
                f.write(requests.get(media_url).content)
            metadata.append({
                "username": USERNAME,
                "datetime": post_dt,
                "caption": caption,
                "media_type": child["media_type"],
                "filename": filename,
                "url": media_url
            })
    else:  # single image/video
        media_url = post["media_url"]
        ext = media_url.split("?")[0].split(".")[-1]
        filename = f"{post_dt.strftime('%Y-%m-%d_%H-%M-%S')}.{'jpg' if post['media_type']=='IMAGE' else 'mp4'}"
        path = os.path.join(MEDIA_DIR, filename)
        with open(path, "wb") as f:
            f.write(requests.get(media_url).content)
        metadata.append({
            "username": USERNAME,
            "datetime": post_dt,
            "caption": caption,
            "media_type": post["media_type"],
            "filename": filename,
            "url": media_url
        })

    print(f"Saved post {post_dt} with {len(post.get('children', {}).get('data', [])) or 1} media files.")

# -----------------------------
# SAVE METADATA CSV
# -----------------------------
df = pd.DataFrame(metadata)
csv_path = os.path.join(ARCHIVE_DIR, f"{USERNAME}_posts_metadata.csv")
df.to_csv(csv_path, index=False)
print(f"Metadata saved to {csv_path}")