# Reports and Arithmetic Microservice 
### A Python-based microservice with multiple services:
    battle_logic: Calculates total damage given an attack, defense, and optional crit value  
    convert_volume:  
    convert_weight:  
    convert_temperature:
    
## Using the `battle_logic` service  
### REQUEST battle_logic Format  
To use the battle_logic service, you need to send a JSON-formatted messsage to the server, which includes:  
1. `service_key` - identifies which service to use.  For this service, use "battle_logic"
2. `data` - a dictionary of the parameters for the calculation:
    - `attack` (number): Attacker damage value
    - `defense` (number): Enemy defense value
    - `crit` (number, optional): Attacker crit multiplyer, default 1

### Example format
```python
message = {
    "service_key": "battle_logic"
    "data": {
        "attack": 10,
        "defense": 5,
        "crit": 1.5
    }
}
```
### Sending the Request (Local Server)
```python
import zmq


# Connect to server
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5556")

# Send the request
socket.send_json(message)

# Receive the response
response = socket.recv_json()
print("Received response from server:")
print(response)
```

## Using the `Kitchen Converter services`
### REQUEST Kitchen Converter Service


### RECEIVE


## UML Diagram


## Communication Contract
1. We will communicate via Teams and respond to any chat messages within 48 hours. This excludes Tuesday and Wednesdays. Aside from these two days, if no response within 24 hours, team members can make assumptions as needed but make sure to communicate their actions in a follow-up email.
2. All group assignments should be completed at least one day prior to the official due date. This will allow the team one additional day to review the assignment/project details, and ensure that there is not a quick rush to complete work right before the deadline.
3. If any one encounters delays or needs extra time they notify the team as soon as possible, so we can adjust our plans accordingly.
4. When collaborating on another team member’s project, clearly communicate your current skill level and availability before committing to tasks. Likewise, project owners should define micro-service requests that are reasonable in scope and align with what others can realistically complete within the timeline.
5. All team members will use GitHub for any collaborative version control and project management.
