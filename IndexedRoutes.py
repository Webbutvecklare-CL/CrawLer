class IndexedRoutes:
    def __init__(self) -> None:
        self.indexedRoutes = []
    
    def addRoute(self, route):
        self.indexedRoutes.append(route)

    def __str__(self) -> str:
        return str(self.indexedRoutes)
    
    def isIndexed(self, route):
        return route in self.indexedRoutes