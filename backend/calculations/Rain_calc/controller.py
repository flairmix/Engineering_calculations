from litestar import Controller, get
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from pydantic import Field, ValidationError, validate_call
from typing_extensions import Annotated
from typing import Optional, Literal


class RainCalcController(Controller):
    path = "/rain_calc"
    tags=["rain_calc"]

    @get("/")
    @validate_call
    async def rain_calc(self) -> dict[str, float]:
        
        try:
            return {"velocity m/s": 123 } 

        
        except ValidationError as exc:
            return {"ValidationError": -1}
        