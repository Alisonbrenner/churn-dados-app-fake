# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

st.set_page_config(page_title="Churn Dashboard", layout="wide")

# --- Carregar dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv('data/processed/churn_dataset.csv')
    df['data_cadastro'] = pd.to_datetime(df['data_cadastro'])
    return df

df = carregar_dados()

st.title("📊 Análise e Previsão de Cancelamento de Clientes (Churn)")

# --- Exibição dos dados
with st.expander("🔍 Visualizar dados"):
    st.dataframe(df.head())

# --- Gráfico 1: Distribuição do tempo de uso
st.subheader("📈 Distribuição do Tempo de Uso")
fig1, ax1 = plt.subplots()
sns.histplot(df['tempo_uso'], bins=30, kde=True, ax=ax1)
ax1.set_xlabel("Tempo de Uso (dias)")
ax1.set_ylabel("Frequência")
st.pyplot(fig1)

# --- Gráfico 2: Uso do app x Cancelamento
st.subheader("📱 Uso do App no Último Mês x Cancelamento")
fig2, ax2 = plt.subplots()
sns.countplot(x='usou_app_ultimo_mes', hue='cancelou', data=df, ax=ax2)
ax2.set_xlabel("Usou App no Último Mês")
ax2.set_ylabel("Quantidade de Clientes")
st.pyplot(fig2)

# --- Gráfico 3: Valor médio x Cancelamento
st.subheader("💰 Valor Médio por Pedido x Cancelamento")
fig3, ax3 = plt.subplots()
sns.boxplot(x='cancelou', y='valor_medio', data=df, ax=ax3)
ax3.set_xlabel("Cancelou")
ax3.set_ylabel("Valor Médio (R$)")
st.pyplot(fig3)

# --- Gráfico 4: Tempo de uso categorizado x Cancelamento
st.subheader("⏱️ Categoria de Tempo de Uso x Cancelamento")
fig4, ax4 = plt.subplots()
sns.countplot(x='categoria_tempo_uso', hue='cancelou', data=df, ax=ax4)
ax4.set_xlabel("Categoria de Tempo de Uso")
ax4.set_ylabel("Clientes")
st.pyplot(fig4)

# --- Modelo preditivo
st.subheader("🤖 Modelo Preditivo de Cancelamento")

# Preparar dados
df_model = pd.get_dummies(df, columns=['categoria_tempo_uso', 'usou_app_ultimo_mes'], drop_first=True)
df_model = df_model.drop(['id_cliente', 'data_cadastro'], axis=1)
X = df_model.drop('cancelou', axis=1)
y = df_model['cancelou']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Avaliação
y_pred = modelo.predict(X_test)

st.markdown("**Relatório de Classificação:**")
st.text(classification_report(y_test, y_pred))

st.markdown("**Matriz de Confusão:**")
st.dataframe(pd.DataFrame(confusion_matrix(y_test, y_pred), 
             columns=["Pred: Não Cancelou", "Pred: Cancelou"], 
             index=["Real: Não Cancelou", "Real: Cancelou"]))

# --- Importância das variáveis
st.subheader("📌 Importância das Variáveis no Modelo")

importancias = modelo.feature_importances_
features = pd.Series(importancias, index=X.columns).sort_values()

fig_imp, ax_imp = plt.subplots()
features.plot(kind='barh', ax=ax_imp)
ax_imp.set_title("Importância das Variáveis")
st.pyplot(fig_imp)
