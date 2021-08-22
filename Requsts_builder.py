import requests
import json

# This is an example of creating a request with mashivisor Real Estate API

# HTTP requests just work like opening a webpage, think about what data a webpage displays when it loads, you're just taking that data when you do requests

# Define data you want to send in a request as variables
address = '70 Pine St'
city = 'New York'
state = 'NY'
zipcode = '10005'

# These variables will likely be linked to your account or specific endpoint and are used to authenticate requests
api_key = 'Enter Your API Key Here'
mash_id = 'Enter your Mashivisor ID here'

# Construct your request, so build out the URL you need for the request, remember to use variables here so its easier to run scripts etc.
url_mash_prop = f'https://api.mashvisor.com/v1.1/client/property?id{mash_id}&state={state}&address={address}&city={city}&zip_code={zipcode}'

# Your headers should reference any authentication information
headers_mash = {'x-api-key' : api_key}

# Functions to send the request to your provider, this returns a JSON as a string. This is probably a good idea to use a JSON most of the time
def get_cl(url, headers):
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    return json_data

mashivor_data = get_cl(url_mash_prop, headers_mash)

#Simple query in the JSON to get specific information
long_term = mashivor_data['content']['ROI']['traditional_rental']
short_term = mashivor_data['content']['ROI']['airbnb_rental']
cap_rate = mashivor_data['content']['ROI']['traditional_cap_rate']