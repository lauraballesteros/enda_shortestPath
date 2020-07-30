#create the map

from collections import defaultdict
import re
from multiprocessing import Pool, Process
from time import time
from os import getpid
import pickle




def checkTraffic(cost,traffic):
    if traffic == 'heavy\n':
        cost = cost*1.2
    elif traffic == 'light':
        cost = cost*0.8
    cost=int(cost)
    
    return cost


f = open("example.txt", "r")
f=f.readlines()
edges=[]
for line in f:
    if re.match("^(n|N)[0-9]+$", line):
        continue
    else:
        (var1, var2, var3, var4) = line.split(",")
        var3=int(var3)
        cost=checkTraffic(var3,var4)
        edges.append((var1,var2,cost))



class Graph():
    def __init__(self):
        self.edges=defaultdict(list)
        self.cost_btw_nodes={}
    def addEdge(self,origin,destiny,cost):
        self.edges[origin].append(destiny)
        self.edges[destiny].append(origin)

        self.cost_btw_nodes[(origin,destiny)]=cost
        self.cost_btw_nodes[(destiny,origin)]=cost

    def buildGraph(self,edges):
        for element in edges:
            self.addEdge(*element)
        newFile="final.txt"
        with open(newFile,'wb') as fp:
            pickle.dump(edges,fp,pickle.HIGHEST_PROTOCOL)
        with open(newFile, 'rb') as fp:
            edgesLoaded = pickle.load(fp)
       

    def findingSP(self,nodes):
        print(f"--- Process {getpid()} ---")

        origin=nodes[0]
        destiny=nodes[1]
        shortestPath={origin:(None,0)}
        current=origin
        visited= set()

        while current!= destiny:
            visited.add(current)
            neighbors=self.edges[current]
            cost_to_current=shortestPath[current][1]

            for nextt in neighbors:
                cost=self.cost_btw_nodes[(current,nextt)] + cost_to_current
                if nextt not in shortestPath:
                    shortestPath[nextt]=(current,cost)
                else:
                    current_shortest_cost= shortestPath[nextt][1]
                    if current_shortest_cost > cost:
                        shortestPath[nextt]= (current,cost)

            for element in shortestPath:
                if element not in visited:
                    nextt_destination={element:shortestPath[element]}

            if not nextt_destination:
                print("Woops! , we could not find you the right route,sorry!")
            
            
            current=min(nextt_destination,key=lambda k:nextt_destination[k][1])

        path=[]
        while current is not None:
            path.insert(0,current)
            nextt=shortestPath[current][0]
            current=nextt

        return path


def main():
    u_nodes=[]
    routes=int(input("Enter how many routes you want to check: "))
    for _ in range(routes):
        u_origin=input("Please enter the origin: ")
        u_destiny=input("Please enter the destination: ")
        u_nodes.append((u_origin,u_destiny))

    g= Graph()
    g.buildGraph(edges)

    p = Pool()
    start = time()
    res =  p.map(g.findingSP, u_nodes)
    p.close()
    
    print(f'Time: {time() - start} s')
    print(res)
    
if __name__ == "__main__":
    main()
