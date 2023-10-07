import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
import pickle

dftrain = pd.read_csv("titanic/train.csv")
dftrain.columns = [col.lower() for col in dftrain.columns]
cols_ind_vars = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "cabin",
    "embarked",
]  # independent variables.
col_ids = ["passengerid", "name"]  # ignore from model but keep in data
col_ignore = ["cabin", "ticket"]  # ignore from model and data.

col_numeric = ["age", "sibsp", "fare", "parch"]  # numeric variables.
col_categorical = ["pclass", "sex", "embarked"]  # categorical variables.


def prepare_data(data):
    df = data.copy()
    df.columns = [col.lower() for col in df.columns]
    df.drop(columns=col_ids, inplace=True)
    df.drop(columns=col_ignore, inplace=True, errors="ignore")
    df = df.ffill(axis=1).bfill(axis=1)
    df_dict = df.to_dict(orient="records")
    return df_dict


dftrain_dict = prepare_data(dftrain)

dv = DictVectorizer(sparse=False)
xtrain = dv.fit_transform(dftrain_dict)
ytrain = dftrain.survived.values


model = RandomForestClassifier(n_estimators=25)
model.fit(xtrain, ytrain.astype(str))

with open("saved_model.pkl", "wb") as fout:
    pickle.dump((model, dv), fout)

prediction = model.predict_proba(xtrain)[:,1]
print(prediction)
