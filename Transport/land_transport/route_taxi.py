from Transport.land_transport.land_transport import Land_transport

class Route_taxi(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)
Route_taxi1 = Route_taxi("Mercedes_Benz", "Germany", "white", "220km/h", 2018)
Route_taxi1.diesel_fuel()