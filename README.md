# 🎓 Student Performance Prediction App

A Machine Learning web application that predicts student final marks based on study habits and academic factors.
The app is deployed using **Streamlit** and includes interactive visualizations.

---

## 🚀 Project Overview

This project uses multiple machine learning algorithms to predict student performance.
It compares models and selects the best-performing one automatically.

Users can input student details and instantly see:

* 📊 Predicted marks
* 🏆 Grade classification
* 📈 Model accuracy
* 📉 Interactive graphs

---

## 🧠 Machine Learning Models Used

* Linear Regression
* Decision Tree
* Random Forest

The model with the highest **R² score** is automatically selected for prediction.

---

## 📊 Features

✔ Predict student marks
✔ Automatic model comparison
✔ Grade classification
✔ Interactive charts (Bar, Line, Pie)
✔ Clean and responsive UI
✔ Deployable via Streamlit

---

## 📁 Project Structure

```
Student-Marks-Prediction/
│
├── app.py                # Streamlit UI
├── model.py              # ML model training & prediction
├── student_marks.csv     # Dataset
├── best_model.pkl        # Saved trained model
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib

---

## ▶️ How to Run Locally

1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/Student-Marks-Prediction.git
cd Student-Marks-Prediction
```

2️⃣ Install dependencies

```
pip install -r requirements.txt
```

3️⃣ Run the app

```
py -m streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Cloud**.

Once deployed, the app will be available at:

```
https://your-app-name.streamlit.app
```

---

## 📈 Output

The app provides:

* Predicted marks
* Grade category
* Model accuracy
* Input visualizations

---

## 🎯 Future Improvements

* Add more features (behavior, attendance trends)
* Use advanced models (XGBoost, Neural Networks)
* Add login system
* Export prediction report
* Database integration

---

## 👨‍💻 Author

Your Name
BTech CSE (AIML)

---

## 📜 License

This project is for educational purposes only.
