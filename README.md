# 🏏 IPL Win Predictor

A machine learning-powered Streamlit app that predicts the win probability of a team during the second innings of an IPL match in real-time. It uses match context such as score, wickets, and balls left to predict win probability using a trained XGBoost classifier.

---

## ✨ Features

* 🔮 Real-time win probability prediction
* 🎛️ Interactive sliders for match simulation
* 🧼 Clean and minimal UI with Streamlit
* 📊 Trained on historical IPL delivery-level data

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/akash-1033/ipl-win-predictor.git
cd ipl-win-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run src/app.py
```

This will open the app in your default browser at:
🌐 **[http://localhost:8501](http://localhost:8501)**

---

## 🖼️ Preview

![Screenshot 2025-06-26 165535](https://github.com/user-attachments/assets/23c18e4e-89b4-41b0-9032-842076de2cba)


## 🛠️ How It Works

### 📥 Inputs

* Current score
* Wickets remaining
* Balls left
* Target score

### 🧮 Features Engineered

* `balls_left`
* `wickets_left`
* `runs_needed`
* `current_run_rate`
* `required_run_rate`

These features are passed into a trained **XGBoost classifier**, which outputs the **win probability of the batting team**.

---

## 🧱 Tech Stack

* 🐍 Python
* 🌐 Streamlit
* 📊 Pandas, NumPy
* 🚀 XGBoost, Scikit-learn
* 🧰 Joblib

---

## 🧪 How I Built It

* 🧹 Cleaned IPL delivery-level dataset (150,000+ rows)
* 🛠️ Engineered key match context features
* 🧠 Trained and evaluated a robust XGBoost classifier
* 📈 Used ROC-AUC, Brier score, confusion matrix for model validation
* 💻 Built an interactive Streamlit dashboard for real-time prediction
* 💾 Integrated model into app via joblib

---

## 🔮 Future Plans

* 🏟️ Add full match simulation
* 📉 Visualize ball-by-ball probability progression
* 🧬 Add venue, bowler, batsman context

---

## 🙌 Acknowledgements

* [Kaggle IPL Dataset](https://www.kaggle.com/datasets)
* [XGBoost Documentation](https://xgboost.readthedocs.io/)
* [Streamlit Documentation](https://docs.streamlit.io/)

---

Made with ❤️ by **Akash**
