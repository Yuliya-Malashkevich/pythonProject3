from Transport.land_transport.land_transport import Land_transport

class Bus(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
      Land_transport.__init__(self,brand,country_of_origin,color,maximum_speed,year)

Bus1=Bus("МАЗ-215","Belarus","yellow","96km/h", "2018")
Bus1.diesel_fuel()