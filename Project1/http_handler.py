from enum import Enum
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from unittest import result
from urllib.parse import urlparse
import json

from .api import API


class HTTPMethods(Enum):
    GET = 1
    POST = 2
    PUT = 3



class HTTPHandler(BaseHTTPRequestHandler):

    def __process_request(self, method):

        api = API(self)

        parsed_path = urlparse(self.path)

        match method:
            case HTTPMethods.GET:
                result, status_code = api.process_request(parsed_path)()
            case (HTTPMethods.POST | HTTPMethods.PUT):
                content_length = int(self.headers.get('content-length', 0))
                content = json.loads(self.rfile.read(content_length))
                result, status_code = api.process_request(parsed_path)(**{
                    'data': content
                })
            case _:
                raise Exception(f'Method "{method}" is not a valid method or is not allowed!')
        

    def do_GET(self):
        return self.__process_request(HTTPMethods.GET)

    def do_POST(self):
        return self.__process_request(HTTPMethods.POST)

    def do_PUT(self):
        return self.__process_request(HTTPMethods.PUT)