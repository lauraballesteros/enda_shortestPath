#create the map
#need to update the edges with the .txt file later
from collections import defaultdict
edges=[
    ("n0","n1",5),
    ("n1","n5",1),
    ("n1","n4",3),
    ("n2","n3",1),
    ("n2","n6",5),
    ("n3","n4",9),
    ("n4","n3",9),
    ("n4","n6",12)
]

class Graph():
    def __init__(self):
        self.edges=defaultdict(list)
        self.cost_btw_nodes={}
    def addEdge(self,origin,destiny,cost):
        self.edges[origin].append(destiny)
        self.edges[destiny].append(origin)

        self.cost_btw_nodes[(origin,destiny)]=cost
        self.cost_btw_nodes[(destiny,origin)]=cost

mapp=Graph()

for element in edges:
    mapp.addEdge(*element)

#implementing dijsktra

def findingSP(mapp,origin,destiny):
    shortestPath={origin:(None,0)}
    current=origin
    visited= set()

    while current!= destiny:
        print("current:",current)
        visited.add(current)
        neighbors=mapp.edges[current]
        print("neighbors of current",neighbors)
        cost_to_current=shortestPath[current][1]

        for nextt in neighbors:
            cost=mapp.cost_btw_nodes[(current,nextt)] + cost_to_current
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
            print("ups, we could not find you the right route,sorry!")
        
        print("next poss destinations:",nextt_destination)
        
        current=min(nextt_destination,key=lambda k:nextt_destination[k][1])
        print("curr now:",current)

    path=[]
    while current is not None:
        path.insert(0,current)
        nextt=shortestPath[current][0]
        current=nextt

    print(path)

u_origin=input("Please enter the origin")
u_destiny=input("Please enter the destination")

findingSP(mapp,u_origin,u_destiny)