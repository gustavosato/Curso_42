import sys
import requests
import json
import dewiki

def get_page_content(page_title):
    base_url = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        'action': 'parse',
        'format': 'json',
        'prop': 'wikitext',
        'page': page_title,
        'redirects': 'true'
    }

    response = requests.get(base_url, params=PARAMS)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        if 'parse' in data:
            return (dewiki.from_string(data["parse"]["wikitext"]["*"]))
    
    return None
            
def main():
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py 'page_title'")
        return
    
    page_title = sys.argv[1]

    page_content = get_page_content(page_title)
    
    if page_content:
        file_name = page_title.replace(' ', '_') + '.wiki'
        
        with open(f"{file_name}", 'w', encoding='utf-8') as file:
            file.write(page_content)
        
        print("Conteudo salvo no arquivo:", file_name)
    else:
        print("Error: conteudo não encontrado")

if __name__ == '__main__':
    main()