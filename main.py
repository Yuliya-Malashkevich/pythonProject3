class transport:

    def __init__(self,brand,country_of_origin,color,maximum_speed,year):
        self.brand=brand
        self.country_of_origin=country_of_origin
        self.color=color
        self.maximum_speed=maximum_speed
        self.year=year
        print(self.brand,self.country_of_origin,self.color,self.maximum_speed,self.year)

    def move_in_space(self):
        print("Move in space")
#
# class type_of_fuel:
#      def diesel_fuel(self):
#         print("diesel fuel")
#      def gas(self):
#          print("gas")
#      def electricity(self):
#          print("electricity")
#      def petrol(self):
#          print("petrol")
#
#
# class underground_transport(type_of_fuel,transport): # подземный
#     def move_underground(self):
#         print("Move underground")
# class metro(underground_transport):
#     def __init__(self,brand,country_of_origin,color,maximum_speed,year):
#         super().__init__(brand,country_of_origin,color,maximum_speed,year)
# metro1=underground_transport("Stadler","Belarus","green","80km/h",2021)
# metro1.electricity()
#
# class land_transport(type_of_fuel,transport,): # наземный
#     def move_on_the_land(self):
#         print("Move on the land")
#
# class bus(land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#       super().__init__(brand,country_of_origin,color,maximum_speed,year)
# bus1=bus("МАЗ-215","Belarus","yellow","96km/h", 2018)
# bus1.diesel_fuel()
# class trolleybus(land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#         super().__init__(brand, country_of_origin, color, maximum_speed, year)
# trolleybus1 = trolleybus("МАЗ-103Т", "Belarus", "blue", "65km/h", 2019)
# trolleybus1.electricity()
# class tram(land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#         super().__init__(brand, country_of_origin, color, maximum_speed, year)
# tram1 = tram("АКСМ", "Belarus", "silver", "100km/h", 2017)
# tram1.electricity()
# class electric_bus(land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#         super().__init__(brand, country_of_origin, color, maximum_speed, year)
# electric_bus1 = electric_bus("Е433", "Belarus", "yellow", "60km/h", 2017)
# electric_bus1.electricity()
#
# class route_taxi(land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#         super().__init__(brand, country_of_origin, color, maximum_speed, year)
# route_taxi1 = route_taxi("Е433", "Belarus", "yellow", "60km/h", 2017)
# route_taxi1.diesel_fuel()
# class autotruck(land_transport): #грузовые
#     pass
# class passenger_car(land_transport):
#     pass
# class train(land_transport):
#     pass
# class diesel_train(land_transport):
#     pass
#
#
# class water_transport(transport):  # водный
#     pass
# class cruise_ship(water_transport):
#     pass
# class motorboat(water_transport): #моторная лодка
#     pass
# class refrigerator_ship(water_transport): #корабль
#     pass
# class ferry(water_transport): #паром
#     pass
# class tanker(water_transport):
#     pass
#
#
# class air_transport(transport): # воздушный
#     pass
# class airplane(air_transport):
#     pass
# class helicopter(air_transport):
#     pass
# class aerostat(air_transport): #воздушный шар
#      pass
#
#
