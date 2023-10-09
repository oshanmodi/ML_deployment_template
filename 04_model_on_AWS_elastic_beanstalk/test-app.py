import requests


passenger1 = {
    "pclass": 3,
    "sex": "male",
    "age": 34.5,
    "sibSp": 0,
    "parch": 2,
    "fare": 7.8292,
    "cabin": "no",
    "embarked": "S",
}




passenger2 = {
    "passengerId": 2,
    "survived": 1,
    "pclass": 1,
    "name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
    "sex": "female",
    "age": 38.0,
    "sibSp": 1,
    "parch": 0,
    "ticket": "PC 17599",
    "fare": 71.2833,
    "cabin": "C85",
    "embarked": "C",
}


# passenger = dftest.iloc[0].to_dict()
host = 'titanic-disaster-serving-env.eba-6vcdipdp.ap-south-1.elasticbeanstalk.com'
url = f"http://{host}/predict"

# print( requests.get(url) )




response = requests.post(url, json=passenger1)
print(response.json())



response = requests.post(url, json=passenger2)
print(response.json())


