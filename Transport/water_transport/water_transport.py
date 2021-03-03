from Transport.transport import transport
from type_of_fuel.type_of_fuel import type_of_fuel

class water_transport(type_of_fuel,transport):  # водный
    def move_on_water(self):
        print("Move on water")