from fastapi import FastAPI, HTTPException
import socket

app = FastAPI()
@app.post("/add/")
async def add_numbers(num1: float, num2: float):
    try:
        # 01 Initial/Unbound mode
        client_socket = socket.socket(
            socket.AF_INET,                          # AF_INET -> IPV4, It's mean IPV4 gonna communication with something like 192.168.1.1
            socket.SOCK_STREAM                       # Create communication between Socket
        )
        # 02 Bound Mode
        client_socket.connect(
            ("plus_service", 8081)                   # This is the name of container "plus_service"
        )  

        # 05 Communication mode
        # Message that separate with ,
        message = f"{num1},{num2}"
        encode_message = message.encode()            # Encode message
        client_socket.sendall(encode_message)        # send message ->

        # Receive the result
        result = client_socket.recv(1024).decode()   # <- Receive data 1024 byte from server then decode it
        client_socket.close()                        # close connection with Plus service
        result = float(result)                       # Convert result to float 

##################################################################################################################

        client_socket2 = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        client_socket2.connect(
            ("time_service", 8082)
        )
        message = f"{result}"
        encode_message = message.encode()
        client_socket2.sendall(encode_message)        # ->

        # Receive the result
        result = client_socket2.recv(1024).decode()   # <- Receive data 1024 byte from server then decode it
        client_socket2.close()                        # close connection with Plus service
        result = float(result)                       # Convert result to float 

##################################################################################################################

        client_socket3 = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        client_socket3.connect(
            ("diff_service", 8083)
        )
        message = f"{result}"
        encode_message = message.encode()
        client_socket3.sendall(encode_message)        # ->

        # Receive the result
        result = client_socket3.recv(1024).decode()   # <- Receive data 1024 byte from server then decode it
        client_socket3.close()                        # close connection with Plus service
        result = float(result)                        # Convert result to float 

##################################################################################################################

        client_socket4 = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        client_socket4.connect(
            ("minus_service", 8085)
        )
        message = f"{result}"
        encode_message = message.encode()
        client_socket4.sendall(encode_message)        # ->

        # Receive the result
        result = client_socket4.recv(1024).decode()   # <- Receive data 1024 byte from server then decode it
        client_socket4.close()                        # close connection with Plus service
        result = float(result)                        # Convert result to float 

##################################################################################################################
        return {"result": result}                     # then return it
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   # Raise error message
