from pydantic import BaseModel


class Data(BaseModel):
    address_id: int
    full_name: str
    house_no: str
    road_name_Area: str
    landmark: str
    country: str
    city: str
    latitude: str
    longitude: str
    
