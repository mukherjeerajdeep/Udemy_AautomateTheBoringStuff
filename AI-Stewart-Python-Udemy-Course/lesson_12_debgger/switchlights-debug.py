market_2nd = {'ns': 'green',
              'ew': 'red'
              }


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    # assert says that this condition is always true otherwise it's a problem
    # so if none of this is 'red' {'ns': 'yellow', 'ew': 'green'} means the traffic
    # is going in all directions
    assert 'red' in intersection.values(), 'neither light is red!' + str(intersection)


print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
