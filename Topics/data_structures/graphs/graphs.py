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
    
    # def AddEdge(self, edge):
    #     edge = set(edge)
    #     (vrtx1, vrtx2) = tuple(edge)
    #     if vrtx1 in self.gdict:
    #         self.gdict[vrtx1].append(vrtx2)
    #     else:
    #         self.gdict[vrtx1] = [vrtx2]
    
    def AddEdge(self, edge):
        edge = set(edge)
        for vrtx in edge:
            if vrtx in self.gdict:
                self.gdict[vrtx].append(vrtx)
            else:
                self.gdict[vrtx] = []
