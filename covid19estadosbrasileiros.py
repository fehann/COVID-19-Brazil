# -*- coding: utf-8 -*-
"""Covid19EstadosBrasileiros

# Dados sobre COVID-19 por Estado Brasileiro

## Fonte de Dados

Boletins informativos e casos do coronavírus por município por dia.

https://brasil.io/dataset/covid19/caso
"""

# Commented out IPython magic to ensure Python compatibility.
# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datadotworld as dw
import altair as alt

# Set style & figures inline
sns.set()
# %matplotlib inline

st.write("""
# Visualização de dados relacionados ao COVID-19 no Brasil
Visando entender o comportamento da evolução da COVID-19 no Brasil, esta página apresenta o ritmo de aceleração ou desaceleração da doença por estado brasileiro. A inspiração para criação desta visualização veio a partir do gráfico publicado pela organização [Our World in Data](https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death) que tem como objetivo apresentar não somente o número de casos mas também o ritmo no qual as morte estão ocorrendo.

## Sobre os dados
É importante salientar que esta visualização se baseia em dados disponibilizados pelas secretarias estaduais, coletados de forma manual uma vez que não há um banco de dados integrados, conforme site [Brasil.io](https://brasil.io/dataset/covid19/caso). São dados passível de erros e vieses portanto qualquer análise não deve ser baseada somente nestes dados e toda tomada de decisões deve considerar uma análise científica com informações complementares.
""")

# Importando dados do site
#data = pd.read_csv('https://brasil.io/dataset/covid19/caso?format=csv')
dw_df = dw.load_dataset('fehann/brasil-io-covid19')
data = dw_df.dataframes['caso']
data.info()

data.head(n = 15)

data.describe()

## Manipulação dos Dados

# Dados por estado
data_states = data[data.place_type.eq('state')]
data_states.head(n = 15)

# Segregar dados de casos confirmados e mortes
data_states_confirmed = data_states[['date','state','confirmed']]
data_states_confirmed.info()

data_states_deaths = data_states[['date','state','deaths']]
data_states_deaths.info()

# Tabela de população de cada estado em 2019

states_pop = data_states[['state','estimated_population_2019']]
states_pop = states_pop.drop_duplicates()
states_pop.set_index('state', inplace = True)
#states_pop

## Numero de Mortes

### Transformação de dados


# Transformar dataframe de long para wide
data_deaths = data_states_deaths.pivot(index='state', columns='date', values='deaths')
data_deaths.head()

# Verificar index das observação
#data_deaths.index

# Está indexado por estado mas para criação da visualização é melhor que esteja indexado por data
data_deaths = data_deaths.transpose()
#data_deaths

# Verificar se a indexação está como data
#data_deaths.index

# Conversão do index para DateTimeIndex pois está como 'object'
datetime_index = pd.DatetimeIndex(data_deaths.index)
data_deaths.set_index(datetime_index, inplace = True)
# Verificar o index novamente
#data_deaths.index

# Existem NAs entre observações válidas, provavlemente houve um falta de informação para aquele estado naquele dia. Vamos considerar este valor igual ao último valor válido para aquele estado.
data_deaths.fillna(method='ffill', inplace=True)
#data_deaths

# Apesar dos dados serem desde fevereiro de 2020, a primeira morte ocorreu somente em 17/03/2020, portanto estas primeiras observações serão removidas
data_deaths = data_deaths.loc['2020-03-16':data_deaths.index[len(data_deaths.index)-3]]
#data_deaths

### Visualização de Dados

# Visualizar número totais de mortes por estado
data_deaths.plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20)
plt.xlabel('Data', fontsize=20);
plt.ylabel('Número de mortes confirmadas', fontsize=20);
plt.title('Evoluçao de mortes confirmadas pela COVID-19', fontsize=20);

# Visualizar número totais de mortes por estado na escala semi-logarítmica
data_deaths.plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy = True)
plt.xlabel('Data', fontsize=20);
plt.ylabel('Número de mortes confirmadas', fontsize=20);
plt.title('Evoluçao de mortes confirmadas pela COVID-19', fontsize=20);

### Visualização de dados alinhando o primeiro dia com 5 mortes

# Iterar sobre as colunas e valores < 5 serão nulos
for col in data_deaths.columns:
    data_deaths.loc[(data_deaths[col] < 5), col] = None

# Check out tail
data_deaths.tail()

# Retirar colunas que tenham tudo NaNs (estados que não chegaram a 5 mortes)
data_deaths.dropna(axis = 1, how = "all", inplace = True)
data_deaths.info()

# Criar dataframe com a data do primeiro dia com a 5a morte em cada estado
date_5th_death = data_deaths.apply(pd.Series.first_valid_index)
df_5th_death = pd.DataFrame(date_5th_death)
#df_5th_death

# Resetar o index, retirar a coluna de data
data_deaths_drop = data_deaths.reset_index().drop(['date'], axis = 1)
data_deaths_drop.head()

# Trazer para cima os dados a partir do primeiro dado válido (shift)
for col in data_deaths_drop.columns:
    data_deaths_drop[col] = data_deaths_drop[col].shift(-data_deaths_drop[col].first_valid_index())
# check out head
#data_deaths_drop

# Evolução na escala semi-logarítimica
data_deaths_drop.plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy = True)
plt.xlabel('Dias', fontsize=20);
plt.ylabel('Número de mortes confirmadas', fontsize=20);
plt.title('Total de mortes confirmadas nos estados com pelo menos 5 mortes', fontsize=20);

### Visualização interativa com altair

# Transformar dados em long para utilizar no altair
deaths_long = data_deaths_drop.reset_index().melt(id_vars = 'index', value_name = 'Deaths').rename(columns={'index':'Day'})
#deaths_long

# Adicionar primeiro dia da 5a morte por estado
deaths_long = deaths_long.merge(df_5th_death, left_on='state', right_index=True, how='left')
#deaths_long

# Adicionar coluna com a data de cada observação
from datetime import datetime
from datetime import timedelta
deaths_long['Date'] = deaths_long.iloc[:,3] + deaths_long['Day'].map(timedelta)
#deaths_long

# Remover coluna com primeiro dia da 5a morte
deaths_long = deaths_long.drop([deaths_long.columns[3]] ,  axis='columns')
#deaths_long

# Adicionar população por estado
deaths_long = deaths_long.merge(states_pop, left_on='state', right_index=True, how='left')
deaths_long.head()

# Adicionar taxa de mortes a cada 100.000 habitantes
deaths_long['DeathPop'] = deaths_long['Deaths']/deaths_long['estimated_population_2019']*100000
deaths_long.head()

# drop NaNs
deaths_long = deaths_long.dropna()
#deaths_long



# Selection tool
selection = alt.selection_single(fields=['state'])
# Color change when clicked
color = alt.condition(selection,
                    alt.Color('state:N'),
                    alt.value('lightgray'))


# Base altair plot
base = alt.Chart(deaths_long, title="Mortes confirmadas pelo COVID-19 por estado").mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color=alt.Color('state', legend=None),
)

# Chart
chart = base.encode(
  color=alt.condition(selection, 'state:N', alt.value('lightgray')),
  tooltip=[alt.Tooltip('state:N', title = 'Estado'), alt.Tooltip('yearmonthdate(Date):N', title = 'Data', format = '%d/%m/%Y'), alt.Tooltip('Deaths:N', title = 'Mortes')]
).add_selection(
  selection
)

# Overlay
overlay = base.encode(
  color='state',
  opacity=alt.value(0.5),
).transform_filter(
  selection
)

# Text labels
text = base.mark_text(
    align='left',
    dx=5,
    size=15
).encode(
    x=alt.X('Day', aggregate='max',  axis=alt.Axis(title='Dias a partir da 5a morte no estado')),
    y=alt.Y('Deaths', aggregate={'argmax': 'Day'}, axis=alt.Axis(title='Mortes (escala logarítmica)')),
    text='state'
).transform_filter(
    selection
)

# Add doubling line

## Death doubles every 2 days
j = 0
for i in range(0,deaths_long.Day.max()):
    if 5*pow(2,(i/2)) < deaths_long.Deaths.max():
      j = i+2

temp = {'x':[0,j],'y':[5*pow(2,(0/2)),5*pow(2,(j/2))]}
source2 = pd.DataFrame(temp, columns = ['x','y'])

double2 = alt.Chart(source2).mark_line(strokeDash=[2,2]
).encode(
    x='x:Q',
    y='y:Q',
    color=alt.value('lightgray')
)

text2 = alt.Chart({'values':[{'x': 13, 'y': 500}]}).mark_text(
    text='mortes duplicam a cada 2 dias', angle=290,
    size=13,
    color = 'gray'
).encode(
    x='x:Q', y='y:Q'
)

## Death doubles every 5 days
j = 0
for i in range(0,deaths_long.Day.max()):
    if 5*pow(2,(i/5)) < deaths_long.Deaths.max():
      j = i+2

temp = {'x':[0,j],'y':[5*pow(2,(0/5)),5*pow(2,(j/5))]}
source5 = pd.DataFrame(temp, columns = ['x','y'])

double5 = alt.Chart(source5).mark_line(strokeDash=[2,2]
).encode(
    x='x:Q',
    y='y:Q',
    color=alt.value('lightgray')
)

text5 = alt.Chart({'values':[{'x': 28, 'y': 250}]}).mark_text(
    text='a cada 5 dias', angle=311,
    size=13,
    color = 'gray'
).encode(
    x='x:Q', y='y:Q'
)

## Death doubles every 10 days
j = 0
for i in range(0,deaths_long.Day.max()):
    if 5*pow(2,(i/10)) < deaths_long.Deaths.max():
      j = i+2

temp = {'x':[0,j],'y':[5*pow(2,(0/10)),5*pow(2,(j/10))]}
source10 = pd.DataFrame(temp, columns = ['x','y'])

double10 = alt.Chart(source10).mark_line(strokeDash=[2,2]
).encode(
    x='x:Q',
    y='y:Q',
    color=alt.value('lightgray')
)

text10 = alt.Chart({'values':[{'x': 60, 'y': 350}]}).mark_text(
    text='a cada 10 dias', angle=330,
    size=13,
    color = 'gray'
).encode(
    x='x:Q', y='y:Q'
)

# Sum it all up
chartA = alt.layer(chart, overlay, text, double2, double5, double10, text2, text5, text10).configure_axis(
    labelFontSize=15,
    titleFontSize=18
).configure_title(
    fontSize=23
).properties(
    width=650,
    height=800
)

"""---

## Número de mortes por estado brasileiro a partir da 5a morte notificada

Nesta visualização não estão aparecendo as legendas das linhas de referências em cinza, são elas da esquerda para a direita: mortes a cada 2 dias, a cada 5 dias e a cada 10 dias respectivamente. Na [página estática](https://fehann.github.io/COVID-19-Brazil/) estas legendas estão aparecendo caso queira consultar.
"""

st.write(chartA)

# Sum em up!
#chart + overlay + text

# Mortes por habitantes

# Base altair plot
basepop = alt.Chart(deaths_long, title="Mortes confirmadas pelo COVID-19 por 100 mil habitantes").mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('DeathPop'),
    color=alt.Color('state', legend=None),
)

# Chart
chartpop = basepop.encode(
  color=alt.condition(selection, 'state:N', alt.value('lightgray')),
  tooltip=[alt.Tooltip('state:N', title = 'Estado'), alt.Tooltip('yearmonthdate(Date):N', title = 'Data', format = '%d/%m/%Y'), alt.Tooltip('DeathPop:N', title = 'Proporção de Mortes', format = '.2f')]
).add_selection(
  selection
)

# Overlay
overlaypop = basepop.encode(
  color='state',
  opacity=alt.value(0.5),
).transform_filter(
  selection
)

# Text labels
textpop = basepop.mark_text(
    align='left',
    dx=5,
    size=15
).encode(
    x=alt.X('Day', aggregate='max',  axis=alt.Axis(title='Dias a partir da 5a morte no estado')),
    y=alt.Y('DeathPop', aggregate={'argmax': 'Day'}, axis=alt.Axis(title='Mortes a cada 100 mil habitantes')),
    text='state'
).transform_filter(
    selection
)

# Sum em up!
chartB = alt.layer(chartpop + overlaypop + textpop).configure_axis(
    labelFontSize=15,
    titleFontSize=18
).configure_title(
    fontSize=23
).properties(
    width=650,
    height=800
)

"""
## Proporção de mortes confirmadas em relação a população do estado
Visando complementar o processo de análise, foi criada a seguinte visualização para mostrar a proporção de mortes confirmadas pelo COVID-19 a cada 100 mil habitantes por estado brasileiro. A população utilizada foi a estimada pelo IBGE para o ano de 2019.
"""

st.write(chartB)

"""---
## Considerações
O único tratamento nos dados originais foi o preenchimento dos números faltantes, provavelmente devido à falta de disponibilidade de informação oficial pela secretaria em um determinado dia, porém não acontece com frequência. Os dados pendentes foram preenchidos com o mesmo número total de mortes válido antes daquele dia para aquele estado. Normalmente esta lacuna ocorre nos dias mais recentes portanto, para fins de visualização, não foram considerados os últimos 2 dias. Como o intuito deste gráfico é mostrar a tendência é importante termos os dados completos para não tirarmos conclusões precipitadas.

## Referências

* [Brasil.io](https://brasil.io/dataset/covid19/caso)
* [Our World in Data](https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death)
* [DataCamp Live Coding: Covid-19 Exploratory Data Analysis](https://www.facebook.com/726282547396228/videos/861466570947781/)
* [Altair: Interactive Plots on the Web](https://matthewkudija.com/blog/2018/06/22/altair-interactive/)
* [Doubling time](https://en.wikipedia.org/wiki/Doubling_time)
* [How coronavirus charts can mislead us](https://www.youtube.com/watch?v=O-3Mlj3MQ_Q&feature=share)

---

- *O código original para geração desta visualização pode ser acessado aqui: [Python](https://github.com/fehann/COVID-19-Brazil/blob/master/Covid19EstadosBrasileiros.py).*
- *A página estática pode ser acessada [aqui](https://fehann.github.io/COVID-19-Brazil/).*
- *A versão em R desta visualização pode ser acessada aqui: [RPubs](https://rpubs.com/fehann/covid19brasil).*
- *Em caso de dúvidas, comentários ou sugestões podem entrar em contato através do [LinkedIn](https://www.linkedin.com/posts/activity-6657331106443993088-V7Lm).*
- *Cuidem da saúde e da familia, colaborando vamos sair desta situação o mais breve possível.*
"""
