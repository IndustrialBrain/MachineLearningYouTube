import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Your data
corrente = [25, 35, 24, 26, 45, 28, 38]
velocidade = [50, 75, 78, 85, 87, 95, 100]
vibracao = [0.25, 0.26, 0.28, 0.32, 0.29, 0.32, 0.34]
resultado = [0, 0, 0, 1, 0, 0, 1]

# Creating a DataFrame
data = pd.DataFrame({
    'corrente': corrente,
    'velocidade': velocidade,
    'vibracao': vibracao
})

# Defining the target variable
target = np.array(resultado)

# Random Forest model
model = RandomForestClassifier()

# Training the model
model.fit(data, target)

# Saving the model to a .pkl file using joblib
joblib.dump(model, 'modelo_SaudeMotor.pkl')


