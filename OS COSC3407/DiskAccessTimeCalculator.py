def FCFS(numCyl, start, queue: list):
    totDis = abs(start - queue[0])
    for i in range(len(queue)-1):
        if queue[i+1]:
            totDis = totDis + abs(queue[i] - queue[i+1])
                    
    print("FCFS:  ", totDis)


""" STF """
def SSTF(reqQueue, head):            
        ll = len(reqQueue)
        diff = [0] * ll
         
        for i in range(ll):
            diff[i] = [0, 0]
         

        finQueue = [0] * (ll + 1)
         
        for i in range(ll):
            finQueue[i] = head
            for i in range(len(diff)):
                diff[i][0] = abs(reqQueue[i] - head)

            index = findMin(diff)
             
            diff[index][1] = True
             
            head = reqQueue[index]
     
        finQueue[len(finQueue) - 1] = head

        totDis =0
        for i in range(len(finQueue)-1):
            if finQueue[i+1]:
                totDis = totDis + abs(finQueue[i] - finQueue[i+1])
        print("SSTF:  ", totDis)
        print("SSTF =, ", finQueue)
                    
def findMin(diff):
    ''' Helper function for SSTF search algorithm '''

    index = -1
    minimum = 999999999
 
    for i in range(len(diff)):
        if (not diff[i][1] and minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index



def cScan(qu, start, numCyl):
    orderedList = sorted(qu)

    totDis = 0
    index = 0
    for i in range(len(orderedList)-1):
        if start< orderedList[i]:
            index = i-1
            break

    totDis += abs(start - numCyl)

    totDis += abs(0 - numCyl)

    totDis += abs(0 - orderedList[index])

    print("CSCAN:  ", totDis)
        

def scan(queue, start, numCyl):

    orderedList = sorted(queue)
    totDis = abs(start - numCyl)
    totDis += abs(numCyl - orderedList[0])
    print("SCAN:  ", totDis)


if __name__ == '__main__':

    # numCyl = int(input("Input the number of cylinders: "))
    # start = int(input("Input the starting position: "))

    # reqQueue = input("Input numbers as part of an array with spaces in between: ")
    # reqQueue = reqQueue.split(' ')
    # reqQueue = [eval(i) for i in reqQueue]

    reqQueue = [98, 183, 37, 122, 14, 224, 65, 267]
    numCyl = 300
    start = 53


    FCFS(numCyl, start, reqQueue)
    SSTF(reqQueue, start)
    cScan(reqQueue, start, numCyl)
    scan(reqQueue, start, numCyl)


    

    