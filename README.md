# Personal Instagram Scraper - for personal archiving
**Written by Lily Gates** 

## Description
This Python project uses the **Instagram Basic Display API** to download  your personal Instagram posts (images, videos, and carousels) and save metadata in a CSV file. Each media file is saved with a timestamped filename, and carousel posts are enumerated for easy reference.  


## Features
- Download **images, videos, and carousel posts**.
- Name files based on **date and time posted**.
- Carousel items are numbered (`_01`, `_02`, etc.).
- Save **metadata** to a CSV file (username, caption, datetime, media type, filename, URL).
- Fully **automated** with Python.
- Works only for your **own Instagram account**.

## Required Dependencies
- Python 3.8+  
- Access to **Instagram Basic Display API** (generate an access token for your account).  
- Required packages: `requests`, `pandas`, `yaml`

## Setup
1. Clone this repository
```
git clone https://github.com/lilyxgates/personal_instagram_scraper.git
cd personal_instagram_scraper
```

2. Configure your access token in YAML file (.yaml)

## Usage
Run script
`python personal_instagram_scraper.py`

The script will:
* Fetch all your posts from Instagram using the API.
* Download media files into personal_instagram_scraper/media/.
* Save metadata to instagram_archive/{USERNAME}_posts_metadata.csv.

File Naming Convention
* Single media posts: Y`YYY-MM-DD_HH-MM-SS.jpg` or `.mp4`
* Carousel posts: `YYYY-MM-DD_HH-MM-SS_01.jpg`, `YYYY-MM-DD_HH-MM-SS_02.jpg`, etc.

## Notes
* Only downloads posts from your account.
* Uses the official Instagram Basic Display API
* Media URLs are time-sensitive; downloaded files preserve a local copy for archiving.

## References
* [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api)  
* [Graph API Reference: User Media](https://developers.facebook.com/docs/instagram-basic-display-api/reference/user/media)
