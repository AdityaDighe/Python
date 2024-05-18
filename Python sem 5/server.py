import socket
def mpm():
    host="127.0.0.1"
    port=6000
    s=socket.socket()
    s.connect((host,port))
    print("Connection Established")
    while True:
        try:
            x=input("Enter a message: ")
            y=x.encode("ascii")
            s.send(y)
            data=s.recv(1024)
            d=data.decode("ascii")
            print("Server:",d)
        
        except KeyboardInterrupt:
            print("Connection Terminated")
            s.send("Connection form client terminated".encode("ascii"))
            break

mpm()
