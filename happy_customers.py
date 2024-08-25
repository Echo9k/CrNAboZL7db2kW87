import streamlit as st
from skops.io import load
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd
import lime
from lime.lime_tabular import LimeTabularExplainer

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

# Explain the reasoning behind the model's output using LIME
st.subheader("Model Interpretation with LIME:")

# LIME explainer
explainer = LimeTabularExplainer(
    training_data=X_interactions,
    feature_names=interaction_names,
    class_names=[str(i) for i in model.classes_],
    mode='classification'
)

# Explain the specific instance
exp = explainer.explain_instance(
    data_row=X_interactions[0],
    predict_fn=model.predict_proba
)

# Display the LIME explanation
st.write(exp.as_list())

# Visualize the explanation
fig = exp.as_pyplot_figure()
st.pyplot(fig)

# Option to download report
st.subheader("Downloadable Report:")
st.write("You can download a report summarizing the inputs, predictions, and LIME explanations for further analysis and sharing.")