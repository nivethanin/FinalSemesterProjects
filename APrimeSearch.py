from queue import PriorityQueue
from collections import deque

mainGraph = {}
heuristicGraph = {}

def dataLoader(filename, mainGraph):
    with open(filename,'r') as wholeText:
        lines = wholeText.readlines()
        
        currLocation = lines[1]
        destination = lines[2]

        transitions = 0

        for lineNum in range(3,len(lines)):

            cityNode = lines[lineNum].split(':')
            city = cityNode[0] 
            #Separated the cities
            
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
        
        print("\n\n DATA LOADING")
        print("Start State: " + str(currLocation) + "End State(s): " + str(destination), end =" ")
        print("State Space Size: " + str(len(mainGraph)))
        print("Total Transitions: " + str(transitions))


    

def heuristicLoader(fileName, heuristicGraph):
    with open(fileName, 'r') as wholeText:
        lines = wholeText.readlines()

        

        for lineNum in range(len(lines)):

            cityNode = lines[lineNum].split(':')
            cityNode[1] = int(cityNode[1][1:].replace('\n', ''))

            heuristicGraph |= {cityNode[0]: cityNode[1]}
        
        print(heuristicGraph)



 
class Graph:
    def __init__(self, mainGraph, heuristicGraph):
        self.mainGraph = mainGraph
        self.heuristicGraph = heuristicGraph
 
    def get_neighbors(self, v):
        return self.mainGraph[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        return self.heuristicGraph[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            for m, weight in self.get_neighbors(n).items():
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None


def main():
    dataLoader("input.txt", mainGraph)
    heuristicLoader("input_heuristic(1).txt", heuristicGraph)

    g = Graph(mainGraph, heuristicGraph)

    g.a_star_algorithm("Craiova", "Hirsova3")
    

    

if __name__ == "__main__":
    main()

