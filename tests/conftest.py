# -*- coding: utf-8 -*-
from typing import Generator

import pytest
from requests.sessions import Session
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client() -> Generator[Session, None, None]:
    with TestClient(app) as client:
        yield client
