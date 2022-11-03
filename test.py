from fastapi.testclient import TestClient

from application import app
from database import engine
import base64


client = TestClient(app)


def test_read_main():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"message": "Hello World!"}


def test_new_photo_set():
	response = client.get("/new_photo_set")
	assert response.status_code == 200


def test_new_photo():
	body = ""
	with open("test_photos/kitsune_with_wings.jpg", "rb") as bf:
		body = bf.read()
		body = base64.b64encode(body)
		body = body.decode("utf-8")

	response = client.post(
		"/new_photo",
		json={
			"body": body,
			"format": "jpg",
			"photo_set_id": 1}
	)
	photo = engine.execute(
		f"SELECT * FROM photos WHERE id={response.json()['photo_id']}").fetchone()
	assert photo[1] == body
	assert response.status_code == 200


