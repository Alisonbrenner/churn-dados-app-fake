import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime

# Inicializar Faker
fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Número de clientes fictícios
n_clientes = 1000

# Gerar dados
dados = []

for i in range(n_clientes):
    id_cliente = i + 1
    data_cadastro = fake.date_between(start_date='-2y', end_date='-30d')
    
    tempo_uso = (datetime.today().date() - data_cadastro).days
    qtde_pedidos = np.random.poisson(lam=5)  # Média de 5 pedidos
    valor_medio = round(np.random.normal(loc=80, scale=30), 2)
    valor_medio = max(valor_medio, 10.0)  # evitar valores negativos

    uso_cupom = np.random.choice([0, 1], p=[0.6, 0.4])  # 40% usaram cupom
    usou_app_ultimo_mes = np.random.choice(['não usou', 'usou'], p=[0.3, 0.7])  # 70% ativos
    
    # Lógica de churn: mais chance de cancelar se pouco ativo
    if usou_app_ultimo_mes == 0 and qtde_pedidos < 3:
        cancelou = np.random.choice([0, 1], p=[0.3, 0.7])
    else:
        cancelou = np.random.choice([0, 1], p=[0.9, 0.1])
    
    dados.append([
        id_cliente,
        data_cadastro,
        tempo_uso,
        qtde_pedidos,
        valor_medio,
        uso_cupom,
        usou_app_ultimo_mes,
        cancelou
    ])

# Criar DataFrame
df = pd.DataFrame(dados, columns=[
    'id_cliente', 'data_cadastro', 'tempo_uso', 'qtde_pedidos',
    'valor_medio', 'uso_cupom', 'usou_app_ultimo_mes', 'cancelou'
])

# Salvar em CSV (opcional)
df.to_csv(r'C:\Users\alyson brenner\Documents\PROJETOS DATA ENGINER\churn-predictor-engdados\data\raw\clientes_ficticios.csv', index=False)

