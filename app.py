from litestar import Litestar, get

from users_managment.controller import UserController
from calculations.Water_general.controller import WaterCalcController
from calculations.Sheveleva_tables.controller import ShevelevController
from calculations.Steam_calc.controller import SteamPipeController


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    return {"book_id": book_id}


app = Litestar(route_handlers=[UserController, 
                               WaterCalcController, 
                               ShevelevController,
                               SteamPipeController], 
                               debug=True)

