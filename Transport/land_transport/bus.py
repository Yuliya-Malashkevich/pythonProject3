from Transport.land_transport import land_transport

class Bus(land_transport.land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
      land_transport.land_transport.__init__(self,brand,country_of_origin,color,maximum_speed,year)

Bus1=Bus("МАЗ-215","Belarus","yellow","96km/h", "2018")
Bus1.diesel_fuel()