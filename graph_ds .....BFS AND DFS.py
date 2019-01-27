class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    def addEdges(self,edge):
        edge=set(edge)
        (vertx1,vertx2)=tuple(edge)
    
        if vertx1 in self.gdict:
            self.gdict[vertx1].append(vertx2)
        else:
            self.gdict[vertx1]=[vertx2]
            
    def getEdges(self):
        return self.findedges()
        
            
    def findedges(self):
        edges=[]
        for nodes in self.gdict:
            for negh in self.gdict[nodes]:
                if{negh,nodes} not in edges:
                    edges.append((nodes,negh))
        return edges
    
        
#breadth first Search 
    def bfs(self,s,visted=[]):
        que=[s]
        while que:
            node=que.pop(0)
            if node not in visted:
                visted.append(node)
                for j in self.gdict[node]:
                    que.append(j)
        return visted
    
#Deapth Firse Search
    def dfs(self,startnode,visi=[]):
        if startnode not in visi:
            visi.append(startnode)
            for i in self.gdict[startnode]:
                self.dfs(i,visi)
        return visi
#             '
        
graph_elements = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C'] 
        }
       
g = graph(graph_elements)

print("Edges:- "+str(g.getEdges()))
print("Vertices:- "+str(g.getVertices()))
print("BFS:- "+str(g.bfs('A')))
print("DFS:-"+str(g.dfs('A')))

