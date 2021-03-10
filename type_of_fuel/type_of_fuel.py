

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

    def electric_fuel(self):
        amount = float(input('Введите объем в киловаттах: '))
        print('Получено киловатт электричества - ', amount)

    def jet_fuel(self):
        amount = float(input('Введите объем в литрах: '))
        print('Получено литров реактивного топлива - ', amount)

    def menu(self):
        act = int(input('ЗАПРАВКА' '\n' '1. - Бензин' '\n' '2. - Дизельное топливо' '\n' '3. - Мазут' '\n' '4. - Керосин' '\n' '5. - Газ' '\n' '6. - Электричество' '\n' '7. - Реактивное топливо' '\n' 'Выбериите вид топлива(введите цифру):  '))
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
            Type_of_fuel.electric_fuel(self)
        elif act == 7:
            Type_of_fuel.jet_fuel(self)
        else:
            Type_of_fuel.menu(self)
my_Fuel = Type_of_fuel()
my_Fuel.menu()





# def diesel_fuel(self):
#         print("diesel fuel")
#      def gas(self):
#         print("gas")
#      def electricity(self):
#         print("electricity")
#      def petrol(self):
#         print("petrol")
#
# class Fuel: