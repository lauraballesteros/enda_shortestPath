#create the map
#need to update the edges with the .txt file later

edges=[
    ("n0","n3",10),
    ("n0","n4",7),
    ("n0","n5",9),
    ("n1","n4",11),
    ("n1","n5",6),
    ("n2","n3",8),

]

class Graph():
    def __init__(self):
        self.edges={}
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
    shortestPath={origin=(None,0)}
    current=origin
    visited= set()

    while current!= destiny:
        visited.add(current)
        neighbors=mapp.edges[current]
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
            print("ups, we could'nt find you the right route,sorry!")
        
        current=min(nextt_destination,key=lambda k:nextt_destination[k][1])

    path=[]
    while current is not None:
        path.insert(current,-1)
        nextt=shortestPath[current][0]
        current=nextt
        print(current)

    print(path)

u_origin=input("Please enter the origin")
u_destiny=input("Please enter the destination")

findingSP(mapp,u_origin,u_destiny)