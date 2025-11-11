# Exemplo simplificado
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dados fictícios de tráfego
dados = pd.DataFrame({
    "latencia": [10, 30, 100, 20, 150],
    "pacotes_perdidos": [0, 1, 5, 0, 10],
    "carga": ["baixa", "media", "alta", "baixa", "muito alta"]
})

# Treinar modelo para prever congestionamento
modelo = RandomForestClassifier()
modelo.fit(dados[["latencia", "pacotes_perdidos"]], dados["carga"])

# Predição
print(modelo.predict([[60, 3]]))  # IA diz que há risco de 'alta' carga

print("Modelo treinado e predição realizada com sucesso.")
