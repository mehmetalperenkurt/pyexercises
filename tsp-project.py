import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

fig= plt.figure(figsize=(8,8))
axes= fig.add_axes([0.1,0.1,0.8,0.8])

nodesPoint=[]
pathPoint=[]
cordinateXList=[]
cordinateYList=[]

class dataSet():
    def __init__(self):
        self.cityDict={}
        self.cities={}
        #self.data['vehicle'] = 1
        #self.data['depot'] = 0

    def readCities(self):
        f = open('cities.txt', 'r').read()
        line = f.split('\n')

        for x in line:
            partition = x.replace(':', ' ').replace(',', ' ').split()
            partOne=partition[0]
            partTwo=((float(partition[1]))*0.1,(float(partition[2]))*0.1)

            self.cityDict[partOne]=partTwo
            self.cities[partition[0]]=city(partition[0], (partition[1]),(partition[2]))

        return self.cityDict

    def printDict(self):
        print(self.cityDict)
        print(self.cities)

class city():
    def __init__(self,name,lat,lon):
        self.name=name
        self.lat=float(lat)
        self.lon=float(lon)
        self.location=(float(lat),float(lon))

d = dataSet()
d.readCities()


rows,cols=len(d.cities.values()),len(d.cities.values())
distMatrix=[[0 for i in range(cols)] for j in range(rows)]

for x in d.cities.values():
    print(x.name,' - ','Location ',x.location)
    nodesPoint.append(list(x.location))



for id,x in enumerate(d.cities.values()):
    cordinateXList.append(x.lat)
    cordinateYList.append(x.lon)

for idx,x in enumerate(d.cities.values()):
    for idy,y in enumerate(d.cities.values()):
        dist = round(float(distance.euclidean(x.location, y.location)),3)
        distMatrix[idx][idy]=dist
for x in distMatrix:
    print(x)
print(nodesPoint,"THIS NODES LAT,LON POINTS")

def drawpath(sortedList):
    print(sortedList," ROUTE LIST\n")
    #pathPoint = [x for _,x in sorted(zip(sortedList,nodesPoint))]
    for x in sortedList:
        pathPoint.append(nodesPoint[x])
    pathPoint.append(pathPoint[0])
    print(pathPoint, "SORTED PATH POINTLIST")
    data = np.array(pathPoint)
    # plt.title('TSP Graph')
    plt.plot(data[:, 0], data[:, 1])
    plt.show()



for id,x in enumerate(d.cities.values()):
    p = [x.lat,x.lon,x.name]
    axes.plot(p[0], p[1], '.')
    plt.text(p[0]+.1,p[1],p[2], horizontalalignment='left', verticalalignment='center')

def print_solution(manager, routing, solution):
    sortedList=[]
    print('Toplam mesafe: {} birim'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Başlangıç noktası 0 araç için:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        sortedList.append(int(manager.IndexToNode(index)))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plt.title(plan_output)
    drawpath(sortedList)


def main():

    manager = pywrapcp.RoutingIndexManager(len(distMatrix), 1, 0)

    routing = pywrapcp.RoutingModel(manager)


    def distance_callback(from_index, to_index):

        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distMatrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)


    solution = routing.SolveWithParameters(search_parameters)


    if solution:
        print_solution(manager, routing, solution)


if __name__ == '__main__':
    main()
