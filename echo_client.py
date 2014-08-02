# Echo client program
import socket
import sys
import time

HOST = 'localhost'    # The remote host
PORT = 10000              # The same port as used by the server
s = None
count = 1
# while True:
#     for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
#         af, socktype, proto, canonname, sa = res
#         try:
#             s = socket.socket(af, socktype, proto)
#         except socket.error as msg:
#             s = None
#             continue
#         try:
#             s.connect(sa)
#         except socket.error as msg:
#             s.close()
#             s = None
#             continue
#         # print '======', s
#         if s is None:
#             print 'could not open socket'
#             sys.exit(1)
#         s.sendall('Hello, world')
#         data = s.recv(1024)
#         count += 1
#         print count, data
#         # time.sleep(1)
#         s.close()

socks = []
pcount = 1
count = 1
counter = 0
while True:
    t = time.time()
    pcount += 1
    for i in xrange(5000):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((HOST, PORT + i + 5000*pcount))
            sock.connect((HOST, PORT))
            socks.append(sock)
            sock.sendall('Hello, world')
            data = sock.recv(1024)
            print 'Received', repr(data)
            sock.close()
            count += 1

            if pcount > 40:
                pcount = 1
            if time.time() - t > 1:
                counter = count - counter
                print '++++++', counter
                time.sleep(1)
                count = 0
                t = time.time()
            counter = 0
        except Exception, e:
            sock.close()
            print sock
            continue
        