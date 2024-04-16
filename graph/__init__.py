class BidirectionalGraph:
  '''Bidirectional Graph'''
  def __init__(self):
    self.NumberOfNodes = 0
    self.adjacentList = {}

  def addVertex(self,nodeName):
    if nodeName not in self.adjacentList.keys():
      self.adjacentList[nodeName] = []
      self.NumberOfNodes += 1
    else:
      raise ValueError("Node already exists")

  def addEdge(self,node1,node2):
    if node1 not in self.adjacentList.keys():
        raise ValueError("Node1 does not exist")
    if node2 not in self.adjacentList.keys():
        raise ValueError("Node2 does not exist")
    if node2 in self.adjacentList[node1] or node2 in self.adjacentList[node2]:
        raise ValueError("Edge already exists. Bidirectional graphs do not allow duplicate edges.")
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)

  def showConnections(self):
    for x in self.adjacentList.keys():
      print("Node:" + x + "Connections:" + " ".join(self.adjacentList[x]))

class DirectedGraph:
  '''Directed Graph'''
  def __init__(self):
    self.NumberOfNodes = 0
    self.adjacentList = {}

  def addVertex(self,nodeName):
    if nodeName not in self.adjacentList.keys():
      self.adjacentList[nodeName] = []
      self.NumberOfNodes += 1
    else:
      raise ValueError("Node already exists")

  def addEdge(self,node1,node2):
    if node1 not in self.adjacentList.keys():
        raise ValueError("Node1 does not exist")
    if node2 not in self.adjacentList.keys():
        raise ValueError("Node2 does not exist")
    self.adjacentList[node1].append(node2)

  def showConnections(self):
    for x in self.adjacentList.keys():
      print("Node:" + x + "Connections:" + " ".join(self.adjacentList[x]))


