Python Task 4 - Basic Weather App
OASIS INFOBYTE Python Programming Internship

This project is a basic weather application developed using Python. It fetches real-time weather information for a user-specified city or ZIP code using the OpenWeatherMap API.

#Objective
The objective of this project is to build a Python application that fetches and displays weather information for a specified location.

#Features
- Accepts a city name or ZIP code from the user.
- Fetches weather information using the OpenWeatherMap API.
- Displays temperature in Celsius (°C).
- Displays temperature in Fahrenheit (°F).
- Displays humidity percentage.
- Displays the current weather condition.
- Displays wind speed.
- Handles invalid API keys.
- Handles city or ZIP code not found errors.
- Handles network and connection errors.
- Validates empty user input.

# Technologies Used
- Python
- Requests library
- OpenWeatherMap API
- Google Colab

# How to Run
# 1. Install the required library

Run the following command:
```python
!pip install requests
```

# 2. Run the program
Enter your OpenWeatherMap API key when requested.
Then enter a city name or ZIP code.
Example:

```text
Enter your OpenWeatherMap API key: YOUR_API_KEY
Enter city name or ZIP code: Coimbatore
```

### 3. Example Output
```text
======================================
          WEATHER INFORMATION
======================================
Location       : Coimbatore, IN
Temperature    : 28.50 °C
Temperature    : 83.30 °F
Humidity       : 72%
Condition      : Partly Cloudy
Wind Speed     : 3.10 m/s
======================================
```
*The values shown above are example values and may differ from the actual weather.*

# Error Handling
The application handles:

- Empty city or ZIP code
- Invalid API key
- City or ZIP code not found
- Network connection errors
- Request timeout
- Invalid weather data

#Project Structure
```text
Python-Task4-BasicWeatherApp/
│
├── weather_app.py
└── README.md
```

#API
This project uses the OpenWeatherMap API to retrieve weather information.

## Internship Task
OASIS INFOBYTE - Python Programming
Task 4: Basic Weather App
Level: Beginner
