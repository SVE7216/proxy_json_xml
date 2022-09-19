import pprint

from fastapi import FastAPI, APIRouter, Body
import requests
from servises.servises import Converter

app = FastAPI()
router = APIRouter()
app.include_router(router)


@app.post('/')
def root(user_post=Body(..., embed=True)):
    data = user_post
    headers = {
        'Content-Type': 'application/soap+xml;charset=utf-8'
    }

    body = Converter(data).json_to_xml()

    url = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso'
    try:
        response = requests.post(url=url, headers=headers, data=body).text
        json_format = Converter(response).xml_to_json()
        return json_format
    except Exception as error:
        print(error)

