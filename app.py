from fastapi  import FastAPI
from tools import get_places, get_processed_data

app = FastAPI()

@app.get("/")
def home():
	return {"mensaje": "Hola Hackathoneros"}

@app.get("/get-places")
def places():
	places = get_places()

	records = places["records"]

	data = get_processed_data(records)

	return data
