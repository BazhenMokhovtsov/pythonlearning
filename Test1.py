def rout_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your distenation is {route['distance']}"

    if ('speed' in route) and ('time' in route):
        return f"Distance to your distenation is {route['speed'] * route['time']}"

    return f"No distance info is avalible"


print(rout_info({'distance': 15, 'speed': 100, 'time': 1}))
print(rout_info({'speed': 100, 'time': 1}))
print(rout_info({'speed': 'asd'}))