s = open('26/txts/26-119.txt')
cars, n_light_cars, n_autobus = [int(i) for i in s.readline().split()]


a = []
for i in range(cars):
    start, time, car_type = [i for i in s.readline().split()]
    end = int(start) + int(time)
    a.append([int(start), end, car_type])

a.sort()
    
places_light = [0] * n_light_cars
places_autobus = [0] * n_autobus


is_parked = 0
counter_not_parked = 0
counter_bus = 0

for i in range(len(a)):
    is_parked = 0
    start, end, car_type = a[i]
    
    if car_type == 'B':
        for j in range(n_autobus):
            if places_autobus[j] <= start:
                places_autobus[j] = end
                counter_bus += 1
                is_parked = 1
                break
            
    if car_type == 'A':
        for j in range(n_light_cars):
            if places_light[j] <= start:
                places_light[j] = end
                is_parked = 1
                break
            
        if is_parked == 0:
            for j in range(n_autobus):
                if places_autobus[j] <= start:
                    places_autobus[j] = end
                    is_parked = 1
                    break
                
                
    if is_parked == 0:
        counter_not_parked += 1        
print(counter_bus, counter_not_parked)
