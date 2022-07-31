import wData_provider as prov
import wLogger as log

def temperature_view(senser):
    data = prov.get_temperature(senser)
    log.temp_logger(data)
    return data

def pressure_view(senser):
    data = prov.get_preassure(senser)
    log.pressure_logger(data)
    return data

def wind_speed_view(senser):
    data = prov.get_wind_speed(senser)
    log.wind_speed_logger(data)
    return data