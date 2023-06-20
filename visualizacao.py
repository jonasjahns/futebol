# coding: latin-1
import matplotlib.pyplot as plt
import pandas as pd

"""
Como fonte de dados eu utilizei os dados presentes no seguinte link:
https://basedosdados.org/dataset/c861330e-bca2-474d-9073-bc70744a1b23?table=18835b0d-233e-4857-b454-1fa34a81b4fa
Para facilitar o processo fiz a extracao dos dados de 2020 (os mais atuais do database) para um arquivo CSV
"""

df = pd.read_csv("bases/2020.csv")

"""
Aqui temos vários conceitos novos, vamos por partes:
groupby: essa função vai agrupar o dataframe pelos parâmetros recebidos, nesse caso estou agrupando por 'rodada'
[[]]: estamos filtrando o dataframe para exibir apenas as colunas 'gols_man' e 'gols_vis'
mean(): pedimos para que o dataframe calcule a média das colunas filtradas acima
plot(): com esse comando criamos um gráfico em memória, ainda sem exibir na tela
plt.show(): usado para exibir o gráfico gerado acima
"""
df.groupby('rodada')[['gols_man', 'gols_vis']].mean().plot()
plt.show()

"""
Vamos descobrir se há relação entre a diferença do preço do elenco e a quantidade de gols que cada time marca?
Além disso já acrescentamos muito conhecimento :)
Para criarmos uma coluna em um dataframe precisamos somente declarar a coluna df['nome_da_coluna'] = alguma operação
Nos exemplos abaixo estamos fazendo a diferença entre os valores do mandante e do visitante
Então, para as duas colunas novas, sempre que o valor for positivo é favorecendo o mandante
"""
df['diferença_gols'] = df['gols_man'] - df['gols_vis']
df['diferença_elenco'] = df['valor_equipe_titular_man'] - df['valor_equipe_titular_vis']

"""
Agora vamos falar da exibição
Simplesmente copiando o exemplo acima, temos um gráfico que não nos diz muito.
Isso acontece devido a diferença de escala entre o valor dos elencos(Em alguns milhões) e a quantidade de gols(em unidades)
Sendo assim, precisamos incrementar o plot do dataframe
Definimos com a função line() que teremos um gráfico de linhas
Dentro da função line, dizemos que o secondary_y (eixo y secundário) será regido pela 'diferença_gols'
Assim, a própria biblioteca se vira para criar dois eixos separados
"""
df.groupby('rodada')[['diferença_gols', 'diferença_elenco']].mean().plot()
plt.show()
df.groupby('rodada')[['diferença_gols', 'diferença_elenco']].mean().plot.line(secondary_y=['diferença_gols'])
plt.show()

"""
Por fim, para não ficar muito extenso
Vamos criar uma função para aplicarmos no dataframe
Essa função retorna 1 se o time que venceu tinha o melhor elenco e -1 caso contrário
Em seguida vamos aplicar essa função no dataframe, criando uma nova coluna 'resultado_esperado'
df.apply(): primeiro parâmetro é o nome da função que queremos aplicar, o parâmetro 'axis=1' define que aplicaremos linha a linha
Então mostramos o gráfico do resultado esperado
"""


def calcula_relacao(row):
    if row['diferença_gols'] > 0 and row['diferença_elenco'] > 0:
        return 1
    elif row['diferença_gols'] < 0 and row['diferença_elenco'] < 0:
        return 1
    else:
        return -1


df['resultado_esperado'] = df.apply(calcula_relacao, axis=1)
df.groupby('rodada')[['resultado_esperado']].mean().plot()
plt.show()
