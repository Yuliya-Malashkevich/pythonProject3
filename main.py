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

    def gasoline(self):
        amount = float(input('Введите объем в литрах: '))
        print('Получено литров бензина - ', amount)

    def diesel_fuel(self):
        amount = float(input('Введите объем в литрах: '))
        print('Получено литров дизельного топлива - ', amount)

    def fuel_oil(self):
        amount = float(input('Введите объем в литрах: '))
        print('Получено литров мазута - ', amount)

    def kerosene(self):
        amount = float(input('Введите объем в литрах: '))
        print('Получено литров керосина - ', amount)

    def gas(self):
        amount = float(input('Введите объем в кубах: '))
        print('Получено кубов газа - ', amount)

    def electricity(self):
        amount = float(input('Введите объем в киловаттах: '))
        print('Получено киловатт электричества - ', amount)

    def jet_fuel(self):
        amount = float(input('Введите объем в литрах: '))
        print('Получено литров реактивного топлива - ', amount)

    def menu(self):
        act = int(input(
            'ЗАПРАВКА' '\n' '1. - Бензин' '\n' '2. - Дизельное топливо' '\n' '3. - Мазут' '\n' '4. - Керосин' '\n' '5. - Газ' '\n' '6. - Электричество' '\n' '7. - Реактивное топливо' '\n' 'Выбериите вид топлива(введите цифру):  '))
        if act == 1:
            Type_of_fuel.gasoline(self)
        elif act == 2:
            Type_of_fuel.diesel_fuel(self)
        elif act == 3:
            Type_of_fuel.fuel_oil(self)
        elif act == 4:
            Type_of_fuel.kerosene(self)
        elif act == 5:
            Type_of_fuel.gas(self)
        elif act == 6:
            Type_of_fuel.electricity(self)
        elif act == 7:
            Type_of_fuel.jet_fuel(self)
        else:
            Type_of_fuel.menu(self)


# my_Fuel = Type_of_fuel()
# my_Fuel.menu()

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

class Electric_bus(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)
Electric_bus1 = Electric_bus("Е433", "Belarus", "yellow", "60km/h", 2017)
Electric_bus1.electricity()

class Route_taxi(Land_transport):
    def __init__(self, brand, country_of_origin, color, maximum_speed, year):
        Land_transport.__init__(self,brand, country_of_origin, color, maximum_speed, year)
Route_taxi1 = Route_taxi("Mercedes_Benz", "Germany", "white", "220km/h", 2018)
Route_taxi1.diesel_fuel()

class Autotruck(Land_transport): #грузовые
    pass
class Passenger_car(Land_transport):
    pass
class Train(Land_transport):
    pass
class Diesel_train(Land_transport):
    pass


class Water_transport(Type_of_fuel,Transport):  # водный
    pass
class Cruise_ship(Water_transport):
    pass
class Motorboat(Water_transport): #моторная лодка
    pass
class Refrigerator_ship(Water_transport): #корабль
    pass
class Ferry(Water_transport): #паром
    pass
class Tanker(Water_transport):
    pass

class Air_transport(Type_of_fuel,Transport): # воздушный
    pass
class Airplane(Air_transport):
    pass
class Helicopter(Air_transport):
    pass
class Aerostat(Air_transport): #воздушный шар
     pass


