#!/usr/bin/python
from redis import StrictRedis
import argparse
import getpass


def get_args():
    parser = argparse.ArgumentParser('redis_delete', description='Example python application to test the delete function in redis.')
    parser.add_argument('-H', '--host', help='IP of the host to connect to.')
    parser.add_argument('-p', '--port', help='Port in which the redis server is listening in the host.')
    parser.add_argument('-k', '--key', help='Key of the value to delete.')
    result = parser.parse_args()
    return result.host, result.port, result.key

def main():
    host, port, key = get_args()

    password = getpass.getpass('Password:')

    print(f'Searching for "{key}"')
    r = StrictRedis(host=host, port=port, password=password, db=0)
    result = r.get(key)
    if result:
        print('key found, proceeding to delete!')
        r.delete(key)
        print(f'key "{key}" was deleted!')
    else:
        raise Exception(f'There is no such key = "{key}"')


if __name__ == '__main__':
    main()

