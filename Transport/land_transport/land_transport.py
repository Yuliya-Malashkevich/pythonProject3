from Transport.transport import transport
from type_of_fuel.type_of_fuel import type_of_fuel

class land_transport(type_of_fuel,transport): # наземный
    def move_on_the_land(self):
        print("Move on the land")
        super().__init__()