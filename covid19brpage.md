title: Covid-19 cases in Brazil
date: 2020-04-12 06:00
authors: Fernando Hannaka
comments: true
slug: altair-interactive
tags: covid19, coronavirus, brazil, python, altair, vega, interactive
include: vega


# Visualização de dados relacionados ao COVID-19 no Brasil
Visando entender o comportamento da evolução da COVID-19 no Brasil, esta página visa apresentar o ritmo de aceleração ou desaceleração da doença por estado brasileiro. A inspiração para criação desta visualização veio a partir do gráfico publicado pela organização [Our World in Data] (https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death) que visa apresentar não somente o número de casos mas também o ritmo no qual as morte estão ocorrendo.

## Sobre os dados 
É importante salientar que esta visualização está baseado em dados disponibilizados pelas secretarias estaduais, coletados de forma manual uma vez que não há um banco de dados integrados, conforme site [Brasil.io] (https://brasil.io/dataset/covid19/caso). São dados passível de erros e vieses portanto qualquer análise não deve ser baseada somente nestes dados e toda tomada de decisões deve haver uma análise científica com informações complementares.

## Número de mortes por estado brasileiro a partir da 5a morte notificada

<div id="vis00"></div>
<script type="text/javascript">
var spec00 = {"config":{"view":{"width":400,"height":300}},"data":{"url":"https://vega.github.io/vega-datasets/data/cars.json","format":{"type":"json"}},"mark":"point","encoding":{"x":{"type":"quantitative","field":"Horsepower"},"y":{"type":"quantitative","field":"Miles_per_Gallon"}},"$schema":"https://vega.github.io/schema/vega-lite/v2.4.3.json"};
// below gives color by origin
// var spec00 = {"config":{"view":{"width":400,"height":300}},"data":{"url":"https://vega.github.io/vega-datasets/data/cars.json","format":{"type":"json"}},"mark":"point","encoding":{"color":{"type":"nominal","field":"Origin"},"x":{"type":"quantitative","field":"Horsepower"},"y":{"type":"quantitative","field":"Miles_per_Gallon"}},"$schema":"https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt00 = {"mode": "vega-lite"};

function showError(el00, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el00 = document.getElementById('vis00');
vegaEmbed("#vis00", spec00, embed_opt00)
.catch(error => showError(el00, error));
</script>



## Considerações
O único tratamento nos dados originais foi o preenchimento de dados faltantes, provavelmente devido a falta de disponibilidade do dado pela secretaria em determinado dia, porém é algo que não acontece com frequência. Os dados pendentes foram preenchidos com o mesmo total de casos de mortes válido para aquele estado. Normalmente estes dados faltantes ocorrem nos dias mais recentes portanto para fins de visualização não foram considerados os últimos 3 dias, para permitir a obtenção completa dos dados antes de serem apresentados. Como o intuito deste gráfico é mostrar a tendência é importante termos os dados completos para não tirarmos conclusões precipitadas.

## Referências

* [Brasil.io] (https://brasil.io/dataset/covid19/caso)
* [Our World in Data] (https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death) 
* [DataCamp Live Coding: Covid-19 Exploratory Data Analysis] (https://www.facebook.com/726282547396228/videos/861466570947781/)

---

- *O notebook original para para geração desta visualização pode ser acessado aqui: [Jupyter Notebook](https://github.com/fehann/covid19brazil/blob/master/Covid19EstadosBrasileiros.ipynb) that was used to generate these examples.*
- *Cuidem da saúde e da familia, colaborando vamos sair desta situação o mais breve possível.*
