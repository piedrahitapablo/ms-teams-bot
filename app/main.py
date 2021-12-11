# -*- coding: utf-8 -*-
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> Dict[str, str]:
    return {"Hello World": "This is a sample API!"}
