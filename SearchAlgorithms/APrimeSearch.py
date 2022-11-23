from queue import PriorityQueue
from collections import deque

mainGraph = {}
heuristicGraph = {}
#holds global dictionaries for the heuristics chart and neighbouring cities and distance chart

start = []
goal = []
#Stored these as strings for reusability and couldn't store strings for some reason

def dataLoader(filename, mainGraph, start, goal):
    #Same dataloader from Assignment 2
    with open(filename,'r') as wholeText:
        lines = wholeText.readlines()

        start.append(lines[1])
        goal.append(lines[2])


        transitions = 0

        for lineNum in range(3,len(lines)):

            cityNode = lines[lineNum].split(':')
            city = cityNode[0] 
            #SenMapated the cities

            connectedCities = cityNode[1].split(' ')
            #Creates an array of the connected cities

            del connectedCities[0]
            #Deletes first empty item in each connected cities array

            transitions += len(connectedCities)
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

        print("\n\nDATA LOADING")
        print("Start State: " + str(start[0]) + "End State(s): " + str(goal[0]), end ="")
        print("State Space Size: " + str(len(mainGraph)))
        print("Total Transitions: " + str(transitions))



def heuristicLoader(fileName, heuristicGraph):
    #loads the heuristic information into a readable dictionary
    with open(fileName, 'r') as wholeText:
        lines = wholeText.readlines()

        for lineNum in range(len(lines)):

            cityNode = lines[lineNum].split(':')
            cityNode[1] = int(cityNode[1][1:].replace('\n', ''))

            heuristicGraph |= {cityNode[0]: cityNode[1]}
            #stores it in the global heuristicGraph dictionary


class AStarSearchClass:
    def __init__(self, mainGraph, heuristicGraph):
        self.mainGraph = mainGraph
        self.heuristicGraph = heuristicGraph

    def get_neighbors(self, v):
        return self.mainGraph[v]

    def heur(self, n):
        #Function used to return the huristic value for nodes
        return self.heuristicGraph[n]

    def aStarSearch(self, start, goal):

        openArr = set([start])
        closedArr = set([])
        testCost =[]

        # dMap holds distances from the start
        dMap = {}
        dMap[start] = 0

        # nMap holds the nieghbouring nodes
        nMap = {}
        nMap[start] = start

        while len(openArr) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in openArr:
                if n == None or dMap[v] + self.heur(v) < dMap[n] + self.heur(n):
                    n = v
                    testCost.append(dMap[v])
                    

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the goal
            # then we start again from start
            if n == goal:
                finalPath = []
 
                while nMap[n] != n:
                    finalPath.append(n)
                    n = nMap[n]
 
                finalPath.append(start)
                finalPath.reverse()

                print("\nA* SEARCH")
                print('States Visited:', dMap.keys())
                print("Total cost:", dMap[goal] )
                f = True
                for city in finalPath:
                    if f:
                        f = False
                        print(city, end =" ")
                    else:
                        print('=> ' + city, end = " ")



                return finalPath
 
            # for all the neighbors of the current node do
            for m, weight in self.get_neighbors(n).items():
              # if the current node is not in  openArr and closedArr we add it to openArr and note n as it's nMap
                if m not in openArr and m not in closedArr:
                    openArr.add(m)
                    nMap[m] = n
                    dMap[m] = dMap[n] + weight
                    # testCost.append(weight)

                # otherwise, check if it's quicker to first visit neighbour, then m the current node
                else:
                    if dMap[m] > dMap[n] + weight:
                        dMap[m] = dMap[n] + weight
                        nMap[m] = n

                        if m in closedArr:
                            closedArr.remove(m)
                            openArr.add(m)

            # remove neighbour node from the openArr and add it to closedArr since all neighbours were checked
            openArr.remove(n)
            closedArr.add(n)
 
        print('No path exists, sorry')
        return None


def main():
    #I tried to make the code more reusable so I implemented a main function
    #which will work by just hardcoding the file names
    dataLoader("input.txt", mainGraph, start, goal)
    heuristicLoader("input_heuristic(1).txt", heuristicGraph)


    star = AStarSearchClass(mainGraph, heuristicGraph)
    star.aStarSearch(str(start[0][:-1]), str(goal[0][:-1]))


if __name__ == "__main__":
    main()