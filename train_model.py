import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# DADOS PARA TREINAR O MOTOR

corrente = [120.77, 158.05, 160.52, 161.22, 159.25, 162.5, 152.48]
temperatura = [99.77, 61.05, 78.2, 58.02, 55.25, 66.08, 71.4]
vibracao = [1.15, 2.43, 1.58, 2.32, 1.29, 2.32, 1.34]
resultado = [1, 0, 0, 0, 0, 0, 0]

# CRIANDO O FRAME PARA TREINO
data = pd.DataFrame({
    'corrente': corrente,
    'temperatura': temperatura,
    'vibracao': vibracao
})

# DEFININDO RESULTADO
target = np.array(resultado)

# MODELO ESCOLHIDO
model = RandomForestClassifier()

# TREINANDO O MODELO
model.fit(data, target)

# SALVANDO O MODELO TREINADO 
joblib.dump(model, 'A5000.pkl')
