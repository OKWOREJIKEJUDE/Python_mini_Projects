import json
import requests

url = "http://official-joke-api.appspot.com/random_ten"
response = requests.get(url)
print(response.status_code)
jsonData = json.loads(response.text)
print(jsonData)

 #this is our class
class Jokes:
    #this is our constructor
    def __init__(self, mySetup, myPunchline, myType, myId) -> None:
        self.setup = mySetup
        self.punchline = myPunchline
        self.type = myType
        self.id = myId

    def __str__(self) ->str:
        return f"mySetup == {self.setup}|| myPunchline == {self.punchline}|| myType == {self.type}|| myId == {self.id} "

jokes = []
for j in jsonData:
    mySetup = j["setup"]
    myPunchline = j["punchline"]
    myType= j["type"]
    myId= j["id"]
    joke = Jokes(mySetup, myPunchline, myType, myId)
    jokes.append(joke)
print(len(jokes))

for jokesss in jokes:
    print()
    print(jokesss)
