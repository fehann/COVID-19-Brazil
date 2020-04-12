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

<a target="_blank" rel="noopener noreferrer" href="https://vega.github.io/editor/#/url/vega-lite/N4KABGBEDGD2B2AzAlgc0gLjMSA3ZApgO6bYwIAuy8ArrDQM4DqyAJhQBakAsADLwBooceFVr0GACQJoOFUgGZ+AX2UDwUADYBDAJ4EATqQDaGiKAiWoAW20GA1qRwVdABwKlIm6h6GRYrtrQyC6kvAB0AOx+DBQGsPYELOxcWNxqZpaQBPBwrNToWBZWWXCasEZFmSXCCPlUCE7VNVAu7p7wsNbU2pqQ6i0lkCgEmqyesdoUvs01kAyjBNAN8BOLyxX8AIyQs5YZgxB4vTQeWF6yFKgGeruDBy2QAB5OkG1nUACONNqiIVPIXC+KAjMaeAAitwec10TUOrTcH0g31+VAoAKB-T2R1B43O4IIUw4DCx8Pm0F6H2ciM85XQyj2DJq0KyHBkqDkpAAbABWQTNebrFavBaaJYUTa8HZFN4084MApi-ogwhjElYYzzdHTSAAXVUAyGaKV5wAKrB0ZowKwCGBrBVpgwwCIUAZbKxtE73OUwABhADyADUAJLggC0WwAnGBXBUwARJqxYGAAEY3BVi5DxEmGqyQIhsTikAAc-EyLOKedsDle71pPmV-kCwVCWAi0SgsXiiWSRbSLKOOTyBThjzKFVrcqgnW68F6jdxE21HgHWQCQRCsJluBOHwiPNXRwlsE0VFcJmxZDr5xnPT6fkX8uXkEPlmp7RvXTvC9VeKgADltGsFc9l1XMhheGVry+H4-m1QFgWGX8IShcC8y3bBL1lD8YNRf4qExNChkfKACSJHMsIYCkTSvKcvFgelGWaVdIDZS5uT5Ii3hCGjIHNS1rVte0DEdZ0EFdd1PRjUZkwDENwyjGM4wTdEk1TdNkEzbNSSNG54AYRAKmsEwcBQU9DBFIVkEaeUhUlHZVDAgUCxSEsyysCsBWrRwoLo6YnnkPxejQVZzjFRBAqgVhILAHkYmQAAvD4tl4Fih1gfJ4EKTDBnIcpKlonDIFvOd7xVUY-y1KZELFVAcj-WhNE0V83gIALJyKkr5wfZCn2ql8iKOGLK0eaDkVgtEMRmMltFQa4CFQfrzlsF5BqybQnmQdUrx4pFwWQKTtBjOwqAMa0jp5I7hOmMBOnjRNYAGrCSMgSFYUZNbIAwka5jGlE4KmnTctm+bFp1GU7FQFaUNhV8jg2rba12zwAFkHQTMSkCzSSnQACgTaijrpOwAFuKG6CkAEonrJF6yM4EkmOZLi2I5eQsF5flfuRs0LV6QS7XRp0XWx7QPS9GS-SDUMI2jWMzpUsXkzTT1NJkbSuLiX4DKMkykPMgqcFFcVrNCzs7IMbYX2UJy5hcvswFLXhyw0W2oqmbRXjnYDPA9dEwwAJl4SJIxTBQeUiBQFEQFMtmLUtuCUSNI1YEPWClXgCF5FMaagAASKi2VsTw5AoVwGAwAB6SugUW8JUBCDgaBTcJrMrwuCFsGuFu0MNvGmGvuHCYtwi2cIACsGEaQ1ID9z0CAobaRtnj3A+D0Pw8j6PY-j3hE94ZPU5TjOs55HONWaHA3rCGJn3OABBFHG3p4lSEiVcr9uLAtlvpaoEf5+hIGakC2AHD+r0v5gADr-cG-8n5+BfttLYB4iKfwwgoGBSIAEIKAa-b+kZwHXzSJgzw2DSK4O2gHBQhDIFxU7HfOBgDyKKFSqgiBGEuQkIfvA8hzC0isMvuwt+XDGE4L4bFARNQ0ElhEZAMhr0KGkD5DQjCgh6F-0gAAIXvkw4BHMVEgNkdo3ReCwDvzYUQqBRidFiL0WAAhFjIEYPUbArRNjeF2JSgY4hLikTGNsaYrY6RHEYToVVVx-iPGBOLN4sAnDfGeEiQo8RUZYkdnCX49xyTPEOMEZY4s1iTFINyVIoRbZZG+gAKJFKUbEn+CTzhVJqVgFBeTIHQIaVAJpATtrmLaegip1SemkBKSUaRPiMmeG6VEyhWxYlhMmK46Z2TTEBzASE7kgzmlQOoRsrA6TFlImWYgxQrTSn5K2cMrA4dYmRkuTMngkixllLACle5KztoRzqfUyZjShkPJaX085kDQHvJOYCupzjfldP+R8pRQLnmWLUdC16AAxbZZzEUgtkeCdFVy4mxI6Si3F2yEVWHGWAKFhyIR4oBWY2J3AcW0rhd-J55KXkLIYWi7ZoDYnxOJcy8Frz1n9OEZ07l+Kti7NFVgAp4qSWSulcCjCdz5WCsUd-JVWLVGyMqQAZQxXU3VBr8VckJca7ZZq9mUotaahltq6VWplbFB1LKCXWv5dS84+rSVpNdUKmJ1q5Uop9fiwNzrkVeqgAAcX9Ia61Pyo2QFjfG51RKk0pvxWSt8LyqVcszXS7N5gXmMvFQWt14blVKNkeWgNsTI1cpRlkoVWw5kJtkU2nlIqq1YHTY25tGrXlOp7Ta8Vnb8UBzbc60tKLx10oDsEiNHbo2WqNWOlddrrV9o0SjDdjrYl5p3Xut1oz2WWJnUm3dPKp0js5Uenli6R2esbceltmKz2QIOS+nlRayAXPXT++tsiAAKA7xHvpzZYxNXLQOppHdu1xsHN3OsPYhsDdjf0UovTB9DpjT2QdoSB3D218PFqRSBzRvr23iuA5RyVN7tWkAQ0iWj16D0UbY9ahtGjgOwqFRBsj2KaN8cHQJv97SQMifEcOxj1zJOrutdhnjUm7GVtky64T2zSPiY4fJyVbKCMYS-cph9sTg1Jt49sydty9N0qUHU7jiGVOmIUI+9TrbbNuu4DJj9GFQWafxTyHzhmQGoZY857avI6lKac6S7t6nHMseDHB9zIHkvIfg2lqjKGstZvtTR9LhagM0YAEopd84Y0r2XMtVf0+x2rdKgn5ZRcBsrkqxMUrvYhtrjXMMvOfTxnrbqF1+oa8N4LgmMLmZg0NoVAc+vkfFSVgAUgp510GNEre2WpirvbZFbfxdpilYXPAHcawZybPB9urcVfM67gGPX3clTtkL+ynvzq1btx273hsvcu1gVVKKzteYY19t5S2bt0u4AtkFG3XHA-439nTIDmOnch26rkbmwcnfOAjwdkRQevdeTFpEePxHFiOy85BP2W28Am8j7+A34fo5bWsupxnmcPph356bm2WeDqCdzm+S3-xrZHXD0nou8tbv21Lor1qcdQBK3LitzWk3K8486rrkvNdPtl7r9THOdf0eK0Dk1dKOtU-2+bt1lvLGo9xzboV9PjvW+q+pknp2nf47u0t735O+Vu7DaNs3PKLsM++370z1rAfq-954u3ILEte55YnnV4q9W+nK0TiXnhM-Z-+1YjPWe6sK9kfn0v07y8l8a4Twv2u8817dcgwPxeHvOqN43nlSOKW89cRXxrPeXmx65QP4bdeI-J-OHq4DBeI+5+n7Pw75qM9L8a2nxQ5e1-Dfi19z3i-tn2etQ3g-+K+Ct5RTP7Z3Ah+WM76fi3t-IF96RFf01T+VVb+21jnPU+oBv7pUjA-xAQX3-23xbSlTqQdzAJ5QUBdyp0V0gAAOb0x2iy-2e2AO-hPxgInVSQTSZ1f3AMHQDi5HDwpS2HvxwPnUiA32-hfzzyIPESUB-0LyjHQLswJ0JT-yQMYLsW4ADkwKgVAJ4Ov0jHgPt2gJEMC3Py3UQOQP41IKZEsF1A0AZGUCAA/view">Clique aqui para abrir gráfico interativo</a>

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
