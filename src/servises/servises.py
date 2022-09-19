import json
import xmltodict


class Converter:
    """Класс для работы с конвертацией xml  в json"""
    def __init__(self, data):
        self.data = data

    def xml_to_json(self):
        dict_xml = xmltodict.parse(self.data)
        dict_xml = dict(dict_xml)['soap:Envelope']['soap:Body']['m:NumberToWordsResponse']['m:NumberToWordsResult']
        json_format = json.dumps(dict_xml)
        return json_format


    def json_to_xml(self):
        body = f'''<?xml version="1.0" encoding="utf-8"?>
                    <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                     <soap12:Body>
                    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
                    <ubiNum>{self.data}</ubiNum>
                     </NumberToWords>
                    </soap12:Body>
                    </soap12:Envelope>'''
        return body
