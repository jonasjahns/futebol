import pandas as pd

"""
Como fonte de dados eu utilizei os dados presentes no seguinte link:
https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa
Para facilitar o processo fiz a extracao dos dados de 2020 (os mais atuais do database) para um arquivo CSV
"""

df = pd.read_csv("bases/2020.csv")
# Aqui conseguimos ver a quantidade de colunas, seus nomes e tipos
print(len(df.dtypes))
print(df.dtypes)

# Importante vermos quais colunas contem algum dado vazio, isso pode impctar algum ponto de vista da analise de dados
colunas_sem_algo_dado = df.columns[df.isnull().any()].tolist()
print(len(colunas_sem_algo_dado))
print(colunas_sem_algo_dado)

# Tambem podemos usar a funcao describe para capturar algumas informacoes basicas como: Contagem, media, maximo, minimo, etc
print(df.describe())

# Lembrando que como o resultado final eh um dataframe, podemos filtrar apenas as colunas que desejamos
print(df.describe()[['gols_man', 'gols_vis', 'colocacao_man', 'colocacao_vis']])
