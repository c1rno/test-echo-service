# test-echo-service
just return raw req back (sort of mirror)
```
$ ./main.py 127.0.0.1:8001
Example args format:
    ./main.py 0.0.0.0:8000
Listen on 127.0.0.1:8001

[1]+  Stopped                 ./main.py 127.0.0.1:8001
$ curl -X POST --data "param1=value1&param2=value2" http://127.0.0.1:8001
$ fg
./main.py 127.0.0.1:8001

Accept conn with ('127.0.0.1', 51531)(<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8001), raddr=('127.0.0.1', 51531)>)
[('127.0.0.1', 51531)] send b'POST / HTTP/1.1\r\nHost: 127.0.0.1:8001\r\nUser-Agent: curl/7.54.1\r\nAccept: */*\r\nContent-Length: 27\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nparam1=value1&param2=value2'

Normal app stopping...
$
```
