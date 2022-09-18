import json
import xmltodict


class Converter:
    """Класс для работы с конвертацией xml  в json"""
    def __init__(self, data):
        self.data = data

    def xml_to_json(self):
        json_format = json.dumps(xmltodict.parse(self.data))
        return json_format

