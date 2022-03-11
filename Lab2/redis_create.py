#!/usr/bin/python
from redis import StrictRedis
import argparse
import getpass


def get_args():
    parser = argparse.ArgumentParser('redis_create', description='Example python application to test the create function in redis.')
    parser.add_argument('-H', '--host', help='IP of the host to connect to.')
    parser.add_argument('-p', '--port', help='Port in which the redis server is listening in the host.')
    parser.add_argument('-k', '--key', help='Key of the value to store.')
    parser.add_argument('-v', '--value', help='Value to store.')
    result = parser.parse_args()
    return result.host, result.port, result.key, result.value

def main():
    host, port, key, value = get_args()

    password = getpass.getpass('Password:')

    print(f'Setting "{key}" to "{value}"')
    r = StrictRedis(host=host, port=port, password=password, db=0)
    r.set(key, value)
    print(f'{key} was set successfully!')


if __name__ == '__main__':
    main()

