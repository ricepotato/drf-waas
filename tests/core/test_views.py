import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from core import models

# Only one global marker (most commonly used)
pytestmark = pytest.mark.unit
# Several global markers
endpoint = "/api/users/"


@pytest.mark.django_db
def test_list(api_client: APIClient):

    # billings = models.Billing.objects.all()
    baker.make(models.WassUser, _quantity=3)

    response = api_client.get(endpoint)
    assert response.status_code == 200
    response_json = json.loads(response.content)
    assert len(response_json["results"]) == 3


@pytest.mark.django_db
def test_create(api_client: APIClient):
    user = baker.prepare(models.WassUser)
    expected_json = {
        "name": user.name,
        "email": user.email,
        "profile": user.profile,
        "password": user.password,
    }

    response = api_client.post(endpoint, data=expected_json, format="json")
    assert response.status_code == 201
    response_json = json.loads(response.content)
    assert response_json["name"] == expected_json["name"]
    assert response_json["email"] == expected_json["email"]
    assert response_json["profile"] == expected_json["profile"]
    assert response_json["password"] == expected_json["password"]
    assert response_json["created_at"]


@pytest.mark.django_db
def test_retrive(api_client: APIClient):
    user = baker.make(models.WassUser)
    expected_json = {
        "name": user.name,
        "email": user.email,
        "profile": user.profile,
        "password": user.password,
    }

    url = f"{endpoint}{user.id}/"

    response = api_client.get(url)
    assert response.status_code == 200
    response_json = json.loads(response.content)
    assert response_json["name"] == expected_json["name"]
    assert response_json["email"] == expected_json["email"]
    assert response_json["profile"] == expected_json["profile"]
    assert response_json["password"] == expected_json["password"]
