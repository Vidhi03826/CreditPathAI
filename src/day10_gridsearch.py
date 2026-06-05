import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import GridSearchCV

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

param_grid = {

    "max_depth":[
        3,
        5,
        7,
        10
    ],

    "min_samples_split":[
        2,
        5,
        10
    ]
}

grid = GridSearchCV(

    DecisionTreeClassifier(
        random_state=42
    ),

    param_grid,

    cv=5
)

grid.fit(
    X,
    y
)

print(
    "Best Parameters:"
)

print(
    grid.best_params_
)

print(
    "\nBest Score:"
)

print(
    grid.best_score_
)