#!/usr/bin/python
from redis import StrictRedis
import argparse
import getpass


def get_args():
    parser = argparse.ArgumentParser('redis_update', description='Example python application to test the update function in redis.')
    parser.add_argument('-H', '--host', help='IP of the host to connect to.')
    parser.add_argument('-p', '--port', help='Port in which the redis server is listening in the host.')
    parser.add_argument('-k', '--key', help='Key of the value to update.')
    parser.add_argument('-v', '--value', help='Value to store.')
    result = parser.parse_args()
    return result.host, result.port, result.key, result.value

def main():
    host, port, key, value = get_args()

    password = getpass.getpass('Password:')

    print(f'Searching for "{key}"')
    r = StrictRedis(host=host, port=port, password=password, db=0)
    result = r.get(key)
    if result:
        r.set(key, value)
        print(f'key "{key}" was set to "{result.decode()}"')
        print(f'key "{key}" is now set to "{value}"')
    else:
        raise Exception(f'There is no such key = "{key}"')


if __name__ == '__main__':
    main()

