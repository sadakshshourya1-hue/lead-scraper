import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

# Browser headers
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

results = []

# Read websites
try:
    with open("urls.txt", "r") as file:
        urls = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("urls.txt not found!")
    exit()

if not urls:
    print("urls.txt is empty!")
    exit()

successful = 0
failed = 0

for url in urls:

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15,
            allow_redirects=True
        )

        response.raise_for_status()

        final_url = response.url

        soup = BeautifulSoup(response.text, "html.parser")
        html = response.text

        title = soup.title.string.strip() if soup.title else "No Title"

        emails = sorted(set(re.findall(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            html
        )))

        instagram = "Not Found"
        linkedin = "Not Found"
        facebook = "Not Found"
        contact = "Not Found"

        for tag in soup.find_all("a", href=True):

            href = tag["href"]

            if href.startswith("/"):
                href = final_url.rstrip("/") + href

            href_lower = href.lower()

            if "instagram.com" in href_lower:
                instagram = href

            elif "linkedin.com" in href_lower:
                linkedin = href

            elif "facebook.com" in href_lower:
                facebook = href

            if "contact" in href_lower:
                contact = href

        results.append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Company": title,
            "Website": final_url,
            "Emails": ", ".join(emails) if emails else "Not Found",
            "Email Count": len(emails),
            "Instagram": instagram,
            "LinkedIn": linkedin,
            "Facebook": facebook,
            "Contact Page": contact
        })

        successful += 1
        print(f"✔ Successfully scraped: {final_url}")

    except Exception as e:
        failed += 1
        print(f"✖ Failed: {url}")
        print(f"  Reason: {e}")

# Save CSV
df = pd.DataFrame(results)
df.to_csv("leads.csv", index=False)

print("\n========== SUMMARY ==========")
print(f"Total Websites : {len(urls)}")
print(f"Successful     : {successful}")
print(f"Failed         : {failed}")
print("CSV Saved As   : leads.csv")
print("=============================\n")

if not df.empty:
    print(df)