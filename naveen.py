import requests
from bs4 import BeautifulSoup

def get_github_repo_data(repo_url):
    # Set headers to mimic a browser to avoid simple bot blocks
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get(repo_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Extract Repo Name (usually in a h1 with class "public")
        repo_name = soup.select_one('[itemprop="name"]').text.strip()
        
        # 2. Extract Description (found in the "About" section)
        # Often a <p> inside a div with class "BorderGrid-cell"
        description_element = soup.select_one('.BorderGrid-cell p.f4')
        description = description_element.text.strip() if description_element else "No description"
        
        # 3. Extract Stars (using the octicon-star as a landmark)
        star_link = soup.select_one('a[href$="/stargazers"]')
        stars = star_link.select_one('strong').text.strip() if star_link else "0"
        
        print(f"Project: {repo_name}")
        print(f"About: {description}")
        print(f"Stars: {stars}")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")

# Usage
get_github_repo_data('https://github.com/vlakshmiprasad/python_tutorial_April2026')
