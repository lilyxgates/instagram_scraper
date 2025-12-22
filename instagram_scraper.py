# ============================================
# Instagram Scraper
# Author: Lily Gates
# Created: 12/22/2025
# Last Updated 12/22/2025

# Description:
# TBD

# Features:
# - TBD
# ============================================

import os
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests import get
from urllib.parse import urljoin
import json

# --------------------------------------------
# STEP 1: SCRAPE DATA
# --------------------------------------------

# URLs for scraping
url = 'https://www.instagram.com/jimmyvanhout/'  # Profile to scrape
base_url = 'https://www.instagram.com'         # Base Instagram URL

# Retrieve and parse the site content
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.instagram.com/"
}
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# --------- #
# HEADER    #
# --------- #

# Find the JSON script tag (older "_sharedData" example)
script_tag = soup.find('script', text=lambda t: t and 'window._sharedData' in t)
if script_tag:
    shared_data = script_tag.string.partition('=')[-1].strip(' ;')
    data = json.loads(shared_data)

    user = data['entry_data']['ProfilePage'][0]['graphql']['user']

    print("Username:", user['username'])
    print("Full Name:", user['full_name'])
    print("Bio:", user['biography'])
    print("Followers:", user['edge_followed_by']['count'])
    print("Following:", user['edge_follow']['count'])
    print("Profile Picture:", user['profile_pic_url_hd'])

"""

# Contains username, "real" name, bio description, posts/followers/following count (type: grid)
<header class="xrvj5dj xl463y0 x1ec4g5p xdj266r xwy3nlu xh8yej3">

# --- Profile Picture --- #

# Contains profile picture (type: flex)
<section class="x6s0dn4 x78zum5 xcrlgei x1cq0mwf xdx80a7 x1agbcgv xl56j7k xlo4toe x2wt2w">
<div class="x6s0dn4 x78zum5 xdt5ytf x1iyjqo2 x2lah0s xl56j7k x1n2onr6"><span aria-describedby="_r_1c_" class="html-span xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1hl2dhg x16tdsg8 x1vvkbs x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j"><div><div class="x6s0dn4 xamitd3 x1lliihq xl56j7k x1n2onr6"><a class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xc5r6h4 xqeqjp1 x1phubyo x13fuv20 x18b5jzi x1q0q8m5 x1t7ytsu x972fbf x10w94by x1qhh985 x14e42zd x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s x3ct3a4 xdj266r x14z9mp xat24cr x1lziwak x2lwn1j xeuugli xexx8yu xyri2b x18d9i69 x1c1uobl x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x1c9tyrk xeusxvb x1pahc9y x1ertn4p x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 xzfakq xhihtb0 x1j8hi7x x172hklt xrw4ojt xg6frx5 xw872ko xhgbb2x xynf4tj xdjs2zz x1r9ni5o xvsnedh xoiy6we x16ouz9t x1qj619r xsrjr5h x1xrz1ek x1s928wv x1unh1gc x1iygr5g x2q1x1w x1j6awrg x1m1drc7 x1ypdohk x4gyw5p _a6hd" href="/jimmyvanhout/" role="link" tabindex="0" style="height: 77px; width: 77px;"><img alt="jimmyvanhout's profile picture" class="xpdipgo x972fbf x10w94by x1qhh985 x14e42zd xk390pu x5yr21d xdj266r x14z9mp xat24cr x1lziwak xl1xv1r xexx8yu xyri2b x18d9i69 x1c1uobl x11njtxf xh8yej3" crossorigin="anonymous" draggable="false" src="https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/460387674_1695126981322143_5835671345411172243_n.jpg?stp=dst-jpg_s150x150_tt6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_cat=103&amp;_nc_oc=Q6cZ2QEHChPVi34LA0xLoMaGLT3hAPMCPziEFDTblNMfDyEfnYcXZtcA9Xd777ngf7PG1UhDylAo3GeEm4WVYuL5PXVl&amp;_nc_ohc=tefTFQMcbM0Q7kNvwGyplG5&amp;_nc_gid=C60tbUuE19dkXBiE7ZBy5g&amp;edm=AP4sbd4BAAAA&amp;ccb=7-5&amp;oh=00_AfmGTQfF7-_1MERioJLRjjr5bv27NOB5O58weHka4cjXGw&amp;oe=694F66AF&amp;_nc_sid=7a9f4b"></a></div></div></span></div>
<span aria-describedby="_r_1c_" class="html-span xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1hl2dhg x16tdsg8 x1vvkbs x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j"><div><div class="x6s0dn4 xamitd3 x1lliihq xl56j7k x1n2onr6"><a class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xc5r6h4 xqeqjp1 x1phubyo x13fuv20 x18b5jzi x1q0q8m5 x1t7ytsu x972fbf x10w94by x1qhh985 x14e42zd x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s x3ct3a4 xdj266r x14z9mp xat24cr x1lziwak x2lwn1j xeuugli xexx8yu xyri2b x18d9i69 x1c1uobl x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x1c9tyrk xeusxvb x1pahc9y x1ertn4p x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 xzfakq xhihtb0 x1j8hi7x x172hklt xrw4ojt xg6frx5 xw872ko xhgbb2x xynf4tj xdjs2zz x1r9ni5o xvsnedh xoiy6we x16ouz9t x1qj619r xsrjr5h x1xrz1ek x1s928wv x1unh1gc x1iygr5g x2q1x1w x1j6awrg x1m1drc7 x1ypdohk x4gyw5p _a6hd" href="/jimmyvanhout/" role="link" tabindex="0" style="height: 77px; width: 77px;"><img alt="jimmyvanhout's profile picture" class="xpdipgo x972fbf x10w94by x1qhh985 x14e42zd xk390pu x5yr21d xdj266r x14z9mp xat24cr x1lziwak xl1xv1r xexx8yu xyri2b x18d9i69 x1c1uobl x11njtxf xh8yej3" crossorigin="anonymous" draggable="false" src="https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/460387674_1695126981322143_5835671345411172243_n.jpg?stp=dst-jpg_s150x150_tt6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_cat=103&amp;_nc_oc=Q6cZ2QEHChPVi34LA0xLoMaGLT3hAPMCPziEFDTblNMfDyEfnYcXZtcA9Xd777ngf7PG1UhDylAo3GeEm4WVYuL5PXVl&amp;_nc_ohc=tefTFQMcbM0Q7kNvwGyplG5&amp;_nc_gid=C60tbUuE19dkXBiE7ZBy5g&amp;edm=AP4sbd4BAAAA&amp;ccb=7-5&amp;oh=00_AfmGTQfF7-_1MERioJLRjjr5bv27NOB5O58weHka4cjXGw&amp;oe=694F66AF&amp;_nc_sid=7a9f4b"></a></div></div></span>
<div class="x6s0dn4 xamitd3 x1lliihq xl56j7k x1n2onr6"><a class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xc5r6h4 xqeqjp1 x1phubyo x13fuv20 x18b5jzi x1q0q8m5 x1t7ytsu x972fbf x10w94by x1qhh985 x14e42zd x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s x3ct3a4 xdj266r x14z9mp xat24cr x1lziwak x2lwn1j xeuugli xexx8yu xyri2b x18d9i69 x1c1uobl x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x1c9tyrk xeusxvb x1pahc9y x1ertn4p x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 xzfakq xhihtb0 x1j8hi7x x172hklt xrw4ojt xg6frx5 xw872ko xhgbb2x xynf4tj xdjs2zz x1r9ni5o xvsnedh xoiy6we x16ouz9t x1qj619r xsrjr5h x1xrz1ek x1s928wv x1unh1gc x1iygr5g x2q1x1w x1j6awrg x1m1drc7 x1ypdohk x4gyw5p _a6hd" href="/jimmyvanhout/" role="link" tabindex="0" style="height: 77px; width: 77px;"><img alt="jimmyvanhout's profile picture" class="xpdipgo x972fbf x10w94by x1qhh985 x14e42zd xk390pu x5yr21d xdj266r x14z9mp xat24cr x1lziwak xl1xv1r xexx8yu xyri2b x18d9i69 x1c1uobl x11njtxf xh8yej3" crossorigin="anonymous" draggable="false" src="https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/460387674_1695126981322143_5835671345411172243_n.jpg?stp=dst-jpg_s150x150_tt6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_cat=103&amp;_nc_oc=Q6cZ2QEHChPVi34LA0xLoMaGLT3hAPMCPziEFDTblNMfDyEfnYcXZtcA9Xd777ngf7PG1UhDylAo3GeEm4WVYuL5PXVl&amp;_nc_ohc=tefTFQMcbM0Q7kNvwGyplG5&amp;_nc_gid=C60tbUuE19dkXBiE7ZBy5g&amp;edm=AP4sbd4BAAAA&amp;ccb=7-5&amp;oh=00_AfmGTQfF7-_1MERioJLRjjr5bv27NOB5O58weHka4cjXGw&amp;oe=694F66AF&amp;_nc_sid=7a9f4b"></a></div>
<a class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xc5r6h4 xqeqjp1 x1phubyo x13fuv20 x18b5jzi x1q0q8m5 x1t7ytsu x972fbf x10w94by x1qhh985 x14e42zd x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s x3ct3a4 xdj266r x14z9mp xat24cr x1lziwak x2lwn1j xeuugli xexx8yu xyri2b x18d9i69 x1c1uobl x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x1c9tyrk xeusxvb x1pahc9y x1ertn4p x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 xzfakq xhihtb0 x1j8hi7x x172hklt xrw4ojt xg6frx5 xw872ko xhgbb2x xynf4tj xdjs2zz x1r9ni5o xvsnedh xoiy6we x16ouz9t x1qj619r xsrjr5h x1xrz1ek x1s928wv x1unh1gc x1iygr5g x2q1x1w x1j6awrg x1m1drc7 x1ypdohk x4gyw5p _a6hd" href="/jimmyvanhout/" role="link" tabindex="0" style="height: 77px; width: 77px;"><img alt="jimmyvanhout's profile picture" class="xpdipgo x972fbf x10w94by x1qhh985 x14e42zd xk390pu x5yr21d xdj266r x14z9mp xat24cr x1lziwak xl1xv1r xexx8yu xyri2b x18d9i69 x1c1uobl x11njtxf xh8yej3" crossorigin="anonymous" draggable="false" src="https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/460387674_1695126981322143_5835671345411172243_n.jpg?stp=dst-jpg_s150x150_tt6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_cat=103&amp;_nc_oc=Q6cZ2QEHChPVi34LA0xLoMaGLT3hAPMCPziEFDTblNMfDyEfnYcXZtcA9Xd777ngf7PG1UhDylAo3GeEm4WVYuL5PXVl&amp;_nc_ohc=tefTFQMcbM0Q7kNvwGyplG5&amp;_nc_gid=C60tbUuE19dkXBiE7ZBy5g&amp;edm=AP4sbd4BAAAA&amp;ccb=7-5&amp;oh=00_AfmGTQfF7-_1MERioJLRjjr5bv27NOB5O58weHka4cjXGw&amp;oe=694F66AF&amp;_nc_sid=7a9f4b"></a>
<img alt="jimmyvanhout's profile picture" class="xpdipgo x972fbf x10w94by x1qhh985 x14e42zd xk390pu x5yr21d xdj266r x14z9mp xat24cr x1lziwak xl1xv1r xexx8yu xyri2b x18d9i69 x1c1uobl x11njtxf xh8yej3" crossorigin="anonymous" draggable="false" src="https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/460387674_1695126981322143_5835671345411172243_n.jpg?stp=dst-jpg_s150x150_tt6&amp;efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&amp;_nc_ht=scontent-iad3-2.cdninstagram.com&amp;_nc_cat=103&amp;_nc_oc=Q6cZ2QEHChPVi34LA0xLoMaGLT3hAPMCPziEFDTblNMfDyEfnYcXZtcA9Xd777ngf7PG1UhDylAo3GeEm4WVYuL5PXVl&amp;_nc_ohc=tefTFQMcbM0Q7kNvwGyplG5&amp;_nc_gid=C60tbUuE19dkXBiE7ZBy5g&amp;edm=AP4sbd4BAAAA&amp;ccb=7-5&amp;oh=00_AfmGTQfF7-_1MERioJLRjjr5bv27NOB5O58weHka4cjXGw&amp;oe=694F66AF&amp;_nc_sid=7a9f4b">


##################################
# Extract anchor tags containing Pokémon names and links
anchor_elem = content.select('a[class="ent-name"]')

# Get list of Pokémon names
pokemon_names = [x.string for x in anchor_elem]

# Create list of full URLs to individual Pokémon pages
completed_links = [urljoin(base_url, a.get('href')) for a in anchor_elem]

"""