from Transport.underground_transport.underground_trasport import Underground_transport

class Metro(Underground_transport):
    def __init__(self,brand,country_of_origin,color,maximum_speed,year):
        Underground_transport.__init__(self,brand,country_of_origin,color,maximum_speed,year)
Metro1=Metro("Stadler","Belarus","green","80km/h",2021)
Metro1.electricity()