from Transport.land_transport import land_transport

class electric_bus(land_transport.land_transport):

    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        land_transport.land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)

electric_bus1 = electric_bus("Е433", "Belarus", "yellow", "60km/h", "2017")
electric_bus1.electricity()