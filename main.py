import requests
from bs4 import BeautifulSoup

def get_title_and_description(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string if soup.title else 'No title found'
        description = ''
        
        meta = soup.find('meta', attrs={'name': 'description'})
        if meta and 'content' in meta.attrs:
            description = meta['content']
        else:
            description = 'No description found'
        
        return title, description
    except requests.RequestException as e:
        return 'Error', str(e)

def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

def save_results(results, file_path):
    with open(file_path, 'w') as file:
        for result in results:
            file.write(f"URL: {result['url']}\n")
            file.write(f"Title: {result['title']}\n")
            file.write(f"Description: {result['description']}\n")
            file.write('-' * 40 + '\n')

def main():
    urls = read_urls('urls.txt')
    results = []
    
    for url in urls:
        title, description = get_title_and_description(url)
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print('-' * 40)
        
        results.append({
            'url': url,
            'title': title,
            'description': description
        })
    
    save_results(results, 'results.txt')

main()

#push it 
