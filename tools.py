import requests as req
import random

def get_places():
	url = "https://api.airtable.com/v0/appOiWDhJmuDQTTpm/Table%201?"
	headers = {
		"Authorization": "Bearer keyEzf2F0aQJppJV4"
	}

	res = req.get(url, headers = headers)

	if res.status_code in range(200, 300):
		return res.json()

	return {"error": True}


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