
import pandas as pd
import requests
import concurrent.futures

def api_call(city):
    """
    Using API Call to load the weather data into a json format
    """
    
    exception_not_happened = True
    try:
        url='http://api.openweathermap.org/data/2.5/forecast?units=metric&appid=5f1aaab27154e9d7a4c6e81336e9266a&q='

        resurl = url + city

        weather=requests.get(resurl).json()
        
        # Check if we had a failure (the forecast will fail in the same way).
        if weather['cod'] != '200':
            raise Exception(weather['message'])
    except Exception as e:
        exception_not_happened = False
        print ("Error in Argument:",e.args[0])
        
    if exception_not_happened:
        return weather
    
def weathercall(weather):
    
    """ 
    Converting the json data received from the API call to Pandas Dataframe for proper visualization.
    """
    
    if weather:
        ls={}
        for x in range(len(weather.get('list'))):
            ls[weather.get('list')[x].get('dt_txt')]=[weather.get('list')[x].get('main').get('temp'),
                                                      weather.get('list')[x].get('main').get('feels_like'),
                                                      weather.get('list')[x].get('main').get('temp_min'),
                                                      weather.get('list')[x].get('main').get('temp_max'),
                                                      weather.get('list')[x].get('main').get('pressure'),
                                                      weather.get('list')[x].get('main').get('sea_level'),
                                                      weather.get('list')[x].get('main').get('humidity'),
                                                      weather.get('list')[x].get('weather')[0].get('main'),
                                                      weather.get('list')[x].get('weather')[0].get('description'),
                                                      weather.get('list')[x].get('clouds').get('all'),
                                                      weather.get('list')[x].get('wind').get('speed'),
                                                      weather.get('list')[x].get('visibility'),
                                                      weather.get('list')[x].get('rain')]

        col_name=['Temp','Feels_Like','Temp_Min','Temp_Max','Pressure','Sea_Level','Humidity','Weather_Condition',
                      'Description','Cloudiness %','Wind_Speed(meter/sec)','Visibility','Rain(Volume mm/3hr)']
        
        df= pd.DataFrame(ls)
        df_t=df.transpose() 
        df_t.columns=col_name
        df_t.fillna('Not Available',inplace=True)
        return df_t
    
    
def forecast():
    """
    Running two threads one for the main function and 
    other for the API call
    With Proper synchronization
    """
    
    print("Welcome to the Weather Forecasting Platform")
    report=input("Print report to text file :(Y/N)").lower()
    
    if report=='y':
        print("Report will be generated: ")
    elif report=='n':
        print('You have opted for NO... Displaying Weather Forecast on Screen:')
    else:
        print('You have not provided proper parameter(Y/N) so skipping this part:')
    
    city=input("Enter the City Name you want the forecast for: ")
    
    
    #ThreadPoolExecutor uses a pool of threads to execute calls asynchronously.
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(api_call, city)
        weather = future.result()
    result_forecast = weathercall(weather)
    
    if report=='y' and result_forecast.empty==False :
        with pd.ExcelWriter('Forecast_Results.xlsx') as writer:
            result_forecast.to_excel(writer,sheet_name="Weather_Report")
    
    if result_forecast.empty==False:
        print(result_forecast)


