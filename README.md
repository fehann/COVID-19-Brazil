<!---
title: Covid-19 cases in Brazil
date: 2020-04-12 06:00
authors: Fernando Hannaka
comments: true
slug: altair-interactive
tags: covid19, coronavirus, brazil, python, altair, vega, interactive
include: vega
-->

# Visualização de dados relacionados ao COVID-19 no Brasil
Visando entender o comportamento da evolução da COVID-19 no Brasil, esta página apresenta o ritmo de aceleração ou desaceleração da doença por estado brasileiro. A inspiração para criação desta visualização veio a partir do gráfico publicado pela organização <a target="_blank" rel="noopener noreferrer" href="https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death">Our World in Data</a> que tem como objetivo apresentar não somente o número de casos mas também o ritmo no qual as morte estão ocorrendo.

## Sobre os dados 
É importante salientar que esta visualização está baseado em dados disponibilizados pelas secretarias estaduais, coletados de forma manual uma vez que não há um banco de dados integrados, conforme site <a target="_blank" rel="noopener noreferrer" href="https://brasil.io/dataset/covid19/caso">Brasil.io</a>. São dados passível de erros e vieses portanto qualquer análise não deve ser baseada somente nestes dados e toda tomada de decisões deve considerar uma análise científica com informações complementares.

## Número de mortes por estado brasileiro a partir da 5a morte notificada
<img 
    src="visualization.svg" 
    alt="Mortes por estado brasileiro"
    height="600"
    width="1000" />

<a target="_blank" rel="noopener noreferrer" href="https://vega.github.io/editor/#/url/vega-lite/N4KABGBEDGD2B2AzAlgc0gLjMSA3ZApgO6bYwIAuy8ArrDQM4DqyAJhQBakAsADLwBooceFVr0GACQJoOFUgGZ+AX2UDwUADYBDAJ4EATqQDaGiKAiWoAW20GA1qRwVdABwKlIm6h6GRYrtrQyC6kvAB0AOx+DBQGsPYELOxcWNxqZpaQBPBwrNToWBZWWXCasEZFmSXCCPlUCE7VNVAu7p7wsNbU2pqQ6i0lkCgEmqyesdoUvs01kAyjBNAN8BOLyxX8AEyQs5YZgxB4vTQeWF6yFKgGeruDBy2QAB5OkG1nUACONNqiIVPIXC+KAjMaeAAitwec10TUOrTcH0g31+VAoAKB-T2R1B43O4IIUw4DCx8Pm0F6H2ciM85XQyj2DJq0KyHBkqDkpAAbABWQTNebrFavBaaJYUTa8HZFN4084MApi-ogwhjElYYzzdHTSAAXVUAyGaKV5wAKrB0ZowKwCGBrBVpgwwCIUAZbKxtE73OUwABhADyADUAJLggC0AEYAJxgVwVMAESasWBgABGNwVYuQ8RJhqskCIbE4pAAHPxMizivnbA5Xu9aT5lf5AsFQlgItEoLF4olksW0iyjjk8gU4Y8yhU63KoJ1uvBek3cRNtR5B1kAkEQrCZbgTh8Ijy10cJbBNFRXCZsWR6+dZz0+n4l-KV5Aj5Zqe1b1174vVXioAActo1irnsup5kMLwyjeXw-H82qAsCwx-hCUIQfm27YFesqfrBqL-FQmLoUMT5QASRK5thDAUia17Tl4sD0oyzRrpAbKXNyfLEW8IS0ZA5qWtatr2gYjrOggrrup6sajCmAYhuG0axvGibosmaYZsgWY5qSRo3PADCIBU1gmDgKBnoYIpCsgjTykKko7Ko4ECoWKSluWViVgKNaONB9HTE88h+L0aCrOcYqIEFUCsFBYA8jEyAAF4fBGvCscOsD5PAhRYYM5DlJUdG4ZAd7zg+KqjP+WpTEhYqoDk-60Jomhvm8BCBVOxWlQuj4oc+NWvsRRyxVWjwwcicFohiMxktoqDXAQqADectgvENWTaE8yDqtevFIuCyDSdosZ2FQBjWsdPLHSJ0xgJ0CZJrAg3YaRkCQrCjLrZAmGjXM40ovB026Xlc0LUtOoynYqCrahsJvkcm3bXWe2eAAsg6ibiUg2ZSU6AAUiY0cddJ2AAtxQ3QUgAlM9ZKveRnAksxzLcexHLyFgvL8n9KNmhavRCXaGNOi6OPaB6XqyX6QahpGMZxudqniym6aelpMg6dxcS-IZxmmchFmFTgorijZYVdvZBjbK+yjOXMrn9mAZa8BWGh29FUzaK884gZ4HromGBCpgoWxbISBARqwSiRBGfIKNoCiRNAPIRpEkSJ5ErBclsvC01AAAk1FsrYnhyBQrgMBgAD0VdAkt4SoCEHA0Km4Q2VXRcELYteLdoYbeNMtfcOEJbhBG4QAFYMI0hqQP7noEBQO2jXPnuB8Hofh5H0ex7w8eJ8nqfp2nWc55eNQ4O9YQxC+5wAIKo02DPEqQkRrpftxYBGN-LVAD9P4SRmpAIxbHfm9T+YAtg-whn-R+fhn47VjmAq+WAFDQKRP-eBgCX5fyjMgiB3B0GeEwWRbBO0tgKHwZheKXZb6wIARRRQaViIf0wlyIh984GkMYWkZhzRWHX1ob-SAAAhO+DCgGcyocAjhUAxESJwWAN+LDwGYSgUImBojxFYJ4WAPBKiUFgDQRopE8idGSLAKlaRaRZFaIUYg9IBiIE0Oqposx3CLERhLNYsA7CTGeHcW9MhwD9H8NUYI1xSJfQAFF7GkEPE4zC39-HnBiXErACSwmGPUZEzwaTzGKOUVkiBxjcmpNiQUnaoSL7hJsSkqA+SPGKK2BGHxLjJiaMaUE3RocfF+LKQ0ipTTyGUMSa-WxXSEGKEyTUwxJYJlDO6RYhQMySgCKwFGBZ6SwB8B8alLZlT4lFNmRAiMySBmQEmcEjJxy1m1LAIIepb0ABi2zVlWHWZY2x4JXmHKkWMrAOSOn7V+cM1+PjSnAohKCpZhSfGEKeT87ZViAVxW+TCqZX9QGov6VC-EGLrmWOxcUzCnYLlIr+ZY0ZJKIl4qgNEgAym8vZtjGXbK5D4oFdDIBsspRy1FkLuW8rBf8mldSLnCthTtflYq0VPMlZi3xfTWVMspbcj59zHkXIAOL+mZai85dLIC6v1bKrlwiTVqohbYy1IqlE+K1Ua1G2i7VnJZU851yLiUnLUbYz1lKIwyp9bS7lqNtXsvdRcsNEbUXms0dGvl1qPXhspdUu5hiEVRpTa61pqL2mhuzVK4BjjZW4oLci9575NW2IAAouqLRkyNRq62muDYC2t9bFVBvTSUjt2z1VVsMY67lNaRH9qbSOsdAbc2yuHcImtizFWVvMPcw1I7F2EuXWQbJtaN26O7Rqwxgr517osQewdBDd3bO8Xmq9qblVPIXcivhbalF3tdSW198zH2nuaTO19myf3bKUHsudmin2UoUJ+ntSS10nu2dwc9K7DEgPfQ2uKSHt0QLA0iGtwZW0wZkY+-DibY21pI3agdyHsO1oAEoEcPacuj46yOPvowGl9hHUHMYDdBxjmFM3NvY66rdnz83zuE+h1OD6Lk1sk4qrYfGL2YRw54WjAApGNsq4OaI09ezlti9P3oFYZzTHH4WmeRdS194ndNmddVRrDbDLMBpvbKslRqjN2ooT479FyvPoa2G5gDLm7XcH-VxyxqnzgBcVdwRznyzmhfQzyYLkXUNPNi4SrkSnqNJOPXZ-tEX+PFuS4qksaaStf1s0iLLujUqYcS2W4RdXPG9NRdFqAtGAJadfTp2rPWrWsf84NyjSaRv6dRYJ7l3XkXFeU-Ewzo2pPzbyyGlrqq7WidXYZzbKWDOZb2128bnmjuEoS-c6bG2WOypq2ps7ui0tVd8btyb7nXvmdRX507yLctOfW5ohlvoGMLa-rYoHIO1vtqeRDz7sqCtIlh66zjz2ruA+B9Otp4OMciZk0apHUmLuGI89ygniqvEOvBzWyH-2wcw+p8Zs1VOK0ndJwz7z3rIto8R+z9DIHb304Qyj0HL3BeUu4E9kXJPhEMt50uyXUOnbM75Qr2nejld2pLH9xLnXICy+2VGVXiX+ueH19O6z6W4086s411dCPTdy8JYG7Xq7ucO+RSWI3q67vnDN956MezmuA8dz0rkwvFepw14FyI22UPfbZ8B3gLuUOAYuX7vnMdOW6-T3FoLnKTe+5DxY7gUYOWZF1BoBkyggA/view">CLIQUE AQUI para abrir gráfico interativo</a>




## Considerações
O único tratamento nos dados originais foi o preenchimento de dados faltantes, provavelmente devido a falta de disponibilidade do dado pela secretaria em um determinado dia, porém é algo que não acontece com frequência. Os dados pendentes foram preenchidos com o mesmo total de casos de mortes válido antes daquele dia para aquele estado. Normalmente estes dados faltantes ocorrem nos dias mais recentes portanto para fins de visualização não foram considerados os últimos 2 dias, para permitir a obtenção completa dos dados antes de serem apresentados.Como o intuito deste gráfico é mostrar a tendência é importante termos os dados completos para não tirarmos conclusões precipitadas.

## Referências

* <a target="_blank" rel="noopener noreferrer" href="https://brasil.io/dataset/covid19/caso">Brasil.io</a>
* <a target="_blank" rel="noopener noreferrer" href="https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death">Our World in Data</a>
* <a target="_blank" rel="noopener noreferrer" href="https://www.facebook.com/726282547396228/videos/861466570947781/">DataCamp Live Coding: Covid-19 Exploratory Data Analysis</a>
* <a target="_blank" rel="noopener noreferrer" href="https://matthewkudija.com/blog/2018/06/22/altair-interactive/">Altair: Interactive Plots on the Web</a>

---

- *O notebook original para geração desta visualização pode ser acessado aqui: <a target="_blank" rel="noopener noreferrer" href="https://github.com/fehann/covid19brazil/blob/master/Covid19EstadosBrasileiros.ipynb">Jupyter Notebook</a> that was used to generate these examples.*
- *Cuidem da saúde e da familia, colaborando vamos sair desta situação o mais breve possível.*


<!---
Para atualizar o gráfico:
1) Google Colab - rodar o notebook
2) Salvar imagem em SVG e substituir no Github
3) Abrir no editor do Vega Lite e copiar link para Github
-->
