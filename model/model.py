import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.porzioni=DAO.getAllPorzioni()
        self.grafo = nx.Graph()
        self._idMap = {}
        self.dict = {}
        self.nodi=[]
        self._solBest = []
        self._costBest = 0


    def creaGrafo(self,calorie):
        self.nodi = DAO.getNodi(calorie)
        self.grafo.add_nodes_from(DAO.getNodi(calorie))
        self.addEdges( )
        return self.grafo

    def addEdges(self):
         self.grafo.clear_edges()
         allEdges = DAO.getConnessioni()
         for connessione in allEdges:
             nodo1 = connessione.v1
             nodo2 = connessione.v2
             if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                 if self.grafo.has_edge(nodo1, nodo2) == False:
                     self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def analisi(self, porzione):
        dizio={}
        for porzioni in self.grafo.neighbors(porzione):
            dizio[porzioni]=self.grafo[porzioni][porzione]["weight"]
        return dizio

    def getBestPath(self, npassi, v0):
        self._solBest = []
        self._costBest = 0
        parziale = [v0]
        for v in self.grafo.neighbors(v0):
            parziale.append(v)
            self.ricorsione(parziale,npassi)
            parziale.pop()
        return self._solBest, self._costBest

    def ricorsione(self, parziale,npassi):
        # Controllo se parziale è una sol valida, ed in caso se è migliore del best
        if len(parziale)-1==npassi:
            if self.peso(parziale)>self._costBest:
                self._costBest = self.peso(parziale)
                self._solBest = copy.deepcopy(parziale)

        if len(parziale)-1<npassi:
            for v in self.grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale,npassi)
                    parziale.pop()
    def peso(self,parziale):
        peso=0
        for i in range(0,len(parziale)-1):
            peso+=self.grafo[parziale[i]][parziale[i+1]]["weight"]
        return peso
