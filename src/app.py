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

    body =f'''<?xml version="1.0" encoding="utf-8"?>
            <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
             <soap12:Body>
            <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
            <ubiNum>{data}</ubiNum>
             </NumberToWords>
            </soap12:Body>
            </soap12:Envelope>'''

    url = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso'
    try:
        response = requests.post(url=url, headers=headers, data=body).text
        json_obg = Converter(response)
        json_format = json_obg.xml_to_json()
        return json_format
    except Exception as error:
        print(error)
