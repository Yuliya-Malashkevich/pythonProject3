from Transport.land_transport import land_transport

class bus(land_transport.land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
      land_transport.land_transport.__init__(self,brand,country_of_origin,color,maximum_speed,year)

bus1=bus("МАЗ-215","Belarus","yellow","96km/h", "2018")
bus1.diesel_fuel()