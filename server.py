import zmq
import json


# Environment and socket initialization
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

while True:
    # Receive message
    message = socket.recv_string()
    try:
        request = json.loads(message)
    except json.JSONDecodeError:
        socket.send_json({"error": "Invalid JSON"})
        continue

    # Unpack message
    service_key = request.get("service_key")
    data = request.get("data", {})
    response = {}   # Setup response

    # Route request
    if not service_key:
        response = {"error": "Missing service_key"}
    elif service_key == "arithmetic":
        pass   # call arithmetic.py function
    elif service_key == "battle_logic":
        pass    # call battle_logic.py function
    elif service_key == "unit_conversion":
        pass    # call unit_conversion.py function
    else:
        response = {"error": f"Unknown service_key: {service_key}"}

    socket.send_json(response)

context.destroy()
