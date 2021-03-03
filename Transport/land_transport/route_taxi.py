from Transport.land_transport import land_transport

class route_taxi(land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        super().__init__(brand, country_of_origin, color, maximum_speed, year)
route_taxi1 = route_taxi("Е433", "Belarus", "yellow", "60km/h", 2017)
route_taxi1.diesel_fuel()