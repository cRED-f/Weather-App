import requests
import json

def weather():
        city_name=input("Enter the name of city:")
        url=f"http://api.weatherapi.com/v1/current.json?key=e3aa3146c4ec46cba58180117232503&q={city_name}"
        x=requests.get(url)

        dic=json.loads(x.text)


        print("Location:",dic["location"]["name"])
        print("Country:",dic["location"]["country"])
        print("Temperature:",dic["current"]["temp_c"],"c , ",dic["current"]["temp_f"],"f")
        print("Humidity:",dic["current"]["humidity"])
        print("Cloud",dic["current"]["cloud"])
        y=input("Want to know another location weather?\ntype: yes or no! ")
        if y=='yes':
          weather()
        else:
          print("see you later!")

weather()