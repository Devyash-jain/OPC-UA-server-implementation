# Simple OPC UA Server in Python

This project is a basic OPC UA (Open Platform Communications Unified Architecture) server implemented using the `opcua` Python library. It simulates a temperature sensor by exposing a single variable `Temperature` under a device node `MyDevice`. The temperature value increments every second, simulating real-time sensor data.

## 🔧 Requirements

- Python 3.6+
- `opcua` library

Install dependencies using pip:

```bash
pip install opcua
```

# Running the Server
Run the server script:
python server.py

You will see output like:
OPC UA Server started at opc.tcp://0.0.0.0:4840/freeopcua/server/
Temperature: 20.1
Temperature: 20.2
...

The server will continue to run, incrementing the Temperature variable every second. Press Ctrl+C to stop.

# Server Details
* Endpoint: opc.tcp://0.0.0.0:4840/freeopcua/server/
* Namespace URI: http://example.com
* Device Node: MyDevice
* Variable: Temperature (writable, Double)

#  Features
* Simple and easy-to-understand structure
* Simulates a real-time changing variable
* Clean shutdown on Ctrl+C

# Project Structure
```
├── automation.py        # Main OPC UA server script
└── README.md            # Project documentation
```

# Future Improvements
* Add more simulated sensor variables (e.g., Humidity, Pressure)
* Include timestamp metadata with variable values
* Implement authentication and encryption (for production use)
* Enable historical data logging
