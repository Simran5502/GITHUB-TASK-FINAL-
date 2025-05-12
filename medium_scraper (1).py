
import os
import requests
from bs4 import BeautifulSoup

def scrape_medium_article(url):
    # Send HTTP request to the Medium article
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the article")
        return

  
    soup = BeautifulSoup(response.text, 'html.parser')


    paragraphs = soup.find_all('p')
    article_text = '\n'.join([para.get_text() for para in paragraphs])

    
    folder_name = "scraped_articles"
    os.makedirs(folder_name, exist_ok=True)

 
    file_path = os.path.join(folder_name, "medium_article.txt")
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(article_text)

    print(f"Article successfully saved to {file_path}")


medium_url = "https://medium.com/personal-growth/the-only-productivity-hack-you-need-1794f68c43a1"
scrape_medium_article(medium_url)
