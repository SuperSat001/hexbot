import requests  # install if necessary -> pip install requests

URL = 'https://api.noopschallenge.com' + '/hexbot'  # change the last part to query different machines

r = requests.get(URL)

result = r.json()
print(result['colors'][0]['value'])  # prints the hex code, e.g. #7A5A28

# Additional parameters
# Hexbot supports: count, width, height, seed

params = {'count': 5, 'width': 1000, 'height': 1000}
r = requests.get(URL)  # the requests module will handle the parameter encoding
result = r.json()
print(result)  # prints a list of hexcodes
