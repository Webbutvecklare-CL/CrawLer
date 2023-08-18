class Page:
    def __init__(self, url):
        self.url = url
        self.name = url.split("/")[-1]
        self.linksTo = []
        self.linkedFrom = []
        self.rating = 0
    
    def getURL(self):
        return self.url
    
    def getName(self):
        return self.name
    
    def addLinks(self, links):
        self.linksTo = links

    def increaseRating(self):
        self.rating += 1

    def __str__(self) -> str:
        return self.name
    
    def printStr(self) -> str:
        if self.name:
            return f"Page: {self.name}\nRating: {str(self.rating)}\nLinks to: {str(self.linksTo)}\nLinked from: {str(self.linkedFrom)}\n"
    
    def __lt__(self, other):
        return self.rating < other.rating


def getPageWithUrl(url, pages):
    for page in pages:
        if page.getURL() == url:
            return page

def rankPages(pages):
    for page in pages:
        for link in page.linksTo:
            p = getPageWithUrl(link, pages)
            p.increaseRating()
            p.linkedFrom.append(page.getURL())