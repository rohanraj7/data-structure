def add_node(v):
    if v in graph:
        print("Already Exists")
    else:
        graph[v] = []

def add_Edge(v1,v2):
    if v1 not in graph:
        print("Node is not in graph")
        return
    if v2 not in graph:
        print("Node is not in graph")
        return
    else:
        graph[v1].append(v2)
        
def delete_node(v):
    if v not in graph:
        print("Value is not in graph")
        return
    else:
        graph.pop(v)
        for i in graph:
            list = graph[i]
            if v in list:
                list.remove(v)     
                
def delete_Edge(v1,v2):
    if v1 not in graph:
        print(v1,"Node is not present in graph")       
        return
    if v2 not in graph:
        print(v2,"Node is not present in the graph")
        return
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            
def DFS(node,graph):
    visited = set()
    if node not in graph:
        print("Node is not present")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current,"->",end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)
                
def BFS(node,graph):
    visited = set()
    if node not in graph:
        print("Node in not present")
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current,"->",end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)
    
graph = {}

add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
print(graph)

add_Edge('A','B')
add_Edge('B','C')
add_Edge('C','D')
add_Edge('A','E')
print(graph)

# delete_node('E')
print(graph)

# delete_Edge('A','B')
print(graph)

DFS('A',graph)
print()
BFS('A',graph)
