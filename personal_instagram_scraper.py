"""
# ============================================

# Personal Instagram Scraper
# Author: Lily Gates
# Created: 12/22/2025
# Last Updated 12/22/2025

# Description:
# TBD

# Features:
# - Works for both Mac and Windows OS

# Requirements
# pip install selenium webdriver-manager pandas requests


# Notes:
Selenium can only see private accounts if:
- You are logged in to Instagram
- You already follow the private account
- Selenium uses your existing Chrome profile
If any of those are false, Instagram will still hide the content.

# ============================================
"""

import os
import time
import platform
import requests
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# ------------------------------
# 1. SETUP CHROME + SELENIUM
# ------------------------------
# Get the OS username dynamically
os_username = os.getlogin()

# Initialize Chrome options
chrome_options = Options()

# Use your real Chrome profile
system_os = platform.system()

if system_os == "Darwin":  # macOS
    chrome_options.add_argument(
        f"--user-data-dir=/Users/{os_username}/Library/Application Support/Google/Chrome"
    )
    chrome_options.add_argument("--profile-directory=Default")
elif system_os == "Windows":
    chrome_options.add_argument(
        fr"--user-data-dir=C:\Users\{os_username}\AppData\Local\Google\Chrome\User Data"
    )
    chrome_options.add_argument("--profile-directory=Default")
else:
    raise Exception(f"Unsupported OS: {system_os}")

# Optional: headless mode
# chrome_options.add_argument("--headless=new")

# Create the driver using webdriver_manager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Test: open Instagram
driver.get("https://www.instagram.com/")
print(driver.title)

# ------------------------------
# 2. OPEN INSTAGRAM PROFILE
# ------------------------------

username_to_scrape = "selenagomez"  # can be public or private (if you follow)
driver.get(f"https://www.instagram.com/{username_to_scrape}/")

time.sleep(3 + random.random() * 2)  # wait for page to load

# ------------------------------
# 3. EXTRACT BASIC INFO
# ------------------------------

# Header contains name, bio, counts
header = driver.find_element(By.TAG_NAME, "header")

full_name = header.find_element(By.XPATH, ".//h1").text
bio_elem = header.find_elements(By.XPATH, ".//div[@role='presentation']//span")
bio = " ".join([b.text for b in bio_elem])

# Posts / Followers / Following
stats = driver.find_elements(By.XPATH, "//ul/li")
post_count = stats[0].text.split(" ")[0]
followers = stats[1].text.split(" ")[0]
following = stats[2].text.split(" ")[0]

print("Full Name:", full_name)
print("Bio:", bio)
print("Posts:", post_count)
print("Followers:", followers)
print("Following:", following)

# ------------------------------
# 4. SCROLL AND COLLECT POST URLs
# ------------------------------

post_urls = set()
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    for link in links:
        post_urls.add(link.get_attribute("href"))

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2 + random.random() * 2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

print(f"Collected {len(post_urls)} post URLs")

# ------------------------------
# 5. DOWNLOAD IMAGES / VIDEOS
# ------------------------------

output_folder = f"instagram_{username_to_scrape}"
os.makedirs(output_folder, exist_ok=True)

for i, post_url in enumerate(post_urls):
    driver.get(post_url)
    time.sleep(2 + random.random())

    # Image
    try:
        img_elem = driver.find_element(By.XPATH, "//img[@decoding='auto']")
        img_url = img_elem.get_attribute("src")

        img_data = requests.get(img_url).content
        with open(os.path.join(output_folder, f"post_{i+1}.jpg"), "wb") as f:
            f.write(img_data)
    except:
        print(f"No image found for {post_url}")

    # Video
    try:
        video_elem = driver.find_element(By.TAG_NAME, "video")
        video_url = video_elem.get_attribute("src")

        video_data = requests.get(video_url).content
        with open(os.path.join(output_folder, f"post_{i+1}.mp4"), "wb") as f:
            f.write(video_data)
    except:
        pass

# ------------------------------
# 6. SAVE EVERYTHING TO CSV
# ------------------------------

df = pd.DataFrame({
    "post_url": list(post_urls)
})
df.to_csv(os.path.join(output_folder, "posts.csv"), index=False)

profile_info = {
    "username": username_to_scrape,
    "full_name": full_name,
    "bio": bio,
    "followers": followers,
    "following": following,
    "post_count": post_count
}

profile_df = pd.DataFrame([profile_info])
profile_df.to_csv(os.path.join(output_folder, "profile_info.csv"), index=False)

driver.quit()

print(f"[INFO] All images/videos for '{username_to_scrape}' saved in {output_folder}.")