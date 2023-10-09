import requests


passenger1 = {
    "Pclass": 3,
    "Sex": "male",
    "Age": 34.5,
    "SibSp": 0,
    "Parch": 2,
    "Fare": 7.8292,
    "Cabin": "no",
    "Embarked": "S",
}


passenger2 = {
    "PassengerId": 2,
    "Survived": 1,
    "Pclass": 1,
    "Name": "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
    "Sex": "female",
    "Age": 38.0,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": "PC 17599",
    "Fare": 71.2833,
    "Cabin": "C85",
    "Embarked": "C",
}


# passenger = dftest.iloc[0].to_dict()
url = "http://0.0.0.0:9696/predict"

requests.get(url)


response = requests.post(url, json=passenger1)
print(response.json())


response = requests.post(url, json=passenger2)
print(response.json())

