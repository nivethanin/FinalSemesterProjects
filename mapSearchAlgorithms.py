from sqlite3 import connect


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

def breadthFirstSearch(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


breadthFirstSearch(visited, mainGraph, 'Craiova') 