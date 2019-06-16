import requests
import winsound

print("-------------------------------")
print("This code will show you how the random colors sound like.")

response = requests.get("http://api.noopschallenge.com/hexbot")
for i in range(25):

    color = response.json()['colors'][0]['value']
    color = color.replace("#", "")

    print(color + " >")

    frequency = int(color, 16) // 1000  
    duration = 500 
    winsound.Beep(frequency, duration)
    response = requests.get("http://api.noopschallenge.com/hexbot")
