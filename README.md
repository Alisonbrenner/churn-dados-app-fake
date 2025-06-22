
# 🔍 Churn Predictor - Análise e Previsão de Cancelamento de Clientes

Este projeto tem como objetivo analisar dados fictícios de clientes de um aplicativo e prever a probabilidade de cancelamento (churn) com o auxílio de técnicas de machine learning.

## 📊 Visão Geral

O cancelamento de clientes é um dos maiores desafios para empresas que atuam com aplicativos e serviços digitais. Neste projeto, realizamos uma análise descritiva e preditiva, simulando o comportamento de clientes de um app (inspirado em cases como Nubank, PicPay e iFood).

## ⚙️ Tecnologias Utilizadas

- Python
- Pandas, Seaborn, Matplotlib
- Scikit-learn (Random Forest)
- Streamlit (para dashboard interativo)
- Jupyter Notebook

## 📁 Estrutura do Projeto

churn-predictor-engdados/

 data/processed/churn_dataset.csv

notebooks/churn_analysis.ipynb

dashboards/dashboard.py

models/modelo_treinado.pkl (opcional)


## 📈 Etapas Realizadas

- 🔹 **Exploração e limpeza de dados**
- 🔹 **Análise descritiva com visualizações**
- 🔹 **Criação de categorias de uso**
- 🔹 **Treinamento de modelo Random Forest**
- 🔹 **Avaliação com métricas de performance**
- 🔹 **Dashboard interativo com Streamlit**

## 🧠 Insights

- O tempo de uso e o uso do app no último mês foram variáveis altamente influentes para prever o churn.
- A maioria dos clientes que cancelaram não utilizou o app recentemente.
- Clientes com menor valor médio por pedido mostraram maior tendência ao cancelamento.

## 🚀 Como Executar

```bash
# Ativar o ambiente virtual (opcional)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Executar o dashboard Streamlit
streamlit run dashboards/dashboard.py
