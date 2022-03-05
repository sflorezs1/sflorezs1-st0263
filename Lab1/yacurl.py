#!/usr/bin/env python3
import socket
import argparse
import ssl
from xml.dom.minidom import parseString


HTTP_VERSION = 'HTTP/1.0'
CRLF = '\r\n'


def get_args():
    parser = argparse.ArgumentParser(
        prog='yacurl', description='Yet Another Curl. A python cli toy http client that only uses GET method.')
    # parser.add_argument('-m', '--method', help='Specify the HTTP method to use.',
    #                     required=False, default='GET', type=str)
    # Como no se especifica el uso de otros verbos http, se asume que solo se va a usar GET, sin embargo queda la posibilidad
    parser.add_argument(
        '-H', '--host', help='Specify the host ip/url to direct the request to.', required=True, type=str)
    parser.add_argument(
        '-p', '--port', help='Specify the port to direct the request to.', required=True, type=int, default=80)
    parser.add_argument(
        '-o', '--output', help='Specify a file to save the requested data.', required=False, type=str)
    parser.add_argument('-r', '--resource', help='Resource to locate.',
                        required=False, default='/', type=str)
    parser.add_argument('-d', '--download-statics', help='Download static resources from the html page.',
                        required=False, default=False, type=bool)
    args = parser.parse_args()
    return 'GET', args.host, args.port, args.output, args.resource, args.download_statics

def print_separator():
    print('============================================================')

def http_request(resource, host, port, method, output, ds):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        if method.upper() not in ('GET',):
            raise Exception('Unimplemented method "{method}"')

        request = f"{method.upper()} {resource} {HTTP_VERSION}{CRLF}Host: {host}{CRLF}{CRLF}"
        
        print_separator()
        print('Request:')
        print_separator()
        print(request)
        print_separator()
        s.sendall(request.encode())
        data = b''
        curr = s.recv(1024)
        while curr:
            data += curr
            curr = s.recv(1024)
        
        code, status, headers, body = parse_http_response(data)

        print_separator()
        print(f'Response:')
        print_separator()
        print(f'Status: {code.decode()} {status.decode()}')
        print_separator()
        for i, j in headers.items():
            print(f'{i}: {j}')
        print_separator()

        if resource == '/' or ('Content-Type' in headers and 'text/html' in  headers['Content-Type']):
            if ds:
                body = parse_html(body, host, port)

        if not output:
            print(body)
        else:
            print(f'Saving body in {output}')

            if isinstance(body, str):
                save_file(output, body.encode('utf-8'))
            else:
                save_file(output, body)
            
            print('Results saved!')


def save_file(filename, data_bytes):
    from pathlib import Path

    last = filename.rfind('/')
    if last != -1:
        dir = filename[:last]

        Path(dir).mkdir(parents=True, exist_ok=True)

    with open(filename, 'wb') as f:
        f.write(data_bytes)

def main():
    method, host, port, output, resource, ds = get_args()
    print('Method:', method)
    print('Host:', host)
    print('Port:', port)

    http_request(resource, host, port, method, output, ds)

def parse_http_response(response):
    data = response.split((CRLF * 2).encode())
    lines = data[0].split(CRLF.encode())

    code = lines[0].split(b' ')[1]
    status = b' '.join(lines[0].split(b' ')[2:])

    # Convierte los headers en un diccionario de python
    # Parte los headers en el CRLF
    # Cada linea que salga se parte en el primer ':' desde la izquierda
    # la parte de la izquierda es el key y lo restante el valor
    headers = {
        i.split(':')[0].strip() : ':'.join(i.split(':')[1:]).strip()
        for i in CRLF.encode().join(lines[1:-1]).decode().split(CRLF)
    }


    if 'Content-Type' in headers:
        if 'charset' in headers['Content-Type']:
            content_type = headers['Content-Type'][:headers['Content-Type'].find(';')]
            charset = headers['Content-Type'][headers['Content-Type'].find('charset') + len('charset') + 1:]
            print(f'Detected {content_type} used {charset} encoding')
        else:
            content_type = headers['Content-Type']
            charset = ''
            print(f'Detected {content_type} without encoding')
    else:
        charset = ''

    if 'Content-Type' in headers and 'text' in headers['Content-Type']:
        if charset:
            body = CRLF.encode().join(data[1:]).decode(charset)
        else:
            body = CRLF.encode().join(data[1:]).decode()
    else:
        body = CRLF.encode().join(data[1:])

    return code, status, headers, body

def parse_html(html, host, port):
    # create a temporal DOM from the html
    if html:
        dom = parseString(html)
        allsrc = [
            *dom.getElementsByTagName('audio'),
            *dom.getElementsByTagName('embed'),
            *dom.getElementsByTagName('iframe'),
            *dom.getElementsByTagName('img'),
            *dom.getElementsByTagName('input'),
            *dom.getElementsByTagName('script'),
            *dom.getElementsByTagName('source'),
            *dom.getElementsByTagName('track'),
            *dom.getElementsByTagName('video'),
        ]

        for tag in allsrc:
            file = tag._attrs['src'].nodeValue
            if file[0] == '/':
                file = file[1:]
                tag._attrs['src'].nodeValue = file
            http_request(f'/{file}', host, port, 'GET', file, False)
        
        return dom.toxml()
    else:
        return html

if __name__ == "__main__":
    main()
