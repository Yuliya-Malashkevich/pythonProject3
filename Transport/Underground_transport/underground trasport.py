from Transport.transport import transport
from  type_of_fuel.type_of_fuel import type_of_fuel

class underground_transport(type_of_fuel,transport): # подземный
    def move_underground(self):
        print("Move underground")

