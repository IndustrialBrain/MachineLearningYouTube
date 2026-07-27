from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd


app = Flask(__name__)

# CARREGANDO O MODELO 
model1 = joblib.load('A5000.pkl')

@app.route('/verificar_motor', methods=['POST'])
def verificar_motor():
    data = request.get_json()
    corrente = data['CORRENTE']
    temperatura = data['TEMPERATURA']
    vibracao = data['VIBRACAO']

    # FAZENDO A PREVISÃO
    prediction = model1.predict(np.array([[corrente, temperatura, vibracao]]))

    return jsonify({'resultado': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)


