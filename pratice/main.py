from fastapi import Body, FastAPI,Depends

import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




