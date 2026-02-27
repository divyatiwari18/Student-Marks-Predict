import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def train_models():

    df = pd.read_csv("student_marks.csv")

    X = df[['Study_Hours', 'Attendance', 'Previous_Marks', 'Assignments_Avg']]
    y = df['Final_Marks']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor()
    }

    scores = {}
    trained_models = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        scores[name] = r2_score(y_test, preds)
        trained_models[name] = model

    best_model_name = max(scores, key=scores.get)
    best_model = trained_models[best_model_name]

    return best_model, scores, best_model_name