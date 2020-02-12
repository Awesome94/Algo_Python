class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def getVertices(self):
        return list(self.gdict.keys())
    
    def edges(self):
        return self.findedges()
    
    def findedges(self):
        edgename = []
        for vrtx in self.gdict.items:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({nxtvrtx, vrtx})
        return edgename  

    def addVertex(self, vrtx):
        if vrtx not in self.gdict.keys():
            self.gdict[vrtx] = []
    
    