import itertools
import numpy as np

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    def get_dir_vec(self):
        return (self.endPoint[0] - self.startPoint[0], self.endPoint[1] - self.startPoint[1])
    
    def calc_intersection(self, l):
        or_1 = self.startPoint
        dir_1 = self.get_dir_vec()
        or_2 = l.startPoint
        dir_2 = l.get_dir_vec()
        t_2 = (or_2[1] * dir_1[0] - or_1[1] * dir_1[0] - or_2[0] * dir_1[1] + or_1[0] * dir_1[1]) / (dir_2[0] * dir_1[1] - dir_2[1] * dir_1[1])
        return (or_1[0] + t_2 * dir_1[0], or_1[1] + t_2 * dir_1[1])
    
    def __str__(self):
        return str(self.startPoint) + "->" + str(self.endPoint)



def calc_manhattan_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_range_list(point, distance):
    return [
        (point[0] - (distance - (abs(point[1] - y))), point[0] + (distance - (abs(point[1] - y))), y) 
        for y 
        in range(point[1] - distance, point[1] + distance + 1)
    ]

def find_furthest_points(point, distance, min_x, min_y, max_x, max_y):
    return [(point[0], point[1] - distance), (point[0] - distance, point[1]), (point[0], point[1] + distance), (point[0] + distance, point[1])]


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d15\input.txt') as f:
    lines = f.readlines()
    task = "b"

    # parse input:
    line_splits = [line.split() for line in lines]
    data = [((int(split[2][2:-1]), int(split[3][2:-1])), (int(split[8][2:-1]), int(split[9][2:]))) for split in line_splits]

    print("Parsed input.")

    # task a:
    if task == "a":
        # calc range list for each sensor:
        distances = [calc_manhattan_dist(point1=d[0], point2=d[1]) for d in data]
        range_lists = [find_range_list(point=data[i][0], distance=distances[i]) for i in range(len(data))]

        print("Calculated ranges.")

        # filter relevant data:
        row_number = 2000000
        relevant_ranges = list(filter(lambda r: r[2] == row_number, list(itertools.chain(*range_lists))))
        min_x = min([r[0] for r in relevant_ranges])
        max_x = max([r[1] for r in relevant_ranges])
        relevant_beacons = [(pos[1][0], pos[1][1]) for pos in list(filter(lambda d: d[1][1] == row_number, data))]

        print("Filtered data.")

        # calc number of impossible beacon positions:
        relevant_row = np.zeros((max_x - min_x + 1), int)
        for range in relevant_ranges:
            relevant_row[range[0]-min_x : range[1]-min_x+1] = 1
        for beacon_pos in relevant_beacons:
            relevant_row[beacon_pos[0]-min_x] = 0
    
        print("Calulated result.")

        # print result:
        print("Result: " + str(sum(relevant_row)))
    

    # task b:
    if task == "b":
        min_xy = 0
        max_xy = 20

        # find furthest points of all sensor points:
        signal_pos = [(d[0][0], d[0][1]) for d in data]
        beacon_pos = [(d[1][0], d[1][1]) for d in data]
        distances = [calc_manhattan_dist(point1=d[0], point2=d[1]) for d in data]
        furthest_points = [find_furthest_points(point=data[i][0], distance=distances[i], min_x=min_xy, min_y=min_xy, max_x=max_xy, max_y=max_xy) for i in range(len(data))]
        
        print("Calculated max points.")

        # find intersection with y = 0 for each diagonal in squares:
        lower_right_sides = [(point[3][0] + point[3][1], 0) for point in furthest_points]
        upper_right_sides = [(point[0][0] - point[0][1], 0) for point in furthest_points]
        upper_left_sides = [(point[0][0] + point[0][1], 0) for point in furthest_points]
        lower_left_sides = [(point[1][0] - point[1][1], 0) for point in furthest_points]

        # find all pairs of upper left and lower right points that have difference of 2:
        main_diagonal_pairs = []
        for lrs in lower_right_sides:
            for uls in upper_left_sides:
                if uls[0] - lrs[0] == 2:
                    main_diagonal_pairs.append((lrs, uls))
        
        # find all pairs of upper right and lower left points that have difference of 2:
        secondary_diagonal_pairs = []
        for urs in upper_right_sides:
            for lls in lower_left_sides:
                if lls[0] - urs[0] == 2:
                    secondary_diagonal_pairs.append((urs, lls))

        print(main_diagonal_pairs)
        print(secondary_diagonal_pairs)

        main_diagonal_x = main_diagonal_pairs[0][0][0] + 1
        secondary_diagonal_x = secondary_diagonal_pairs[0][0][0] + 1

        result = ((main_diagonal_x + secondary_diagonal_x) // 2, (main_diagonal_x - secondary_diagonal_x) // 2)

        print((main_diagonal_x, secondary_diagonal_x))
        print(4000000 * result[0] + result[1])
        
