import requests as req
import random
from keys import get_keys

def get_places():
	url = "https://api.airtable.com/v0/appOiWDhJmuDQTTpm/Table%201?"
	headers = {
		"Authorization": f"Bearer {get_keys()['airtable']}"
	}

	res = req.get(url, headers = headers)

	if res.status_code in range(200, 300):
		return res.json()

	return {"error": True}

def get_processed_data(records):

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

		if instance["schedule"] != "abierto":
			for index, sc in enumerate(instance["schedule"]):
				instance["schedule"][index] = [h.strip() for h in sc]

		# Procesamiento de sentimientos
		instance["reviews"] = sentiment_analysis(record["fields"]["reviews"])

		data.append(instance)

	return data

def sentiment_analysis(reviews):
	score = max(0, len(reviews)) # Aquí, idealmente va un modelo de ML que detecte inseguridad o el sentimiento general del lugar

	phrases = [
		{"Recomendado": "40%", "Seguridad": "Poco Seguro"},
		{"Recomendado": "100%", "Seguridad": "Muy seguro"},
		{"Recomendado": "10%", "Seguridad": "Me asaltaron"},
		{"Recomendado": "0%", "Seguridad": "Asalté"},
		{"Recomendado": "80%", "Seguridad": "Seguro"},
	]

	return random.choice(phrases)