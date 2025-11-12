#find the user name from url

import re
 
url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?instagram\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:",matches.group(1))

