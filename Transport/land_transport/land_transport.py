from Transport.transport import Transport
from type_of_fuel.type_of_fuel import Type_of_fuel

class Land_transport(Type_of_fuel,Transport): # наземный
    def move_on_the_land(self):
        print("Move on the land")
        super().__init__()