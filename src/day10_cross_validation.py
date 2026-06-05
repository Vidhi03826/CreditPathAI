import pandas as pd

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

features = [

    "Principal",
    "terms",
    "age",
    "education_encoded",
    "gender_encoded"
]

X = df[features]

y = df["loan_status"]
encoder = LabelEncoder()

y = encoder.fit_transform(y)

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score

tree = DecisionTreeClassifier(
    random_state=42
)

scores = cross_val_score(

    tree,

    X,

    y,

    cv=5
)

print(scores)

print(
    "\nAverage Score:"
)

print(
    scores.mean()
)