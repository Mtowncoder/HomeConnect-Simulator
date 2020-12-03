import requests
import json


url = "https://simulator.home-connect.com/api/homeappliances"
url_setting = 'https://simulator.home-connect.com/api/homeappliances/HAID/settings'
url_freezer_setting = 'https://simulator.home-connect.com/api/homeappliances/HAID/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureFreezer'
url_fridge_setting =  'https://simulator.home-connect.com/api/homeappliances/HAID/settings/Refrigeration.FridgeFreezer.Setting.SetpointTemperatureRefrigerator'

# go to home connect simulator run get all HAID's and the authorization key will be in the header(-H) of the GET function
auth_key = ''  

headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'authorization': auth_key }
setting_headers = { 'accept': 'application/vnd.bsh.sdk.v1+json', 'Accept-Language' : 'en-US', 'authorization': auth_key }



resp = requests.get(url,headers=headers) #### This is how you can get all your available HAID's for simulation
resp_setting =  requests.get(url_setting,headers=setting_headers)
resp_freezer_setting = requests.get(url_freezer_setting, headers = setting_headers)
resp_fridge_setting = requests.get(url_fridge_setting, headers = setting_headers)

x = resp_setting.content
freezer = json.loads(resp_freezer_setting.content)
fridge = json.loads(resp_fridge_setting.content)


# Do you want all settings?
y = json.loads(x)
#print(y)
#print(y['data']['settings'])


nice = y['data']['settings']
# Which setting do you want?
# you can use list.append(x) and say x = input(Appliance ID) to add new Applainces
# increase/decrease freezer setting
freezer_min = int(freezer['data']['constraints']['min']) # get min value from json data
freezer_max = int(freezer['data']['constraints']['max']) # get max value from json data

fridge_min = int(fridge['data']['constraints']['min']) # get min value from json data
fridge_max = int(fridge['data']['constraints']['max']) # get max value from json data

#print(freezer)
current_freezer_temp = freezer['data']['value'] # gets the current freezer temperature
current_fridge_temp = fridge['data']['value'] # gets the current fridge temperature

def change_freezer_temp():
    print("The current temperature is {} °C".format(current_freezer_temp))
    ans1 = input('Would you like to change the temperature? ')

    if ans1.lower() == 'yes':
        # set bounds of min and max
        value = int(input('What would you like to set the temperature to? '))
        while value < freezer_min or value > freezer_max:
            print('The bounds are {} and {} try again'.format(freezer_min, freezer_max))
            value = int(input('What would you like to set the temperature to? '))
        print('Changing temperature to {} °C '.format(value))
    else:
        print("Okay, Thank you")
        
def change_fridge_temp():
    print("The current temperature is {} °C".format(current_fridge_temp))
    ans1 = input('Would you like to change the temperature? ')

    if ans1.lower() == 'yes':
        # set bounds of min and max
        value = int(input('What would you like to set the temperature to? '))
        while value < fridge_min or value > fridge_max:
            print('The bounds are {} and {} try again'.format(fridge_min, fridge_max))
            value = int(input('What would you like to set the temperature to? '))
        print('Changing temperature to {} °C '.format(value))
    else:
        print("Okay, Thank you")
