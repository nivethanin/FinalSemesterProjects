import collections


with open('input.txt','r') as wholeText:
    lines = wholeText.readlines()
    
    currLocation = lines[1]
    destination = lines[2]

    mainGraph = {}

    for lineNum in range(3,len(lines)):

        cityNode = lines[lineNum].split(':')
        city = cityNode[0] 
        #Separated the cities
        
        connectedCities = cityNode[1].split(' ')
        #Creates an array of the connected cities

        del connectedCities[0]
        #Deletes first empty item in each connected cities array

        
        miniDic ={}

        for conCity in range(len(connectedCities)):
            
            conCitiesWithDistance = connectedCities[conCity].split(',')

            conCityDictionary ={conCitiesWithDistance[0]:int(conCitiesWithDistance[1])}
            
            miniDic |= conCityDictionary
            

        conCitiesDictionary = {city:miniDic}
        
        mainGraph|=conCitiesDictionary

    print(mainGraph)


''' 
I could create an recursive function that keeps track of 
the distance of the path it is currently on. I will have
store:
- path
- weight of path
That way I can have a check in the recursive function to
see which recursive call has the lowest weight and
shortest path
'''

visited = [] # List to keep track of visited nodes.
queue = []   # Initialize a queue

# def breadthFirstSearch(visited, graph, node, goal):
#   # if node in visited:
#   #   return

#   if node == goal and node in visited:
#     print ("this is visited: " , visited)
#     print ("this is queue: ", queue)
#     return

#   else:
#     if node not in visited:
#       visited.append(node)
      
#       queue.append(node)

#     while queue:
#       s = queue.pop(0) 
#     # print (s, end = " ") 

#       for neighbour, key in graph[s].items():
#         if neighbour not in visited:
#           visited.append(neighbour)
#           queue.append(neighbour)

#         breadthFirstSearch(visited, mainGraph, s, goal)

# breadthFirstSearch(visited, mainGraph, "Craiova", "Bucharest")

'''  another try   '''
# breadthFirstSearch(visited, mainGraph, 'Craiova') 

# def bdfs (graph, visited, currNode, goal):
#   if currNode not in visited:
#     visited.append(currNode)
#     print(visited)

#   for node,value in graph[currNode].items():
#     if node in visited:
#       return
      
#     queue.append(node)
#     # print("made it to loop")
#     if currNode == goal:
#       print(queue)
#       return
    
#     bdfs(graph, visited, node, goal)

#   print("finished a recursion call")
  
  

 
# bdfs(mainGraph, visited, 'Craiova', 'Bucharest')


# for key, value in mainGraph['Arad'].items():
#   print(key, value)

''' Another try'''

def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]

        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path

        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []



print(shortest_path(mainGraph, "Craiova", "Bucharest"))