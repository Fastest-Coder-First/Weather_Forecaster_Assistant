# Weather_Forecaster_Assistant
Weather forecaster assistant Weather One is a personal AI assistant who can tell information about the temperature of any city worldwide.

## Usage

1. Clone the repository using the command below
   * $ git clone https://github.com/Fastest-Coder-First/Weather_Forecaster_Assistant.git

2. Sign Up on OpenWeatherMap to generate an API key
    * api_key = "Your API key"
    * base_url = "Base URL of OpenWeatherMap"

3. Run the Assistant using the command below in the command line tool
    * python weather_forecast.py


## Weather Information
Weather One can tell the temperature of any city worldwide using OpenWeatherMap API.
It includes:
* The current temperature of the city
* The humidity in percentage
* The current  maximum temperature of the city
* The current minimum temperature of the city
* The description of the temperature

## Requirements
The required modules and library of the code can be found requirement.txt file.

## Architecture 
The architecture of the Weather Forecasting Tool follows a simple flow:
    
I. Command Line Interface (CLI): The user interacts with the tool through the command line by providing the city name and optional flags for imperial units.
    
II. Command Line Argument Parsing: The ppytext module is used to take commands from the user in the command line arguments provided by the user, including the city name.
    
III. API Request Building: The build_weather_query function constructs the URL for an API request to the OpenWeatherMap Weather API. It utilizes the provided city name and imperial unit flag to create the query URL.

IV. API Request Execution: The get_weather_data function makes an HTTP request to the OpenWeatherMap API using the constructed URL. It handles potential errors, such as unauthorized access or not found responses.

V. API Response Parsing: The received data from the API response is parsed using the json module to extract the relevant weather information. The parsed data is returned as a Python object using the str() function.

VI. Weather Information Display: The weather() function takes the parsed weather data and displays the formatted weather information on the command line. It includes the city name, weather symbol, weather description, and temperature in the desired unit.

![Forecast Architecture](forecast_architecture2.png)

## GitHub Copilot Usage

 GitHub Copilot can assist in various scenarios throughout the codebase::

+ API Request URL Building: Copilot can provide suggestions for constructing the API request URL based on the city name and imperial unit flag, ensuring the correct formatting of the URL parameters.

+ Configuration File Parsing: Copilot can assist in file handling and parsing the configuration file (secrets.ini) to retrieve the API key, suggesting code snippets for reading and extracting the key from the file.
        
+ Error Handling and Exception Handling: Copilot can provide suggestions for error handling and exception handling in the get_weather_data function, helping to handle different HTTP error codes and displaying appropriate error messages to the user.
        
+ Weather Information Formatting: Copilot can suggest improvements in formatting and displaying the weather information, such as aligning the output and improving the visual representation of weather symbols and descriptions.
 
+ Variable Naming and Code Organization: Copilot can provide suggestions for variable naming and code organization, helping to improve the readability and maintainability of the codebase.
      
Please note that while GitHub Copilot can provide helpful suggestions, it's important to review and validate the generated code to ensure correctness and adherence to specific requirements.

# Images/Videos of Working Solution
Included relevant image showcasing working solution. This includes screenshots output.png  of the assistant in action. Also, the working of the tool can be found in the video weather.mp4 which demonstrates the working of the assistant.

