import streamlit as st
from skops.io import load
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt

# Load the skops model
model_path = 'models/xgb_clf_best_model-20240825_1532.skops'
model = load(model_path, trusted=['xgboost.core.Booster', 'xgboost.sklearn.XGBClassifier'])

# Streamlit app
st.title("Customer Satisfaction Prediction and Interpretation")

# Take 2 variables from the customer
X1 = st.slider("Order delivered on time (1 to 5 scale)", 1, 5, 3)
X3 = st.slider("Ordered everything wanted (1 to 5 scale)", 1, 5, 3)

# Create interaction features
poly = PolynomialFeatures(3, interaction_only=False, include_bias=False)
X_interactions = poly.fit_transform(np.array([[X1, X3]]))

# Predict the customer satisfaction using the loaded model
predictions = model.predict(X_interactions)
y_proba = model.predict_proba(X_interactions)

# Variable and interaction names
feature_names = ['X1: Order delivered on time', 'X3: Ordered everything wanted']
interaction_names = poly.get_feature_names_out(input_features=feature_names)

# Create a DataFrame to show the interaction terms with their corresponding values
interaction_df = pd.DataFrame(data=X_interactions, columns=interaction_names)

# Display the interaction terms and their meanings
st.subheader("Generated Interaction Features and Their Meanings:")
st.write(interaction_df)

# Print the predictions
st.subheader("Predicted Customer Satisfaction:")
st.write(f"Class: {predictions[0]}, Probability: {y_proba[0][predictions[0]]:.2f}")

# Explain the reasoning behind the model's output
st.subheader("Model Interpretation:")
st.write("""
The model predicts customer satisfaction based on the following factors:
1. **X1: Order delivered on time**: Reflects how timely the order was delivered, on a scale from 1 to 5.
2. **X3: Ordered everything wanted**: Reflects whether the customer received everything they ordered, on a scale from 1 to 5.

The model also considers interactions between these variables, such as:
- **X1 * X3**: The interaction between timely delivery and completeness of the order.
- **X1^2**: The quadratic effect of timely delivery.
- **X3^2**: The quadratic effect of receiving everything ordered.
- **X1^2 * X3**: The interaction of the quadratic effect of timely delivery with receiving everything ordered.
- **X1 * X3^2**: The interaction of timely delivery with the quadratic effect of receiving everything ordered.

These interactions allow the model to capture more complex relationships between the variables and better predict customer satisfaction.
""")

# Feature importance using SHAP
st.subheader("Feature Importance and SHAP Explanation:")
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_interactions)

# SHAP summary plot
st.write("SHAP Summary Plot:")
fig, ax = plt.subplots()
shap.summary_plot(shap_values, features=X_interactions, feature_names=interaction_names, plot_type="bar", show=False)
st.pyplot(fig)

# SHAP force plot for the individual prediction
st.write("SHAP Force Plot for the Prediction:")
fig, ax = plt.subplots()
shap.force_plot(explainer.expected_value, shap_values[0], interaction_df, matplotlib=True)
st.pyplot(fig)

# Option to download report
st.subheader("Downloadable Report:")
st.write("You can download a report summarizing the inputs, predictions, and SHAP explanations for further analysis and sharing.")
# Here you can add functionality to generate and download a report (e.g., using `pdfkit` or `weasyprint`)

# Historical Comparison Placeholder
# st.subheader("Historical Comparison:")
# Here, you could compare the current prediction to historical data if available.