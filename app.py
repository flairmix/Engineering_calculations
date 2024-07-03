from litestar import Litestar, get

from users_managment.controller import UserController
from calculations.Water_general.controller import WaterCalcController
from calculations.Sheveleva_tables.controller import ShevelevController
from calculations.Rain_calc.controller import RainCalcController


app = Litestar(route_handlers=[UserController, 
                               WaterCalcController, 
                               ShevelevController, 
                               RainCalcController], 
                               debug=True)