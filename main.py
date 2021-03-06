class Transport:

    def __init__(self,brand,country_of_origin,color,maximum_speed,year):
        self.brand=brand
        self.country_of_origin=country_of_origin
        self.color=color
        self.maximum_speed=maximum_speed
        self.year=year
        print(self.brand,self.country_of_origin,self.color,self.maximum_speed,self.year)

    def move_in_space(self):
        print("Move in space")


class Type_of_fuel:
    def diesel_fuel(self):
        print("diesel fuel")
    def gas(self):
        print("gas")
    def electricity(self):
        print("electricity")
    def petrol(self):
        print("petrol")

class Underground_transport(Type_of_fuel,Transport): # подземный
    def move_underground(self):
        print("Move underground")

class Metro(Underground_transport):
    def __init__(self,brand,country_of_origin,color,maximum_speed,year):
        Underground_transport.__init__(self,brand,country_of_origin,color,maximum_speed,year)
Metro1=Metro("Stadler","Belarus","green","80km/h",2021)
Metro1.electricity()

class Land_transport(Type_of_fuel,Transport): # наземный
    def move_on_the_land(self):
        print("Move on the land")

class Bus(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
      Land_transport.__init__(self,brand,country_of_origin,color,maximum_speed,year)

Bus1=Bus("МАЗ-215","Belarus","yellow","96km/h", "2018")
Bus1.diesel_fuel()

class Trolleybus(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)
Trolleybus1 = Trolleybus("МАЗ-103Т", "Belarus", "blue", "65km/h", 2019)
Trolleybus1.electricity()

class Tram(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)


Tram1 = Tram("АКСМ", "Belarus", "silver", "100km/h", 2017)
Tram1.electricity()

# class Electric_bus(Land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#         super().__init__(brand, country_of_origin, color, maximum_speed, year)
# Electric_bus1 = electric_bus("Е433", "Belarus", "yellow", "60km/h", 2017)
# Electric_bus1.electricity()
#
# class Route_taxi(Land_transport):
#     def __init__(self, brand, country_of_origin, color, maximum_speed, year):
#         super().__init__(brand, country_of_origin, color, maximum_speed, year)
# Route_taxi1 = Route_taxi("Е433", "Belarus", "yellow", "60km/h", 2017)
# Route_taxi1.diesel_fuel()
# class Autotruck(Land_transport): #грузовые
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
