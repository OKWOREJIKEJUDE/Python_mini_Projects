import json
import requests
#Text to Speech library
import pyttsx3

url = "http://official-joke-api.appspot.com/random_ten"
response = requests.get(url)
print(response.status_code)
jsonData = json.loads(response.text)
print(jsonData)

 #this is our class
class Jokes:
    #this is our constructor
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) ->str:
        return f"mySetup == {self.setup}|| myPunchline == {self.punchline} "


jokes = []
for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Jokes(setup, punchline)
    jokes.append(joke)
print(len(jokes))

for jokesss in jokes:
    print(jokesss)

    #text to speech of what we fetched online
    print("For Setup") 
    pyttsx3.speak(joke.setup)
    print("For Punchline")
    pyttsx3.speak(joke.punchline)






