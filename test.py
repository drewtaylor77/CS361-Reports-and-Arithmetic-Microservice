import zmq


# Set up environment and sockets
context = zmq.Context()
print("Client attempting to connect to server...")
socket = context.socket(zmq.REQ)

# Connect to server socket
socket.connect("tcp://localhost:5556")

# Setup request for battle_logic service
request_dmg = {
    "service_key": "battle_logic",
    "data": {
        "attack": 10,
        "defense": 5,
        "crit": 1.5
    }
}

# Send request
print("Sending request...")
socket.send_json(request_dmg)

# Get the reply
response = socket.recv_json()

# Print response
print("Received response from server:")
print(response)
