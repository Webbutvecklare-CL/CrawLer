import requests
from bs4 import BeautifulSoup
from Page import Page
from Page import getPageWithUrl
from Page import rankPages
from IndexedRoutes import IndexedRoutes
import Sitemapper as sm

indexedRoutes = IndexedRoutes()
pages = []

def getLinksInPage(url, excludedTags=[]):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful HTTP requests
        if not getPageWithUrl(url, pages):
            pages.append(Page(url))

        soup = BeautifulSoup(response.content, 'html.parser').find('body')
        for tag in excludedTags:
            soup.find(tag).decompose()

        links = soup.find_all('a')  # Find all anchor tags


        hyperlinks = []
        for link in links:
            href = link.get('href')
            if href and href.startswith('/') and "/aktuellt/" not in href:
                url_end = url.split('/')[-1]
                if url_end == href.split('/')[1]:
                    hyperlinks.append(url + href[1:].removeprefix(url_end))
                else:
                    hyperlinks.append(url + href[1:])

        indexedRoutes.addRoute(url)
        return hyperlinks

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []
    
def index(link):
    if link == "https://www.cl-sektionen.se/":
        routes = getLinksInPage(link)
    else: 
        routes = getLinksInPage(link, ['header', 'footer'])

    page = getPageWithUrl(link, pages)
    if not page:
        return

    page.addLinks(routes)

    for link in page.linksTo:
        if not indexedRoutes.isIndexed(link):
            index(link)

def main():
    webpage_url = "https://www.cl-sektionen.se/"
    print("indexing...")
    index(webpage_url)
    print("ranking...")
    rankPages(pages)

    print("")
    print("RANKINGS__________________________________")
    pages.sort(reverse=True)
    for p in pages:
        print(p.printStr())

    print("Creating sitemap...")
    sm.createGraph(pages)
    input("[DONE] Press Enter to close window...")

if __name__ == "__main__":
    main()
    