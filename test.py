import zmq
import json


# Set up environment and sockets
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)

# Connect to server socket
socket.connect("tcp://localhost:5556")

# Setup request for arithmetic service
request = {
    "service_key": "arithmetic",
    "data": {
        "num_1": 10,
        "num_2": 5
    }
}

# Send request
print("Sending request...")
socket.send_json(request)

# Get the reply
message = socket.recv()
response = json.loads(message.decode())

# Print response
print("Received response from server:")
print(response)
