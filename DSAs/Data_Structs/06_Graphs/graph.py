# Make a graph that looks like:
#
#   3-------4-------5 
#   |       |       | 
#   |       |       |
#   1-------2       6
#    \     / 
#     \   /
#      \ /
#       0

class Graph():
    def __init__(self) -> None:
        self.numberOfNodes = 0
        self.adjacentList = {}
    

    def add_vertex(self, node):
        try:
            self.adjacentList[node]
        except KeyError:
            self.adjacentList[node] = []
            self.numberOfNodes += 1

    def add_edge(self, node1=None, node2=None):
        if not node1 or not node2:
            print('Error: One or both nodes are of type None')
            return
        
        try:
            self.adjacentList[node1]
        except KeyError:
            self.add_vertex(node1)
            
        try: 
            self.adjacentList[node2]
        except KeyError:
            self.add_vertex(node2)
        
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def show_connections(self):
        for node in self.adjacentList:
            print(f"{node} --> {', '.join(map(str, self.adjacentList[node]))}")

def main():
    myGraph = Graph()
    myGraph.add_vertex('0')
    myGraph.add_vertex('1')
    myGraph.add_vertex('2')
    myGraph.add_vertex('3')
    myGraph.add_vertex('4')
    myGraph.add_edge('3', '1')
    myGraph.add_edge('3', '4')
    myGraph.add_edge('4', '2')
    myGraph.add_edge('4', '5')
    myGraph.add_edge('1', '2')
    myGraph.add_edge('1', '0')
    myGraph.add_edge('0', '2')
    myGraph.add_edge('6', '5')
    print(f'Total Nodes: {myGraph.numberOfNodes}')
    myGraph.show_connections()

if __name__ == '__main__':
    main()