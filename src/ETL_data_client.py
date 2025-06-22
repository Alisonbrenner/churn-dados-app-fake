import pandas as pd

df = pd.read_csv(r"C:\Users\alyson brenner\Documents\PROJETOS DATA ENGINER\churn-predictor-engdados\data\raw\clientes_ficticios.csv")    



# adicionar classificação de tempo de uso
def classificar_tempo(dias):
    if dias < 30:
        return "novo"
    elif dias <= 180:
        return "intermediário"
    else:
        return "antigo"
    
#criar coluna de classificação
df['categoria_tempo_uso']= df['tempo_uso'].apply(classificar_tempo)


#tratar a coluna de data

df['data_cadastro'] = pd.to_datetime(df['data_cadastro'])



df.to_csv(r'C:\Users\alyson brenner\Documents\PROJETOS DATA ENGINER\churn-predictor-engdados\data\processed\churn_dataset.csv')