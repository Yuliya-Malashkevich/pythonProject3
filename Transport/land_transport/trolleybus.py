from Transport.land_transport.land_transport import Land_transport
class Trolleybus(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        super().__init__(brand, country_of_origin, color, maximum_speed, year)
Trolleybus1 = Trolleybus("МАЗ-103Т", "Belarus", "blue", "65km/h", 2019)
Trolleybus1.electricity()