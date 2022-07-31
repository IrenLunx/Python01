from random import randint

def get_temperature(senser): # температура
    return randint(-20, 0) if senser else randint(0, 20)

def get_preassure(senser): # давление
    if senser:
        return randint(720, 750)
    else:
        return randint(750, 770)

def get_wind_speed(senser): # скорость ветра
    if senser == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)

def data_collection():
    senser = 1
    return(get_temperature(senser), get_preassure(senser), get_wind_speed(senser))