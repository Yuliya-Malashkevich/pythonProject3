from Transport.Underground_transport import Underground_transport

class metro(underground_transport):
    def __init__(self,brand,country_of_origin,color,maximum_speed,year):
        super().__init__(brand,country_of_origin,color,maximum_speed,year)
metro1=metro("Stadler","Belarus","green","80km/h",2021)
metro1.electricity()