import streamlit as st
import joblib
import numpy as np
import os

# Load model from current directory (src/)
model_path = os.path.join(os.path.dirname(__file__), "xgb_model.pkl")
model = joblib.load(model_path)

# Streamlit app UI
st.set_page_config(page_title="IPL Win Predictor", layout="centered")
st.title("🏏 IPL Win Predictor")
st.markdown("Simulate a second-innings chase and get real-time win probability predictions.")

# Inputs
target = st.number_input("🎯 Target Score", min_value=1, value=180)
current_score = st.number_input("🏏 Current Score", min_value=0, max_value=target, value=90)
balls_left = st.slider("🔥 Balls Left", 0, 120, 60)
wickets_left = st.slider("💀 Wickets Left", 0, 10, 6)

# Features
runs_needed = target - current_score
balls_done = 120 - balls_left
current_run_rate = (current_score * 6) / balls_done if balls_done > 0 else 0
required_run_rate = (runs_needed * 6) / balls_left if balls_left > 0 else 0

features = np.array([[balls_left, wickets_left, runs_needed, current_run_rate, required_run_rate]])

# Predict
if st.button("Predict Win Probability"):
    win_prob = model.predict_proba(features)[0][1] * 100
    lose_prob = 100 - win_prob

    st.subheader("📊 Prediction")
    st.markdown(f"**Batting Team Win Probability:** `{win_prob:.2f}%`")
    st.markdown(f"**Bowling Team Win Probability:** `{lose_prob:.2f}%`")

    st.progress(int(win_prob))

    st.caption("Powered by XGBoost · Real-time prediction")
