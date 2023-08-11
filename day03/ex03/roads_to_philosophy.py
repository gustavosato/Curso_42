import sys
import requests
from bs4 import BeautifulSoup

def search_wiki(url):
    try:
        response = requests.get(url) #realiza a requisição para o site
        response.raise_for_status() #armazena a mensagem de status do site
        soup = BeautifulSoup(response.text, "html.parser") #monta a estrutura html para procurar elementos especificos

        main_title = soup.find("h1", id="firstHeading").text.strip() #extrai o titulo principal da pagina

        # Find the first valid link in the introduction paragraph
        for id_valido in soup.find(id='mw-content-text'): #encontra o primeiro link valido
            if not id_valido: #caso o link não exista, então irá para a condição de exceção
                pass
            for paragraph in id_valido.find_all("p", recursive=False): #busca todos os elementos com <p>, somente os paragrafos principais e não os aninhados
                for link in paragraph.find_all("a", href=True):#busca todos os elementos com <a>, considerando somente aqueles que possuem o href
                    if link.get('href') is not None and link['href'].startswith('/wiki/')\
                        and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):# valida se o href não é nulo, se começa com /wiki/ e se o link não começa com /wiki/Wikipedia: ou com /wiki/Help:
                        return link["href"], main_title #retorna parte da url valida e o titulo da pagina

    except requests.HTTPError as e:
        if (response.status_code == 404): #caso o status code seja 404, irá retornar uma mensagem de erro
                return print("It's a dead end !")
        return print(e)

def main():

    if len(sys.argv) != 2:
        print("Número de argumentos inválido") #valida a quantidade de argumentos
        return
    
    page_title = sys.argv[1] #pega o primeiro argumento
    visited_articles = [] #lista_vazia de artigos
    total_count = 0 #contador de rotas ate o philosophy
    current_url = f"https://en.wikipedia.org/wiki/{page_title}" #url do wikipedia

    while True: #iteração para buscar no wikipedia o argumento passado
        if not search_wiki(current_url): #valida se a url retornou uma lista vazia
            break #para a iteração
        else:
            link, title = search_wiki(current_url) #retorna o conteudo da pagina e armazena nas variaveis de link e title

            print(title) #imprimi na tela todos os titulos percorridos
        
            if title == "Philosophy": #valida se chegou no titulo Philosophy
                print(f"{total_count} roads from {page_title} to philosophy") #imprimi na tela quantas rotas foram chamadas do tittle ate o philosofhy
                break

            if link in visited_articles: #verifica se ja passou pelo link alguma vez
                print("It leads to an infinite loop !")
                break

            visited_articles.append(link) #adiciona a lista de artigos visitados
            total_count += 1 #adiciona mais 1 a cada iteração para ter a contagem de rotas
            current_url = f"https://en.wikipedia.org{link}" #atualiza o current_url com o proximo link

if __name__ == "__main__":
    main()
