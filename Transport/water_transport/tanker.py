from Transport.water_transport.water_transport import Water_transport

class Tanker(Water_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Water_transport.__init__(self, brand, country_of_origin, color, maximum_speed, year)