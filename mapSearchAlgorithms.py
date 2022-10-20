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
    
    print("\n\n DATA LOADING")
    print("Start State: " + str(currLocation) + "\nEnd State(s): " + str(destination))
    



def bfs(graph, node1, goal):
  ''' Breadth-First Search'''
  path_list = [[node1]]
  path_index = 0
  # To keep track of previously visited nodes
  previous_nodes = {node1}
  if node1 == goal:
      print(previous_nodes)
      print( path_list[0])
      
  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = graph[last_node]

    # Search goal node
    if goal in next_nodes:
      current_path.append(goal)
      print("\nBREADTH FIRST SEARCH")
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


bfs(mainGraph, "Craiova", "Bucharest")




def UCS(graph, start, goal):
  ''' Uniform Cost Search '''
  pq = PriorityQueue()
  pq.put((0, [start]))
  visitedStates = []
  visitedStates.append(start)

  while not pq.empty():
      node = pq.get()
      current = node[1][len(node[1]) - 1]

      if goal in node[1]:
          print("\n\n UNIFORM COST SEARCH")
          print("States Vvisited: " + str(visitedStates))
          print("Found path of length: " + str(node[1]) + " with a total cost of " + str(node[0]) +"\n\n")
          
          f = True
          for city in node[1]:
            if f:
              f = False
              print(city, end =" ")
            else:
              print('=> ' + city, end = " ")
          return ""
          break

      cost = node[0]
      for neighbor in graph[current]:
          temp = node[1][:]
          temp.append(neighbor)
          if neighbor not in visitedStates:
            visitedStates.append(neighbor)

          pq.put((cost + graph[current][neighbor], temp))


UCS(mainGraph, "Craiova", "Bucharest")