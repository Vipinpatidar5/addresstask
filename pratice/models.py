from tokenize import String
from database import Base
from sqlalchemy import Column, Integer,String

class Address(Base):
    __tablename__="address"
 
    address_id = Column(Integer(), autoincrement=True, primary_key=True)
    full_name = Column(String())
    house_no = Column(String())
    road_name_Area = Column(String())
    landmark = Column(String())
    country = Column(String())
    city = Column(String())
    latitude = Column(String())
    longitude = Column(String())
