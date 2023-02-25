from fastapi  import FastAPI
from tools import get_places, sentiment_analysis

app = FastAPI()

@app.get("/")
def home():
	return {"mensaje": "Hola Hackathoneros"}

@app.get("/get-places")
def places():
	places = get_places()

	records = places["records"]


	data = []
	for record in records:
		instance = dict()
		instance["img"] = record["fields"]["img"][0]["url"]
		instance["name"] = record["fields"]["name"]
		instance["description"] = record["fields"]["description"]
		
		if "days" in record["fields"]:
			instance["days"] = record["fields"]["days"]
		else:
			instance["days"] = "todos"
		
		# Proceso de horario
		instance["schedule"] = "abierto"
		if "schedule" in record["fields"]:
			instance["schedule"] = record["fields"]["schedule"].split("y")
			instance["schedule"] = [hora.split("a") for hora in instance["schedule"]]

		# Procesamiento de sentimientos
		instance["reviews"] = sentiment_analysis(record["fields"]["reviews"])

		data.append(instance)


	return data
