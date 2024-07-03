from litestar import Controller, get
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from pydantic import Field, ValidationError, validate_call
from typing_extensions import Annotated
from typing import Optional

class WaterCalcController(Controller):
    path = "/water_calc"
    tags=["water_calc"]

    @get("/convert_power")
    @validate_call
    async def convert_GCalh_to_kW(self, 
                                  power_value: Annotated[float,Field(gt=0)],
                                  power_unit_in: str = "GCalh",
                                  power_unit_out: str = "KW"
                                  ) -> dict[str, float]:
        try:
            power_value_temp_GCalh = 0
            if (power_unit_in == "GCalh" and power_unit_out == "KW"):
                return {"power_GCalh": power_value, 
                        "power_KW": round(power_value * 1163.0, 3)}
        except ValidationError as exc:
            return {"ValidationError": -1}
        
