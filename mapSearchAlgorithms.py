import collections
from queue import PriorityQueue
import queue


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

# visited = [] # List to keep track of visited nodes.
# queue = []   # Initialize a queue

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
      print(previous_nodes)
      return path_list[0]
      
  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = graph[last_node]

    # Search goal node
    if node2 in next_nodes:
      current_path.append(node2)
      print("States visted: ", previous_nodes)

      print("Found path of length: ", path_index)
      f = True
      for city in current_path:
        if f:
          f = False
          print(city, end =" ")
        else:
          print('=> ' + city, end = " ")
      return ""

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



''' UCS '''
# def UCS(graph, src, dest):
#     minDistances, predecessor = dijkstra(graph, src)
    
#     path = []
#     currentNode = dest
#     while currentNode != src:
#         if currentNode not in predecessor:
#             print("Path not reachable")
#             break
#         else:
#             path.insert(0, currentNode)
#             currentNode = predecessor[currentNode]
#     path.insert(0, src)
    
#     if dest in minDistances and minDistances[dest] != float("inf"):
#         print('Shortest distance is ' + str(minDistances[dest]))
#         print('And the path is ' + str(path))
        
# UCS(mainGraph, 'a', 'd')

def UCS(graph, start, goal):
  global cost
  answer = []
  queue = PriorityQueue()


  for i in range(len(goal)):
    answer.append(10**20)

  queue.put(0, start)

  visited = {}

  count = 0

  while (len(queue)> 0):
    queue = sorted(queue)
    p = [-1]

    del queue[-1]

    p[0] *=-1

    if p[1] in goal:
      index = goal.index(p[1])

      if(answer[index] == 10**20):
        count +=1 
      
      if(answer[index]>p[0]):
        answer[index]=p[0]

      del queue[-1]

      queue = sorted(queue)
      if (count == len(goal)):
        return answer

      
    if p[1] not in visited:
      for i in range(len(graph[p[1]])):
        queue.append([(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
    
    visited[p[1]] = 1

  return answer


UCS(mainGraph, "Craiova", "Bucharest")