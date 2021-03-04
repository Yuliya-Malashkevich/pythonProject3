from Transport.land_transport.land_transport import Land_transport

class Autotruck(Land_transport): #грузовые
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self, brand, country_of_origin, color, maximum_speed, year)
