from Transport.transport import Transport
from type_of_fuel.type_of_fuel import Type_of_fuel

class Water_transport(Type_of_fuel,Transport):  # водный
    def move_on_water(self):
        print("Move on water")
