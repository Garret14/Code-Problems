#Graph class that accounts for the weights of each edge.
# Takes an array of vertices and edges as parameters
class UGraph():
  def __init__(self, V = None, E = None):
    #set of nodes(vertices) in Graph
    self._V = set()
    #set of edges in Graph
    self._E = set()
    #dictionary of weights where the key is an edge
    self._Weights = {}
    #dicitonary where the number of neighbors for each vertex is stored
    self._NeighborCount = {}
    #Constructor iterates over parameters and adds vertices and edges to the instance of the object
    if V != None and E != None:
      for v in V:
        self.addVertex(v)
      for u, v, weight in E:
        self.addEdge(u, v, weight)
    elif V != None:
      for v in V:
        self.addVertex(v)

  def vertices(self):
    #method that returns the iterator of the set of verticies
    #This iterator is used by the ZombieDjikstra method to iterate over the vertices
    return iter(self._V)

  def addVertex(self, v):
    #adds vertex to the set of verticies
    self._V.add(v)
    self._NeighborCount[v] = 0

  def addEdge(self, u, v, weight = None):
    #adds edge to the set of edges and stores the weight in the weight dictionary with the key being the edge
    self._E.add((u, v))
    self._E.add((v,u))
    self._Weights[(u,v)] = weight
    self._Weights[(v,u)] = weight
    self._NeighborCount[v] += 1
    self._NeighborCount[u] += 1

  def neighbors(self, v):
    #returns a generator object of all nodes that are a neighbor of vertex v.
    #This generator is used by the ZombieDjikstra method to iterate over the neighbors of the city removed from the priority queue
    return (w for u, w in self._E if u == v)

  def getWeight(self, edge):
    #returns the weight of the given edge by using the edge as the key in the Weight dictionary
    return self._Weight[edge]

  def minNeighbor(self):
    #returns the vertex with the least amount of neighbors
    return (min(self._NeighborCount, key = lambda x: self._NeighborCount[x]))

def ZombieDijkstra(G):
  #The implementation of the Djikstra Algorithm. Initial node is the node with the least amount of neighbors in the graph.
  #The path dictionary returns the shortest path from the initial node to all other nodes in the graph, with each key-value pair being node-parent.
  #The Keys Dictionary initializes all nodes with a key of infinity in the priority queue. The initial node's key is set to 0.
  #The minimum value of the Priority Queue (represented as a list of tuples with each tuple being a vertex and its Key from the Keys dictionary) is removed from the PriorityQueue and its neighbors are iterated over.
  #If the key of initial node plus the weight of the edge between the node and the current neighbor is less than the current key of the neighbor, then:
      #the current tuple contaning the neibor is stored in the oldkey variable.
      #The PriorityQueue removes the old tuple (oldkey).
      #The Key for the neighbor node in the Keys dictionary is updated to the Key of the current node plus the weight of the edge between it and the neighbor node.
      #The neighbor city is added to the path dictionary with its entry being the current node, representing the current shortest path from the current city to the neighbor city.
      #A new tuple (newkey) is initalized with the neigbhor city and its new key and is added to the Priority Queue.
      #By doing this, the algorithm will keep updating the keys and the shortest paths between two cities until the priority queue is empty.
  #This keeps track of the current shortest path overall, as each entry in path for each city will be the neighbor with the shortest total weight to that city.
  #Once the Priority Queue is empty, then the path dictionary is iterated over:
    #For each city in the path dictionary, if its parent city is not None, then the weight of the edge between the city and its neighbor is added to the total time.
  #Afterwards, the path dictionary is returned along wiht the totaltime.
  totaltime = 0
  initial = G.minNeighbor()
  path = {initial:None}
  Keys = {u:float("inf") for u in G.vertices()}
  Keys[initial] = 0
  PriorityQueue = [(u, Keys[u]) for u in G.vertices()]
  while PriorityQueue:
    city = min(PriorityQueue, key = lambda x: x[1])
    PriorityQueue.remove(city)
    for ncity in G.neighbors(city[0]):
      if Keys[city[0]] + G._Weights[(city[0],ncity)] < Keys[ncity]:
        oldkey = (ncity, Keys[ncity])
        PriorityQueue.remove(oldkey)
        Keys[ncity] = Keys[city[0]] + G._Weights[city[0],ncity]
        path[ncity] = city[0]
        newkey = (ncity, Keys[ncity])
        PriorityQueue.append(newkey)
  for x in path:
    parentcity = path[x]
    if path[x] is not None:
      totaltime += G._Weights[(parentcity,x)]

  return path, str(totaltime) + " " + "hours to infect all cities"

#TestCase 1: General
#Cities = {"Los_Angeles","San_Diego","San_Fransisco", 'Sacremento', "Ontario"}
#Edges = {("San_Diego", "Los_Angeles", 120), ("Los_Angeles", "Sacremento", 384)
#,("San_Fransisco", "Sacremento", 86), ("San_Diego", "Ontario", 113)}
#Graph = UGraph(Cities,Edges)
#a = ZombieDijkstra(Graph)
#print(a)

#TestCase 2: General, but with an extra path between LA and San Fransisco that shortens the time of infection
#Cities2 = {"Los_Angeles","San_Diego","San_Fransisco", 'Sacremento', "Ontario"}
#Edges2 = {("San_Diego", "Los_Angeles", 120), ("Los_Angeles", "Sacremento", 384)
#,("San_Fransisco", "Sacremento", 86), ("San_Diego", "Ontario", 113), ("San_Fransisco", "Los_Angeles", 100)}
#Graph2 = UGraph(Cities2,Edges2)
#b = ZombieDijkstra(Graph2)
#print(b)

#TestCase3: General again, but the new path between LA and San Fransisco is longer than LA to Sacremento in order to show that the algorithm incorporates the shortest routes.
#Cities3 = {"Los_Angeles","San_Diego","San_Fransisco", 'Sacremento', "Ontario"}
#Edges3 = {("San_Diego", "Los_Angeles", 120), ("Los_Angeles", "Sacremento", 384)#
#,("San_Fransisco", "Sacremento", 86), ("San_Diego", "Ontario", 113), ("San_Fransisco", "Los_Angeles", 500)}
#Graph3 = UGraph(Cities3,Edges3)
#c = ZombieDijkstra(Graph3)
#print(c)

#TestCase4: Cities have at least 2 outgoing edges
#Cities4 = {"Indianapolis", "Gary", "Louisville", "Nashville", "Birmingham"}
#Edges4 = {("Nashville", "Indianapolis", 40),("Indianapolis", "Louisville", 10)
#,("Nashville", "Gary", 114),("Nashville", "Birmingham", 200), ("Birmingham", "Gary", 30),("Louisville", "Nashville", 100)}
#Graph4 = UGraph(Cities4,Edges4)
#d = ZombieDijkstra(Graph4)
#print(d)

#TestCase5: Two Edges have same weight
#Cities4 = {"Indianapolis", "Gary", "Louisville", "Nashville", "Birmingham"}
#Edges4 = {("Nashville", "Indianapolis", 40),("Indianapolis", "Louisville", 10)
#,("Nashville", "Gary", 114),("Nashville", "Birmingham", 30), ("Birmingham", "Gary", 30),("Louisville", "Nashville", 100)}
#Graph4 = UGraph(Cities4,Edges4)
#d = ZombieDijkstra(Graph4)
#print(d)




