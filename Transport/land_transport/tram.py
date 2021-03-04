from Transport.land_transport.land_transport import Land_transport


class Tram(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)


Tram1 = Tram("АКСМ", "Belarus", "silver", "100km/h", 2017)
Tram1.electricity()