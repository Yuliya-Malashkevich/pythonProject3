from Transport.transport import Transport
from type_of_fuel.type_of_fuel import Type_of_fuel

class Underground_transport(Type_of_fuel,Transport): # подземный
    def move_underground(self):
        print("Move underground")

