from Transport.water_transport.water_transport import Water_transport

class Ferry(Water_transport): #паром
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Water_transport.__init__(self, brand, country_of_origin, color, maximum_speed, year)