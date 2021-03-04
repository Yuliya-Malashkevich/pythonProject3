from Transport.transport import Transport
from type_of_fuel.type_of_fuel import Type_of_fuel


class Air_transport(Type_of_fuel,Transport):  # воздушный
    def move_in_the_air(self):
        print("Move in the air")