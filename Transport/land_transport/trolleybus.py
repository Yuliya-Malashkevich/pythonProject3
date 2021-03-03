from Transport.land_transport import land_transport
class trolleybus(land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        super().__init__(brand, country_of_origin, color, maximum_speed, year)
trolleybus1 = trolleybus("МАЗ-103Т", "Belarus", "blue", "65km/h", 2019)
trolleybus1.electricity()