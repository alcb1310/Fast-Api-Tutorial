import json


def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
    }
    response = client.post("/jobs/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_read_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
    }
    response = client.post("/jobs/", json.dumps(data))

    response = client.get("/jobs/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "SDE super"

    response = client.get("/jobs/2")
    assert response.status_code == 404


def test_read_all_jobs(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/", json.dumps(data))
    client.post("/jobs/", json.dumps(data))

    response = client.get("/jobs/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/", json.dumps(data))

    data["title"] = "test new title"

    response = client.put("/jobs/1", json.dumps(data))

    assert response.json()["msg"] == "Successfully updated data."
