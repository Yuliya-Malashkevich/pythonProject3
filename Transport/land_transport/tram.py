from Transport.land_transport import land_transport


class tram(land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        super().__init__().__init__(brand, country_of_origin, color, maximum_speed, year)


tram1 = tram("АКСМ", "Belarus", "silver", "100km/h", 2017)
tram1.electricity()