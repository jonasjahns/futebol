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
Aqui temos v�rios conceitos novos, vamos por partes:
groupby: essa fun��o vai agrupar o dataframe pelos par�metros recebidos, nesse caso estou agrupando por 'rodada'
[[]]: estamos filtrando o dataframe para exibir apenas as colunas 'gols_man' e 'gols_vis'
mean(): pedimos para que o dataframe calcule a m�dia das colunas filtradas acima
plot(): com esse comando criamos um gr�fico em mem�ria, ainda sem exibir na tela
plt.show(): usado para exibir o gr�fico gerado acima
"""
df.groupby('rodada')[['gols_man', 'gols_vis']].mean().plot()
plt.show()

"""
Vamos descobrir se h� rela��o entre a diferen�a do pre�o do elenco e a quantidade de gols que cada time marca?
Al�m disso j� acrescentamos muito conhecimento :)
Para criarmos uma coluna em um dataframe precisamos somente declarar a coluna df['nome_da_coluna'] = alguma opera��o
Nos exemplos abaixo estamos fazendo a diferen�a entre os valores do mandante e do visitante
Ent�o, para as duas colunas novas, sempre que o valor for positivo � favorecendo o mandante
"""
df['diferen�a_gols'] = df['gols_man'] - df['gols_vis']
df['diferen�a_elenco'] = df['valor_equipe_titular_man'] - df['valor_equipe_titular_vis']

"""
Agora vamos falar da exibi��o
Simplesmente copiando o exemplo acima, temos um gr�fico que n�o nos diz muito.
Isso acontece devido a diferen�a de escala entre o valor dos elencos(Em alguns milh�es) e a quantidade de gols(em unidades)
Sendo assim, precisamos incrementar o plot do dataframe
Definimos com a fun��o line() que teremos um gr�fico de linhas
Dentro da fun��o line, dizemos que o secondary_y (eixo y secund�rio) ser� regido pela 'diferen�a_gols'
Assim, a pr�pria biblioteca se vira para criar dois eixos separados
"""
df.groupby('rodada')[['diferen�a_gols', 'diferen�a_elenco']].mean().plot()
plt.show()
df.groupby('rodada')[['diferen�a_gols', 'diferen�a_elenco']].mean().plot.line(secondary_y=['diferen�a_gols'])
plt.show()

"""
Por fim, para n�o ficar muito extenso
Vamos criar uma fun��o para aplicarmos no dataframe
Essa fun��o retorna 1 se o time que venceu tinha o melhor elenco e -1 caso contr�rio
Em seguida vamos aplicar essa fun��o no dataframe, criando uma nova coluna 'resultado_esperado'
df.apply(): primeiro par�metro � o nome da fun��o que queremos aplicar, o par�metro 'axis=1' define que aplicaremos linha a linha
Ent�o mostramos o gr�fico do resultado esperado
"""


def calcula_relacao(row):
    if row['diferen�a_gols'] > 0 and row['diferen�a_elenco'] > 0:
        return 1
    elif row['diferen�a_gols'] < 0 and row['diferen�a_elenco'] < 0:
        return 1
    else:
        return -1


df['resultado_esperado'] = df.apply(calcula_relacao, axis=1)
df.groupby('rodada')[['resultado_esperado']].mean().plot()
plt.show()
