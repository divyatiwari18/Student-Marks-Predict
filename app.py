import streamlit as st
import numpy as np
import pandas as pd

from model import train_models
from utils import get_grade

st.set_page_config(page_title="Student Predictor", layout="wide")

st.title("🎓 Student Performance Prediction")

# Train models
best_model, scores, best_model_name = train_models()

# Model comparison
st.subheader("📊 Model Comparison")
st.write(pd.DataFrame(scores.items(), columns=["Model", "Accuracy"]))

st.success(f"🏆 Best Model: {best_model_name}")

# Sidebar inputs
st.sidebar.header("Enter Student Details")

study = st.sidebar.number_input("Study Hours", 0.0, 24.0, 5.0)
attendance = st.sidebar.number_input("Attendance (%)", 0.0, 100.0, 75.0)
previous = st.sidebar.number_input("Previous Marks", 0.0, 100.0, 70.0)
assignment = st.sidebar.number_input("Assignments Avg", 0.0, 100.0, 80.0)

if st.sidebar.button("Predict"):

    input_data = np.array([[study, attendance, previous, assignment]])
    prediction = best_model.predict(input_data)[0]
    grade = get_grade(prediction)

    st.subheader("📈 Prediction Result")
    st.metric("Predicted Marks", f"{prediction:.2f}")
    st.metric("Grade", grade)

    labels = ['Study Hours', 'Attendance', 'Previous Marks', 'Assignments']
    values = [study, attendance, previous, assignment]

    chart_df = pd.DataFrame({"Category": labels, "Value": values}).set_index("Category")

    st.bar_chart(chart_df)
    st.line_chart(chart_df)

    st.subheader("🥧 Contribution Distribution")
    st.pyplot(chart_df.plot.pie(y="Value", autopct='%1.1f%%').figure)