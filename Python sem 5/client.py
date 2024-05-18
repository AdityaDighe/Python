import socket

def mpm():
    host="127.0.0.1"
    port=6000
    s=socket.socket()
    s.bind((host,port))
    s.listen(1)
    print("Waiting for connection")
    c,addr=s.accept()
    print("Connection Established")
    print("Client address: ",addr)
    while True:
        try:
            data=c.recv(1024)
            d=data.decode("ascii")
            print("Client: ",d)
            x=input("Enter a message: ")
            y=x.encode("ascii")
            c.send(y)

        except KeyboardInterrupt:
            print("Connection terminated")
            break
    
mpm()
