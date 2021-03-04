from Transport.land_transport.land_transport import Land_transport

class Electric_bus(Land_transport):

    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)

Electric_bus1 = Electric_bus("Е433", "Belarus", "yellow", "60km/h", "2017")
Electric_bus1.electricity()