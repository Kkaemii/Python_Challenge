import requests
from bs4 import BeautifulSoup

all_jobs = []
skills = ["python", "typescript", "javascript"]


def scrape_page(url):
    print(f"scraping...{url}")
    response = requests.get(url,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                            }
                            )
    soup = BeautifulSoup(response.content, "html.parser")
    job_list = soup.find_all("li", class_="bjs-jlid")[1:-1]

    for job in job_list:
        company_name = job.find("a", class_="bjs-jlid__b").text
        job_title = job.find("h4", class_="bjs-jlid__h").text
        job_des = job.find("div", class_="bjs-jlid__description").text
        job_link = job.find("h4", class_="bjs-jlid__h").find("a")['href']

        job_data = {
            "company_name": company_name,
            "job_title": job_title,
            "job_description": job_des,
            "job_link": job_link
        }
        all_jobs.append(job_data)


def get_pages(url):
    response = requests.get(url,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                            }
                            )
    soup = BeautifulSoup(response.content, "html.parser")
    test = int(soup.find("a", class_="page-numbers").text)
    return test


user_input = input("  원하는 정보를 입력하세요. basic, python, typescript, javascript  ")


if user_input == "basic":
    input_url = 'https://berlinstartupjobs.com/engineering/page/1/'
    total_pages = get_pages(input_url)

    for x in range(total_pages):  # 2페이지라서 for사용
        url = f"https://berlinstartupjobs.com/engineering/page/{x+1}/"
        scrape_page(url)
else:  # 나머지는 단일페이지
    input_url = f'https://berlinstartupjobs.com/skill-areas/{user_input}/'
    # Scrape single page
    scrape_page(input_url)

print(all_jobs)