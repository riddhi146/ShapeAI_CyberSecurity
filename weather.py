import requests
from datetime import datetime

api_key = '1d99225db3d9b87db95a804b6f7fdc21'
city_name = input("Enter the name of the city: \n")

comp_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid='+api_key
api_link = requests.get(comp_api_link)
api_data = api_link.json()

temp_city = ((api_data["main"]["temp"]) - 273.15)
weather_desc = api_data["weather"][0]["description"]
hmdt = api_data["main"]["humidity"]
wind_spd = api_data["wind"]["speed"]
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print('Weather Stats for - {} || {}'.format(city_name.upper(), date_time))

print('Current temperature is: {:.2f} deg C'.format(temp_city))
print('Current weather desc :', weather_desc)
print('Current Humidity: ',hmdt, '%')
print('Current wind speed: ',wind_spd,'kmph')

print("====================================================")


txtlist = [temp_city,weather_desc,hmdt,wind_spd,date_time]

with open("textfile.txt" , mode= 'w' ,encoding= 'cp1252') as f :
                                     
    f.write("------------------------------------------------------------- \n ")
    f.write("Weather Stats for - {}  || {}".format(city_name.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))

    f.write("{},{} \n".format("Current weather desc: " ,txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity: ",txtlist[2],"%"))
    f.write("{},{},{} \n".format("Current wind speed :",txtlist[3],"kmph"))
    f.write("====================================================")


    f.close
