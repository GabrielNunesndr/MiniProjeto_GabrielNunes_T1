                # importando bibliotecas 
import pandas as pd 
import numpy as np

                # lendo o CSV
df_sujo= pd.read_csv ('dados/Base Varejo.csv',sep=';')
df = df_sujo.copy()

                # visualização inicial dos dados 
print(df.head())

                # gera um relatório completo do DataFrame
def relatorio_qualidade(df):
    
    print("        RELATÓRIO ")
    print(f"\n Total de linhas:   {df.shape[0]:,}")
    print(f" Total de colunas: {df.shape[1]:,}")
    print(f"Linhas duplicadas: {df.duplicated().sum():,}")
    print("\n Valores ausentes por coluna:")
    nulos = df.isnull().sum()
    pct_nulos = (df.isnull().sum() / len(df) * 100).round(2)

    relatorio = pd.DataFrame({
        'Tipo': df.dtypes,
        'Nulos': nulos,
        '% Nulos': pct_nulos,
        'Únicos': df.nunique()
    })
    print(relatorio)
    

relatorio_qualidade(df)

                # remoção de duplicatas  
df = df.drop_duplicates()

                # remoção de colunas inúteis
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])

                # padronização de texto
df['PR_CAT'] = df['PR_CAT'].str.title().str.strip()
df['PR_NOME'] = df['PR_NOME'].str.title().str.strip()
                 
                # procurando nulos escondidos
print(df['PR_CAT'].value_counts())
print(df['PR_NOME'].value_counts())

                # Padronização de valores inválidos
df.replace(['#N/D','NULL', 'N/A', '', ' '], np.nan, inplace=True)

                # convertendo as datas 
df['DATA'] = pd.to_datetime(df['DATA'],dayfirst=True,errors='coerce')

                # Preenchendo valores nulos, usando (if/else)
df['PR_NOME'] = [
    'Sem Nome' if pd.isna(valor) else valor
    for valor in df['PR_NOME']
]

df['PR_CAT'] = [
    'Sem Categoria' if pd.isna(valor) else valor
    for valor in df['PR_CAT']
]

                # relatório final dos dados
relatorio_qualidade(df)

                # visualização final dos dados 
print("Dados apos limpeza")
print(df.head())