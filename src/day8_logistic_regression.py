import pandas as pd

from sklearn.model_selection import train_test_split

df = pd.read_csv(
    "data/features/feature_engineered_data.csv"
)

print("Dataset Loaded Successfully")

features = [

    "Principal",
    "terms",
    "age",
    "loan_month",
    "education_encoded",
    "gender_encoded"
]

X = df[features]

y = df["loan_status"]

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)

print(y[:10])

X_train, X_test, y_train, y_test = (

    train_test_split(

        X,
        y,

        test_size=0.2,

        random_state=42
    )
)

print(X_train.shape)

print(X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

print(
    "\nModel Training Completed!"
)

predictions = model.predict(
    X_test
)

print(
    "\nPredictions:"
)

print(predictions[:10])

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(
    y_test,
    predictions
)

print(
    "\nAccuracy:"
)

print(accuracy)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(
    y_test,
    predictions
)

print(
    "\nConfusion Matrix:"
)

print(cm)

from sklearn.metrics import classification_report

print(
    "\nClassification Report"
)

print(
    classification_report(
        y_test,
        predictions
    )
)