import csv
import os

PATH = os.path.join(os.getcwd(), 'routes.csv') # Windows delimater = '\'; Linux delimater = '/'

def main():
    route_list = createRouteList(PATH)
    
    # for i in route_list:
    #     print(i)
    
    route_list.sort(key=lambda route: route.route_length, reverse=False)
    # for i in route_list:
    #     print(i.route_length)

    stationX = 'Start_Station1'

    # lessAverageLength(18,route_list)

    # route_from_station_X = [route for route in route_list if route.start_station == stationX]
    # for i in route_from_station_X:
    #     print(i.route_name)
    
    for i in maxStops(route_list):
        print(i.route_name)


def createRouteList(file_path):
    lst = []
    with open(file_path, 'r') as f: # 0 - STDIN; 1 - STDOUT; 2 - STDERR
        reader = csv.DictReader(f)
        for row in reader:
            route = Transport_route(row)
            lst.append(route)
    
    return lst


def lessAverageLength(X,route_list):
    for route in route_list:
        if route.route_length / route.count_stops < X:
            print(route.route_name)


def maxStops(route_list):
    stops = [route.count_stops for route in route_list]
    maxCount = max(stops)

    return [route for route in route_list if route.count_stops == maxCount]
    

class Transport_route:

    def __init__(self, routes):

        self.route_name = routes['Route_name']
        self.start_station = routes['Start_station']
        self.end_station = routes['End_station']
        self.count_stops = int(routes['Count_stops'])
        self.route_length = int(routes['Route_length'])


if __name__ == "__main__":
    main()