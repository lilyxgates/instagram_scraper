"""
# ============================================

# Instagram Scraper
# Author: Lily Gates
# Created: 12/22/2025
# Last Updated 12/22/2025

# Description:
# TBD

# Features:
# - TBD

# Notes:
Selenium can only see private accounts if:
- You are logged in to Instagram
- You already follow the private account
- Selenium uses your existing Chrome profile
If any of those are false, Instagram will still hide the content.

# ============================================
"""

import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# ------------------------------
# 1️⃣ SETUP CHROME + SELENIUM
# ------------------------------

chrome_username = lilyxgates@gmail.com

chrome_options = Options()
# Use your real Chrome profile
chrome_options.add_argument(
    f"--user-data-dir=/Users/{chrome_username}/Library/Application Support/Google/Chrome"
)

chrome_options.add_argument("--profile-directory=Default")
# chrome_options.add_argument("--headless=new")  # optional

service = Service("/path/to/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

