import requests
from bs4 import BeautifulSoup
import csv

# Example job board (replace this with the actual one you want)
url = "https://www.seek.com.au/jobs-in-construction"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

companies = []
for job in soup.select(".job-card"):  # <- You'll need to adjust this based on the real HTML
    name = job.select_one(".company-name").text.strip()
    website = job.select_one("a")["href"]
    companies.append([name, website])

with open("companies.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Website"])
    writer.writerows(companies)

print("Done scraping.")
