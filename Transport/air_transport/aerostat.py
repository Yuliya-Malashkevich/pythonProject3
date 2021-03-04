from Transport.air_transport.air_transport import Air_transport

class Aerostat(Air_transport): #воздушный шар
     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
          Air_transport.__init__(self, brand, country_of_origin, color, maximum_speed, year)