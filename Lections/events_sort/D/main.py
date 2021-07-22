def is_parking_full(cars, n):
    events = []
    for car in cars:
        time_in, time_out, place_from, place_to = car
        events.append((time_in, 1, place_to - place_from + 1))
        events.append((time_out, -1, place_to - place_from + 1))
    events.sort()
    occupied = 0
    for event in events:
        if event[1] == -1:
            occupied -= event[2]
        elif event[1] == 1:
            occupied += event[2]
        if occupied == n:
            return True
    return False


n = 10  # 10 places in parking
cars = [(4, 8, 1, 2),
        (5, 7, 3, 3),
        (4, 6, 4, 10),
        (15, 20, 3, 4)]
print(is_parking_full(cars, n))
