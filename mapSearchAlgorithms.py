import collections
from queue import PriorityQueue
import queue


with open('input.txt','r') as wholeText:
    lines = wholeText.readlines()
    
    currLocation = lines[1]
    destination = lines[2]

    mainGraph = {}
    transitions = 0

    for lineNum in range(3,len(lines)):

        cityNode = lines[lineNum].split(':')
        city = cityNode[0] 
        #Separated the cities
        
        connectedCities = cityNode[1].split(' ')
        transitions += len(connectedCities)
        #Creates an array of the connected cities

        del connectedCities[0]
        #Deletes first empty item in each connected cities array

        miniDic ={}                                                                                                                                                                                                            

        for conCity in range(len(connectedCities)):
            
            conCitiesWithDistance = connectedCities[conCity].split(',')

            conCityDictionary ={conCitiesWithDistance[0]:int(conCitiesWithDistance[1])}
            #Splits connected cities into the city and the distance

            miniDic |= conCityDictionary
            #Stores just connected cities in a dictionary

            
        conCitiesDictionary = {city:miniDic}
        #Connects the cities to the dictionary of connected cities
        
        mainGraph|=conCitiesDictionary
        #Connects all the dictionaries into one
    
    print("\n\n DATA LOADING")
    print("Start State: " + str(currLocation) + "End State(s): " + str(destination), end =" ")
    print("State Space Size: " + str(len(mainGraph)))
    print("Total Transitions: " + str(transitions))
    



def bfs(graph, node1, goal):
  ''' Breadth-First Search'''
  path_list = [[node1]]
  pathCount = 0

  visitedNodes = {node1}  
  # To keep track of visited nodes

  if node1 == goal:
      print(visitedNodes)
      print( path_list[0])
      
  while pathCount < len(path_list):
    currPath = path_list[pathCount]
    last_node = currPath[-1]
    next_nodes = graph[last_node]

    # Search goal node
    if goal in next_nodes:
      currPath.append(goal)
      print("\nBREADTH FIRST SEARCH")
      print("States visted: ", visitedNodes)
      print("Found path of length: ", pathCount)
      f = True
      for city in currPath:
        if f:
          f = False
          print(city, end =" ")
        else:
          print('=> ' + city, end = " ")
      return ""

    # Add new paths
    for next_node in next_nodes:
        if not next_node in visitedNodes:
            new_path = currPath[:]
            new_path.append(next_node)
            path_list.append(new_path)
            
            visitedNodes.add(next_node)
            # Keep track of visited nodes
    # Continue to next path in list
    pathCount += 1
  
  return ""
  # Returns empty string if no solution is found

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
          #Prints the cities with arrows
          return ""
          #Returns empty if goal isn't found

      cost = node[0]
      for nextNode in graph[current]:
          temp = node[1][:]
          temp.append(nextNode)
          if nextNode not in visitedStates:
            visitedStates.append(nextNode)

          pq.put((cost + graph[current][nextNode], temp))
          #Adds cost as the priority metric and the node in the queue


UCS(mainGraph, "Craiova", "Bucharest")