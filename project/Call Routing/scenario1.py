
def get_routes():
    with open("/Users/duncan/Desktop/MakeSchool/CS3/CS-3-Core-Data-Structures/project/Call Routing/route-costs-106000.txt", mode='r', encoding='utf8') as f:
        lines = []
        for line in f:
            line = line.replace('\n', '')
            line = line.split(',')
            
            lines.append(line)

    return lines
            
def get_cost(p_num):
    costs = get_routes()

    matching = []

    for cost in costs:
        if cost[0] in p_num:
            matching.append(cost)

    max_length = 0
    matching_cost = 0
    for match in matching:
        if len(match[0]) > max_length:
            max_length = len(match[0])
            matching_cost = match[1]

    return float(matching_cost)

print(get_cost('+446592918')