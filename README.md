# Reports and Arithmetic Microservice 
### A Python-based microservice with multiple services:
`battle_logic`: Calculates total damage given an attack, defense, and optional crit value  
`convert_volume`:  Converts a volume measurement from one unit to another  
`convert_weight`:  Converts a weight measurement from one unit to another  
`convert_temperature`: Converts a temperature measurement from one unit to another  
    
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
```
### Response Format
The response is formatted as follows:
```python
response = {"damage": 7.5}
```

### Receiving the Response
```python
response = socket.recv_json()
print("Received response from server:")
print(response)
```

## Using the `convert_volume`, `convert_weight`, and `convert_temperature` Services
Available unit conversions:
- `convert_volume`:
    -  teaspoon
    -  tablespoon
    -  fluid_ounce
    -  cup
    -  spint
    -  quart
    -  gallon
    -  mililiters
- `convert_weight`:
    -  ounce
    -  pound
    -  grams
- `convert_temperature`:
    -  Farenheit
    -  Celsius

### REQUEST Unit Conversion Services
To use these services, you need to send a JSON formatted message to the server, which includes:
1. `service_key`: identfies which service you want to use. For this service, choose any of the available unit conversion services listed above  
2. `data`: a dictionary of parameters for the unit conversion service.

### `data` parameter mappings
The parameters you include in data can vary depending on the unit conversion service.  The necessary parameters and example formats are listed below.  
1.  `convert_volume`:
    -  `amount` (number):  volume amount  
    -  `unit` (string, default=None):  measurement unit you want to convert to
    -  `to_metric` (bool, default=True): True if converting from imperial to metric, otherwise False
2.  `convert_weight`:
    -  `amount` (number):  volume amount  
    -  `unit` (string, default=None):  measurement unit you want to convert to  
    -  `to_metric` (bool, default=True): True if converting from imperial to metric, otherwise False  
3.  `convert_temperature`:  
    -  `value` (number):  temperature value
    -  `direction` (string, default="F_to_C"):  "F_to_C" if converting from Farenheit to Celsius.  "C_to_F" if converting from Celsius to Farenheit.

  ### JSON Format examples
`convert_volume`:  

  
`convert_weight`:  

  
`convert_temperature`:   



## UML Diagram


## Communication Contract
1. We will communicate via Teams and respond to any chat messages within 48 hours. This excludes Tuesday and Wednesdays. Aside from these two days, if no response within 24 hours, team members can make assumptions as needed but make sure to communicate their actions in a follow-up email.
2. All group assignments should be completed at least one day prior to the official due date. This will allow the team one additional day to review the assignment/project details, and ensure that there is not a quick rush to complete work right before the deadline.
3. If any one encounters delays or needs extra time they notify the team as soon as possible, so we can adjust our plans accordingly.
4. When collaborating on another team member’s project, clearly communicate your current skill level and availability before committing to tasks. Likewise, project owners should define micro-service requests that are reasonable in scope and align with what others can realistically complete within the timeline.
5. All team members will use GitHub for any collaborative version control and project management.
