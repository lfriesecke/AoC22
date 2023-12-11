import numpy as np

def calc_distances(valve_name, valves):

    open_valves = set([valve_name])
    traversed_valves = set()
    distances = {valve_name:0}
    cur_distance = 0

    while open_valves:
        # find all reachable valves:
        next_valves = set()
        for valve in open_valves:
            for reachable_valve in valves[valve][2]:
                if reachable_valve not in traversed_valves and reachable_valve not in open_valves and reachable_valve not in next_valves:
                    next_valves.add(reachable_valve)

        # prepare next iteration:
        traversed_valves = traversed_valves.union(open_valves)
        distances.update({valve:cur_distance for valve in open_valves})
        open_valves = next_valves
        cur_distance += 1
    
    return distances


def calc_max_pressure_a(valves, distances, cur_valve_name, remaining_valves, minutes_remaining):

    # exit condition: no time remaining
    if minutes_remaining < 0:
        return 0
    
    # calc pressure of all remaining routes:
    pressure_vals = [minutes_remaining * valves[cur_valve_name][1] + calc_max_pressure_a(valves=valves, distances=distances, cur_valve_name=valve_name, remaining_valves=remaining_valves - set([valve_name]), minutes_remaining=minutes_remaining - distances[cur_valve_name][valve_name] - 1) for valve_name in remaining_valves]
    if len(pressure_vals) == 0:
        return minutes_remaining * valves[cur_valve_name][1]
    return max(pressure_vals)


def calc_max_pressure_b(valves, distances, origin_human, origin_elephant, target_human, target_elephant, rem_mins_human, rem_mins_elephant, rem_valves, rem_minutes, pressure):

    # case 1: human has no target:
    if target_human is None and origin_human is not None:
        pressure_vals = [
            calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=origin_human,
                origin_elephant=origin_elephant,
                target_human=valve_name,
                target_elephant=target_elephant,
                rem_mins_human=distances[origin_human][valve_name] + 1,
                rem_mins_elephant=rem_mins_elephant,
                rem_valves=rem_valves - set([valve_name]),
                rem_minutes=rem_minutes,
                pressure=pressure
            )
            for valve_name in rem_valves
        ]
        if len(pressure_vals) == 0:
            return calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=None,
                origin_elephant=origin_elephant,
                target_human=None,
                target_elephant=target_elephant,
                rem_mins_human=-1,
                rem_mins_elephant=rem_mins_elephant,
                rem_valves=rem_valves,
                rem_minutes=rem_minutes,
                pressure=pressure
            )
        return max(pressure_vals)

    # case 2: elephant has no target:
    if target_elephant is None and origin_elephant is not None:
        pressure_vals = [
            calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=origin_human,
                origin_elephant=origin_elephant,
                target_human=target_human,
                target_elephant=valve_name,
                rem_mins_human=rem_mins_human,
                rem_mins_elephant=distances[origin_elephant][valve_name] + 1,
                rem_valves=rem_valves - set([valve_name]),
                rem_minutes=rem_minutes,
                pressure=pressure
            )
            for valve_name in rem_valves
        ]
        if len(pressure_vals) == 0:
            return calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=origin_human,
                origin_elephant=None,
                target_human=target_human,
                target_elephant=None,
                rem_mins_human=rem_mins_human,
                rem_mins_elephant=-1,
                rem_valves=rem_valves,
                rem_minutes=rem_minutes,
                pressure=pressure
            )
        return max(pressure_vals)

    # case 3: both entities have targets:
    else:
        # case 3.1: human reached target:
        if rem_mins_human == 0:
            return calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=target_human,
                origin_elephant=origin_elephant,
                target_human=None,
                target_elephant=target_elephant,
                rem_mins_human=rem_mins_human,
                rem_mins_elephant=rem_mins_elephant,
                rem_valves=rem_valves,
                rem_minutes=rem_minutes,
                pressure=pressure + valves[target_human][1]
            )

        # case 3.2: elephant reached target:
        if rem_mins_elephant == 0:
            return calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=origin_human,
                origin_elephant=target_elephant,
                target_human=target_human,
                target_elephant=None,
                rem_mins_human=rem_mins_human,
                rem_mins_elephant=rem_mins_elephant,
                rem_valves=rem_valves,
                rem_minutes=rem_minutes,
                pressure=pressure + valves[target_elephant][1]
            )

        # case 3.3: both entities are on their way and there are minutes left:
        if rem_minutes > 0:
            return calc_max_pressure_b(
                valves=valves,
                distances=distances,
                origin_human=origin_human,
                origin_elephant=origin_elephant,
                target_human=target_human,
                target_elephant=target_elephant,
                rem_mins_human=rem_mins_human - 1,
                rem_mins_elephant=rem_mins_elephant - 1,
                rem_valves=rem_valves,
                rem_minutes=rem_minutes - 1,
                pressure=pressure
            ) + pressure

        # case 3.4 both entities are on their way and there are no minutes left:
        else:
            return 0


with open(r'C:\Users\lfrie\OneDrive\Projekte\AoC22\d16\input.txt') as f:
    lines = f.readlines()
    task = "a"

    # parse input:
    line_splits = [line.split() for line in lines]
    valves = {split[1]:(split[1], int(split[4][5:-1]), set(split[9:])) for split in line_splits}
    for k in valves.keys():
        valve = valves[k]
        valves[k] = (valve[0], valve[1], set([item.replace(",", "") for item in valve[2]]))

    print("Parsed input.")

    # filter relevant valves and calc distances:
    valve_names = set(valves.keys())
    relevant_valves_names = [name[0] for name in list(filter(lambda v: v[1][1] > 0, valves.items()))]
    distances = {}
    for valve_name in relevant_valves_names + ["AA"]:
        dists = calc_distances(valve_name=valve_name, valves=valves)
        for v in valve_names:
            if v not in relevant_valves_names:
                dists.pop(v)
        distances[valve_name] = dists

    print("Distances calculated.")

    # maximize presure:
    print(calc_max_pressure_a(valves=valves, distances=distances, cur_valve_name="AA", remaining_valves=set(relevant_valves_names), minutes_remaining=30))
    print(calc_max_pressure_b(
        valves=valves,
        distances=distances,
        origin_human="AA",
        origin_elephant="AA",
        target_human=None,
        target_elephant=None,
        rem_mins_human=1,
        rem_mins_elephant=1,
        rem_valves=set(relevant_valves_names),
        rem_minutes=26,
        pressure=0
    ))
