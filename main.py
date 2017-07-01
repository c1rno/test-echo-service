#!/usr/bin/env python3

import sys, socket, traceback

DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = 8000
DEFAULT_CHUNK = 4096


def make_service(host, port):
    # the actual server starts here
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.setblocking(False)  # too lazy to use `select`
    s.listen(5)
    return s


def mirror_data(provider, chunk):
    try:
        clientsock, clientaddress = provider.accept()
    except Exception as ex:
        print('[{}] {}'.format(clientaddress, ex))
        return

    print('\nAccept conn with {}({})'.format(clientaddress, clientsock))
    data = clientsock.recv(chunk)
    if not data:
        return
    print('[{}] send {}'.format(clientaddress, data))

    clientsock.sendall(data)

    return data


def run(host=DEFAULT_HOST, port=DEFAULT_PORT, chunk=DEFAULT_CHUNK):
    print('Listen on {}:{}'.format(host, port))
    stop = False
    while not stop:
        provider = make_service(host, port)
        try:
            mirror_data(provider, chunk)
        except KeyboardInterrupt as ex:
            stop = True
            print('Normal app stopping...\n')
        except Exception as ex:
            traceback.print_exc()
        finally:
            provider.close()


if __name__ == '__main__':
    print('''Example args format:
    ./main.py 0.0.0.0:8000''')

    if len(sys.argv) > 1:
        host, port = sys.argv[1].split(':')
        run(host, int(port))
    else:
        run()
