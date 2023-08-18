import networkx as nx
from pyvis.network import Network
from Page import getPageWithUrl

def createGraph(pages):
    G = nx.DiGraph()
    for p in pages:
        G.add_node(p.name, size= p.rating * 10, color= "#bb291d")
    for p in pages:
        for l in p.linksTo:
            G.add_edge(p.name, getPageWithUrl(l, pages).name, color="#8a2419")

    net = Network("1000px", "100%", directed=True)
    net.from_nx(G)

    net.show("Sitemap.html", notebook=False)