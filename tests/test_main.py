# -*- coding: utf-8 -*-
from requests.sessions import Session


def test_main_root(client: Session) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello World": "This is a sample API!"}
