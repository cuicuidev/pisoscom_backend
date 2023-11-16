from fastapi import FastAPI
from pydantic import BaseModel
import glob
import pickle as pkl

class RequestForm(BaseModel):

    province: str | None
    lat: float | None
    lng: float | None
    n_bathrooms: int | None
    n_rooms: int | None
    surface: float | None
    net_surface: float | None
    garden: bool | None
    elevator: bool | None
    garage: bool | None
    condition: str | None
    age: float | None

class Prediction(BaseModel):
    price: float
    r2: float | None
    mae: float | None
    mse: float | None
    msle: float | None


app = FastAPI()

@app.get("/")
async def health():
    return {"status" : "server_is_running"}

@app.post("/predict")
async def predict(request_form: RequestForm):
    m_25 = False
    province = request_form.province

    model_paths = glob.glob("./*.pkl")
    model_path = [path for path in model_paths if province in path]

    if len(model_path) == 0:
        model_path = './model_25.pkl'
        m_25=True
    else:
        model_path = model_path[0]
    
    with open(model_path, 'br') as file:
        model = pkl.load(file)

    del file

    lat = request_form.lat
    lng = request_form.lng
    n_bathrooms = request_form.n_bathrooms
    n_rooms = request_form.n_rooms
    surface = request_form.surface
    net_surface = request_form.net_surface
    garden = request_form.garden
    elevator = request_form.elevator
    garage = request_form.garage
    age = request_form.age
    condition = request_form.condition

    if m_25:
        price = model.predict([[province,lat,lng,n_bathrooms,n_rooms,surface,net_surface,garden,elevator,garage,age,condition]])[0]
    else:
        price = model.predict([[lat,lng,n_bathrooms,n_rooms,surface,net_surface,garden,elevator,garage,age,condition]])[0]

    prediction = Prediction(price=price, r2=None, mae=None, mse=None, msle=None)

    return prediction