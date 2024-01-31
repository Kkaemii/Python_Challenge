import requests
from bs4 import BeautifulSoup

all_jobs = []


def scrape_page(url):
    print(f"scraping...{url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    for job in jobs:
        title = job.find("span", class_="title").text
        region = job.find("span", class_="region").text
        companies = job.find("span", class_="company").text
        url = job.find("div", class_="tooltip").next_sibling["href"]
        # (title, region, companies)
        # print(f"-----------------\n title: {title}\n region: {region}\n company: {companies}")

        job_data = {
            "title": title,
            "region": region,
            "companies": companies,
            "url": f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)


def get_pages(url):
    response = requests.get(
        "https://weworkremotely.com/remote-full-time-jobs?page=1")
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all(
        "span", class_="page"))


total_pages = get_pages(
    "https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))