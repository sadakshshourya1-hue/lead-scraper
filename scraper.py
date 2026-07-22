import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = input("Enter website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    response = requests.get(
        url,
        timeout=10,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    html = response.text

    title = soup.title.string.strip() if soup.title else "No Title"

    # Emails
    emails = sorted(list(set(re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        html
    ))))

    instagram = ""
    linkedin = ""
    facebook = ""
    contact_page = ""

    for link in soup.find_all("a", href=True):

        href = link["href"]

        if href.startswith("/"):
            href = url.rstrip("/") + href

        if "instagram.com" in href:
            instagram = href

        elif "linkedin.com" in href:
            linkedin = href

        elif "facebook.com" in href:
            facebook = href

        if "contact" in href.lower():
            contact_page = href

    data = {
        "Company": [title],
        "Website": [url],
        "Emails": [", ".join(emails) if emails else "Not Found"],
        "Instagram": [instagram if instagram else "Not Found"],
        "LinkedIn": [linkedin if linkedin else "Not Found"],
        "Facebook": [facebook if facebook else "Not Found"],
        "Contact Page": [contact_page if contact_page else "Not Found"]
    }

    df = pd.DataFrame(data)

    df.to_csv("leads.csv", index=False)

    print("\nLead saved successfully!\n")
    print(df)

except Exception as e:
    print("Error:", e)