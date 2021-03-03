from Transport.transport import transport
from type_of_fuel.type_of_fuel import type_of_fuel


class air_transport(type_of_fuel,transport):  # воздушный
    def move_in_the_air(self):
        print("Move in the air")