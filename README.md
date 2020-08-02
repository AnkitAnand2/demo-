# Weather API Call (weather_py)

This is a standard python package 

weather_py is a Python library for forcasting the weather of any reagion .

# API USED:
https://openweathermap.org/forecast5

This API returns the forecasted weather data based on the parameters like "CITY_NAME","LOCATION_ID",etc.

# Installation
## IN Virtual Environment(Recomended):
>conda info -e # To see list of environment

>conda create -n yourenvname python=x.x 

>conda activate yourenvname

>conda install git

>Use the package manager> [pip] install git+https://github.com/AnkitAnand2/weatherpackage2  #to install weather_py

>conda deactivate# To deactivate virtual environment

>conda env remove -n yourenvname #To remove any environment permanently.


## Normal installation:

Use the package manager [pip] install git+https://github.com/AnkitAnand2/weatherpackage2 to install weather_py

## Installation using .rar file:

>python setup.py install



## Usage

```python
from weather_py import weather_py

weather_py.forecast() # returns 'Date with 5 Days Forecasting with every 3 hour interval'

report=input("Print report to text file :(Y/N)").lower()#Prompt to select whether to print the weather report in xlsx file or not 

city=input("Enter the City Name you want the forecast for: ")# Prompt to input city weather to forecast.

```

## requirements.txt file

This contains all the packages used.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


