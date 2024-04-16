from graph import DirectedGraph as Graph

def dfs(graph: Graph,start):
    visited = []
    stack = [start]
    # print("Visited:",visited)
    # print("Stack:",stack)
    while stack:
        # print("Visited:",visited)
        # print("Stack:",stack)
        node = stack.pop()
        # print("Node",node)
        if node not in visited:
            visited.append(node)
            stack += graph.adjacentList[node]
    return visited

# Example 1:

my_graph = Graph()
my_graph.addVertex("0")
my_graph.addVertex("1")
my_graph.addVertex("2")
my_graph.addVertex("3")

my_graph.addEdge("0","1")
my_graph.addEdge("0","2")
my_graph.addEdge("2","0")
my_graph.addEdge("1","2")
my_graph.addEdge("2","3")
my_graph.addEdge("3","3")


print(dfs(my_graph,"2")) # ['2', '3', '0', '1']

# Example 2:

my_graph = Graph()
my_graph.addVertex("A")
my_graph.addVertex("B")
my_graph.addVertex("C")
my_graph.addVertex("D")
my_graph.addVertex("E")
my_graph.addVertex("F")


my_graph.addEdge("A","B")
my_graph.addEdge("B","A")
my_graph.addEdge("B","C")
my_graph.addEdge("B","D")
my_graph.addEdge("D","C")
my_graph.addEdge("C","E")
my_graph.addEdge("E","F")
my_graph.addEdge("F","D")



print(dfs(my_graph,"B")) # ['B', 'D', 'C', 'E', 'F', 'A']