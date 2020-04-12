title: Covid-19 cases in Brazil
date: 2020-04-12 06:00
authors: Fernando Hannaka
comments: true
slug: altair-interactive
tags: covid19, coronavirus, brazil, python, altair, vega, interactive
include: vega

# Visualização de dados relacionados ao COVID-19 no Brasil
Visando entender o comportamento da evolução da COVID-19 no Brasil, esta página apresenta o ritmo de aceleração ou desaceleração da doença por estado brasileiro. A inspiração para criação desta visualização veio a partir do gráfico publicado pela organização [Our World in Data] (https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death) que tem como objetivo apresentar não somente o número de casos mas também o ritmo no qual as morte estão ocorrendo.

## Sobre os dados 
É importante salientar que esta visualização está baseado em dados disponibilizados pelas secretarias estaduais, coletados de forma manual uma vez que não há um banco de dados integrados, conforme site [Brasil.io] (https://brasil.io/dataset/covid19/caso). São dados passível de erros e vieses portanto qualquer análise não deve ser baseada somente nestes dados e toda tomada de decisões deve considerar uma análise científica com informações complementares.

## Número de mortes por estado brasileiro a partir da 5a morte notificada

[Open the Chart in the Vega Editor](https://vega.github.io/editor/#/url/vega-lite/N4KABGBEDGD2B2AzAlgc0gLjMSA3ZApgO6bYwIAuy8ArrDQM4DqyAJhQBakAsADLwBooceFVr0GACQJoOFUgGZ+AX2UDwUADYBDAJ4EATqQDaGiKAiWoAW20GA1qRwVdABwKlIm6h6GRYrtrQyC6kvAB0AOx+DBQGsPYELOxcWNxqZpaQBPBwrNToWBZWWXCasEZFmSXCCPlUCE7VNVAu7p7wsNbU2pqQ6i0lkCgEmqyesdoUvs01kAyjBNAN8BOLyxX8AIyQs5YZgxB4vTQeWF6yFKgGeruDBy2QAB5OkG1nUACONNqiIVPIXC+KAjMaeAAitwec10TUOrTcH0g31+VAoAKB-T2R1B43O4IIUw4DCx8Pm0F6H2ciM85XQyj2DJq0KyHBkqDkpAAbABWQTNebrFavBaaJYUTa8HZFN4084MApi-ogwhjElYYzzdHTSAAXVUAyGaKV5wAKrB0ZowKwCGBrBVpgwwCIUAZbKxtE73OUwABhADyADUAJLggC0WwAnGBXBUwARJqxYGAAEY3BVi5DxEmGqyQIhsTikAAc-EyLOKedsDle71pPmV-kCwVCWAi0SgsXiiWSRbSLKOOTyBThjzKFVrcqgnW68F6jdxE21HgHWQCQRCsJluBOHwiPNXRwlsE0VFcJmxZDr5xnPT6fkX8uXkEPlmp7RvXTvC9VeKgADltGsFc9l1XMhheGVry+H4-m1QFgWGX8IShcC8y3bBL1lD8YNRf4qExNChkfKACSJHMsIYCkTSvKcvFgelGWaVdIDZS5uT5Ii3hCGjIHNS1rVte0DEdZ0EFdd1PRjUZkwDENwyjGM4wTdEk1TdNkEzbNSSNG54AYRAKmsEwcBQU9DBFIVkEaeUhUlHZVDAgUCxSEsyysCsBWrRwoLo6YnnkPxejQVZzjFRBAqgVhILAHkYmQAAvD4tl4Fih1gfJ4EKTDBnIcpKlonDIFvOd7xVUY-y1KZELFVAcj-WhNE0V83gIALJyKkr5wfZCn2ql8iKOGLK0eaDkVgtEMRmMltFQa4CFQfrzlsF5BqybQnmQdUrx4pFwWQKTtBjOwqAMa0jp5I7hOmMBOnjRNYAGrCSMgSFYUZNbIAwka5jGlE4KmnTctm+bFp1GU7FQFaUNhV8jg2rba12zwAFkHQTMSkCzSSnQACgTaijrpOwAFuKG6CkAEonrJF6yM4EkmOZLi2I5eQsF5flfuRs0LV6QS7XRp0XWx7QPS9GS-SDUMI2jWMzpUsXkzTT1NJkbSuLiX4DKMkykPMgqcFFcVrNCzs7IMbYX2UJy5hcvswFLXhyw0W2oqmbRXjnYDPA9dEwwAJl4SJIxTBQeUiBQFEQFMtmLUtuCUSNI1YEPWClXgCF5FMaagAASKi2VsTw5AoVwGAwAB6SugUW8JUBCDgaBTcJrMrwuCFsGuFu0MNvGmGvuHCYtwi2cIACsGEaQ1ID9z0CAobaRtnj3A+D0Pw8j6PY-j3hE94ZPU5TjOs55HONWaHA3rCGJn3OABBFHG3p4lSEiVcr9uLAtlvpaoEf5+hIGakC2AHD+r0v5gADr-cG-8n5+BfttLYB4iKfwwgoGBSIAEIKAa-b+kZwHXzSJgzw2DSK4O2gHBQhDIFxU7HfOBgDyKKFSqgiBGEuQkIfvA8hzC0isMvuwt+XDGE4L4bFARNQ0ElhEZAMhr0KGkD5DQjCgh6F-0gAAIXvkw4BHMVEgNkdo3ReCwDvzYUQqBRidFiL0WAAhFjIEYPUbArRNjeF2JSgY4hLikTGNsaYrY6RHEYToVVVx-iPGBOLN4sAnDfGeEiQo8RUZYkdnCX49xyTPEOMEZY4s1iTFINyVIoRbZZG+gAKJFKUbEn+CTzhVJqVgFBeTIHQIaVAJpATtrmLaegip1SemkBKSUaRPiMmeG6VEyhWxYlhMmK46Z2TTEBzASE7kgzmlQOoRsrA6TFlImWYgxQrTSn5K2cMrA4dYmRkuTMngkixllLACle5KztoRzqfUyZjShkPJaX085kDQHvJOYCupzjfldP+R8pRQLnmWLUdC16AAxbZZzEUgtkeCdFVy4mxI6Si3F2yEVWHGWAKFhyIR4oBWY2J3AcW0rhd-J55KXkLIYWi7ZoDYnxOJcy8Frz1n9OEZ07l+Kti7NFVgAp4qSWSulcCjCdz5WCsUd-JVWLVGyMqQAZQxXU3VBr8VckJca7ZZq9mUotaahltq6VWplbFB1LKCXWv5dS84+rSVpNdUKmJ1q5Uop9fiwNzrkVeqgAAcX9Ia61Pyo2QFjfG51RKk0pvxWSt8LyqVcszXS7N5gXmMvFQWt14blVKNkeWgNsTI1cpRlkoVWw5kJtkU2nlIqq1YHTY25tGrXlOp7Ta8Vnb8UBzbc60tKLx10oDsEiNHbo2WqNWOlddrrV9o0SjDdjrYl5p3Xut1oz2WWJnUm3dPKp0js5Uenli6R2esbceltmKz2QIOS+nlRayAXPXT++tsiAAKA7xHvpzZYxNXLQOppHdu1xsHN3OsPYhsDdjf0UovTB9DpjT2QdoSB3D218PFqRSBzRvr23iuA5RyVN7tWkAQ0iWj16D0UbY9ahtGjgOwqFRBsj2KaN8cHQJv97SQMifEcOxj1zJOrutdhnjUm7GVtky64T2zSPiY4fJyVbKCMYS-cph9sTg1Jt49sydty9N0qUHU7jiGVOmIUI+9TrbbNuu4DJj9GFQWafxTyHzhmQGoZY857avI6lKac6S7t6nHMseDHB9zIHkvIfg2lqjKGstZvtTR9LhagM0YAEopd84Y0r2XMtVf0+x2rdKgn5ZRcBsrkqxMUrvYhtrjXMMvOfTxnrbqF1+oa8N4LgmMLmZg0NoVAc+vkfFSVgAUgp510GNEre2WpirvbZFbfxdpilYXPAHcawZybPB9urcVfM67gGPX3clTtkL+ynvzq1btx273hsvcu1gVVKKzteYY19t5S2bt0u4AtkFG3XHA-439nTIDmOnch26rkbmwcnfOAjwdkRQevdeTFpEePxHFiOy85BP2W28Am8j7+A34fo5bWsupxnmcPph356bm2WeDqCdzm+S3-xrZHXD0nou8tbv21Lor1qcdQBK3LitzWk3K8486rrkvNdPtl7r9THOdf0eK0Dk1dKOtU-2+bt1lvLGo9xzboV9PjvW+q+pknp2nf47u0t735O+Vu7DaNs3PKLsM++370z1rAfq-954u3ILEte55YnnV4q9W+nK0TiXnhM-Z-+1YjPWe6sK9kfn0v07y8l8a4Twv2u8817dcgwPxeHvOqN43nlSOKW89cRXxrPeXmx65QP4bdeI-J-OHq4DBeI+5+n7Pw75qM9L8a2nxQ5e1-Dfi19z3i-tn2etQ3g-+K+Ct5RTP7Z3Ah+WM76fi3t-IF96RFf01T+VVb+21jnPU+oBv7pUjA-xAQX3-23xbSlTqQdzAJ5QUBdyp0V0gAAOb0x2iy-2e2AO-hPxgInVSQTSZ1f3AMHQDi5HDwpS2HvxwPnUiA32-hfzzyIPESUB-0LyjHQLswJ0JT-yQMYLsW4ADkwKgVAJ4Ov0jHgPt2gJEMC3Py3UQOQP41IKZEsF1A0AZGUCAA)






<div id="vis00"></div>
<script type="text/javascript">
var spec00 = {
  "config": {
    "view": {
      "continuousWidth": 400,
      "continuousHeight": 300
    }
  },
  "layer": [
    {
      "mark": {
        "type": "line",
        "opacity": 0.7,
        "strokeWidth": 4
      },
      "encoding": {
        "color": {
          "condition": {
            "type": "nominal",
            "field": "state",
            "selection": "selector001"
          },
          "value": "lightgray"
        },
        "x": {
          "type": "quantitative",
          "field": "Day"
        },
        "y": {
          "type": "quantitative",
          "field": "Deaths",
          "scale": {
            "type": "log"
          }
        }
      },
      "height": 650,
      "selection": {
        "selector001": {
          "type": "single",
          "fields": [
            "state"
          ]
        }
      },
      "title": "Total de mortes confirmadas pelo COVID-19 por estado brasileiros",
      "width": 800
    },
    {
      "mark": {
        "type": "line",
        "opacity": 0.7,
        "strokeWidth": 4
      },
      "encoding": {
        "color": {
          "type": "nominal",
          "field": "state"
        },
        "opacity": {
          "value": 0.5
        },
        "tooltip": [
          {
            "type": "nominal",
            "field": "state"
          },
          {
            "type": "nominal",
            "field": "Name"
          }
        ],
        "x": {
          "type": "quantitative",
          "field": "Day"
        },
        "y": {
          "type": "quantitative",
          "field": "Deaths",
          "scale": {
            "type": "log"
          }
        }
      },
      "height": 650,
      "title": "Total de mortes confirmadas pelo COVID-19 por estado brasileiros",
      "transform": [
        {
          "filter": {
            "selection": "selector001"
          }
        }
      ],
      "width": 800
    },
    {
      "mark": {
        "type": "text",
        "align": "left",
        "dx": 5,
        "size": 10
      },
      "encoding": {
        "color": {
          "type": "nominal",
          "field": "state",
          "legend": null
        },
        "text": {
          "type": "nominal",
          "field": "state"
        },
        "x": {
          "type": "quantitative",
          "aggregate": "max",
          "axis": {
            "title": "Dias a partir da 5a morte no estado"
          },
          "field": "Day"
        },
        "y": {
          "type": "quantitative",
          "aggregate": {
            "argmax": "Day"
          },
          "axis": {
            "title": "Mortes confirmadas (escala logarítmica)"
          },
          "field": "Deaths"
        }
      },
      "height": 650,
      "title": "Total de mortes confirmadas pelo COVID-19 por estado brasileiros",
      "transform": [
        {
          "filter": {
            "selection": "selector001"
          }
        }
      ],
      "width": 800
    }
  ],
  "data": {
    "name": "data-2079b35733fb188043099d79d010e65b"
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v4.8.1.json",
  "datasets": {
    "data-2079b35733fb188043099d79d010e65b": [
      {
        "Day": 0,
        "state": "AM",
        "Deaths": 7
      },
      {
        "Day": 1,
        "state": "AM",
        "Deaths": 12
      },
      {
        "Day": 2,
        "state": "AM",
        "Deaths": 15
      },
      {
        "Day": 3,
        "state": "AM",
        "Deaths": 19
      },
      {
        "Day": 4,
        "state": "AM",
        "Deaths": 23
      },
      {
        "Day": 5,
        "state": "AM",
        "Deaths": 30
      },
      {
        "Day": 6,
        "state": "AM",
        "Deaths": 40
      },
      {
        "Day": 7,
        "state": "AM",
        "Deaths": 50
      },
      {
        "Day": 8,
        "state": "AM",
        "Deaths": 50
      },
      {
        "Day": 0,
        "state": "BA",
        "Deaths": 6
      },
      {
        "Day": 1,
        "state": "BA",
        "Deaths": 7
      },
      {
        "Day": 2,
        "state": "BA",
        "Deaths": 9
      },
      {
        "Day": 3,
        "state": "BA",
        "Deaths": 10
      },
      {
        "Day": 4,
        "state": "BA",
        "Deaths": 14
      },
      {
        "Day": 5,
        "state": "BA",
        "Deaths": 18
      },
      {
        "Day": 6,
        "state": "BA",
        "Deaths": 19
      },
      {
        "Day": 7,
        "state": "BA",
        "Deaths": 19
      },
      {
        "Day": 8,
        "state": "BA",
        "Deaths": 19
      },
      {
        "Day": 0,
        "state": "CE",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "CE",
        "Deaths": 5
      },
      {
        "Day": 2,
        "state": "CE",
        "Deaths": 7
      },
      {
        "Day": 3,
        "state": "CE",
        "Deaths": 9
      },
      {
        "Day": 4,
        "state": "CE",
        "Deaths": 21
      },
      {
        "Day": 5,
        "state": "CE",
        "Deaths": 22
      },
      {
        "Day": 6,
        "state": "CE",
        "Deaths": 23
      },
      {
        "Day": 7,
        "state": "CE",
        "Deaths": 35
      },
      {
        "Day": 8,
        "state": "CE",
        "Deaths": 35
      },
      {
        "Day": 9,
        "state": "CE",
        "Deaths": 40
      },
      {
        "Day": 10,
        "state": "CE",
        "Deaths": 57
      },
      {
        "Day": 11,
        "state": "CE",
        "Deaths": 57
      },
      {
        "Day": 12,
        "state": "CE",
        "Deaths": 57
      },
      {
        "Day": 13,
        "state": "CE",
        "Deaths": 57
      },
      {
        "Day": 0,
        "state": "DF",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "DF",
        "Deaths": 6
      },
      {
        "Day": 2,
        "state": "DF",
        "Deaths": 7
      },
      {
        "Day": 3,
        "state": "DF",
        "Deaths": 7
      },
      {
        "Day": 4,
        "state": "DF",
        "Deaths": 10
      },
      {
        "Day": 5,
        "state": "DF",
        "Deaths": 12
      },
      {
        "Day": 6,
        "state": "DF",
        "Deaths": 12
      },
      {
        "Day": 7,
        "state": "DF",
        "Deaths": 13
      },
      {
        "Day": 8,
        "state": "DF",
        "Deaths": 13
      },
      {
        "Day": 9,
        "state": "DF",
        "Deaths": 13
      },
      {
        "Day": 0,
        "state": "ES",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "ES",
        "Deaths": 6
      },
      {
        "Day": 2,
        "state": "ES",
        "Deaths": 6
      },
      {
        "Day": 3,
        "state": "ES",
        "Deaths": 6
      },
      {
        "Day": 4,
        "state": "ES",
        "Deaths": 6
      },
      {
        "Day": 5,
        "state": "ES",
        "Deaths": 6
      },
      {
        "Day": 6,
        "state": "ES",
        "Deaths": 7
      },
      {
        "Day": 7,
        "state": "ES",
        "Deaths": 8
      },
      {
        "Day": 8,
        "state": "ES",
        "Deaths": 8
      },
      {
        "Day": 0,
        "state": "GO",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "GO",
        "Deaths": 5
      },
      {
        "Day": 2,
        "state": "GO",
        "Deaths": 7
      },
      {
        "Day": 3,
        "state": "GO",
        "Deaths": 7
      },
      {
        "Day": 4,
        "state": "GO",
        "Deaths": 8
      },
      {
        "Day": 5,
        "state": "GO",
        "Deaths": 8
      },
      {
        "Day": 0,
        "state": "MA",
        "Deaths": 11
      },
      {
        "Day": 1,
        "state": "MA",
        "Deaths": 12
      },
      {
        "Day": 2,
        "state": "MA",
        "Deaths": 16
      },
      {
        "Day": 3,
        "state": "MA",
        "Deaths": 21
      },
      {
        "Day": 4,
        "state": "MA",
        "Deaths": 24
      },
      {
        "Day": 0,
        "state": "MG",
        "Deaths": 6
      },
      {
        "Day": 1,
        "state": "MG",
        "Deaths": 6
      },
      {
        "Day": 2,
        "state": "MG",
        "Deaths": 6
      },
      {
        "Day": 3,
        "state": "MG",
        "Deaths": 9
      },
      {
        "Day": 4,
        "state": "MG",
        "Deaths": 11
      },
      {
        "Day": 5,
        "state": "MG",
        "Deaths": 14
      },
      {
        "Day": 6,
        "state": "MG",
        "Deaths": 15
      },
      {
        "Day": 7,
        "state": "MG",
        "Deaths": 17
      },
      {
        "Day": 8,
        "state": "MG",
        "Deaths": 17
      },
      {
        "Day": 0,
        "state": "PA",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "PA",
        "Deaths": 5
      },
      {
        "Day": 2,
        "state": "PA",
        "Deaths": 6
      },
      {
        "Day": 3,
        "state": "PA",
        "Deaths": 7
      },
      {
        "Day": 4,
        "state": "PA",
        "Deaths": 9
      },
      {
        "Day": 5,
        "state": "PA",
        "Deaths": 9
      },
      {
        "Day": 0,
        "state": "PB",
        "Deaths": 7
      },
      {
        "Day": 1,
        "state": "PB",
        "Deaths": 11
      },
      {
        "Day": 2,
        "state": "PB",
        "Deaths": 11
      },
      {
        "Day": 3,
        "state": "PB",
        "Deaths": 11
      },
      {
        "Day": 0,
        "state": "PE",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "PE",
        "Deaths": 5
      },
      {
        "Day": 2,
        "state": "PE",
        "Deaths": 6
      },
      {
        "Day": 3,
        "state": "PE",
        "Deaths": 6
      },
      {
        "Day": 4,
        "state": "PE",
        "Deaths": 8
      },
      {
        "Day": 5,
        "state": "PE",
        "Deaths": 9
      },
      {
        "Day": 6,
        "state": "PE",
        "Deaths": 10
      },
      {
        "Day": 7,
        "state": "PE",
        "Deaths": 14
      },
      {
        "Day": 8,
        "state": "PE",
        "Deaths": 21
      },
      {
        "Day": 9,
        "state": "PE",
        "Deaths": 30
      },
      {
        "Day": 10,
        "state": "PE",
        "Deaths": 34
      },
      {
        "Day": 11,
        "state": "PE",
        "Deaths": 46
      },
      {
        "Day": 12,
        "state": "PE",
        "Deaths": 56
      },
      {
        "Day": 13,
        "state": "PE",
        "Deaths": 65
      },
      {
        "Day": 14,
        "state": "PE",
        "Deaths": 72
      },
      {
        "Day": 0,
        "state": "PI",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "PI",
        "Deaths": 6
      },
      {
        "Day": 2,
        "state": "PI",
        "Deaths": 7
      },
      {
        "Day": 3,
        "state": "PI",
        "Deaths": 7
      },
      {
        "Day": 4,
        "state": "PI",
        "Deaths": 7
      },
      {
        "Day": 0,
        "state": "PR",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "PR",
        "Deaths": 7
      },
      {
        "Day": 2,
        "state": "PR",
        "Deaths": 10
      },
      {
        "Day": 3,
        "state": "PR",
        "Deaths": 14
      },
      {
        "Day": 4,
        "state": "PR",
        "Deaths": 15
      },
      {
        "Day": 5,
        "state": "PR",
        "Deaths": 17
      },
      {
        "Day": 6,
        "state": "PR",
        "Deaths": 24
      },
      {
        "Day": 7,
        "state": "PR",
        "Deaths": 26
      },
      {
        "Day": 8,
        "state": "PR",
        "Deaths": 27
      },
      {
        "Day": 0,
        "state": "RJ",
        "Deaths": 6
      },
      {
        "Day": 1,
        "state": "RJ",
        "Deaths": 8
      },
      {
        "Day": 2,
        "state": "RJ",
        "Deaths": 9
      },
      {
        "Day": 3,
        "state": "RJ",
        "Deaths": 10
      },
      {
        "Day": 4,
        "state": "RJ",
        "Deaths": 13
      },
      {
        "Day": 5,
        "state": "RJ",
        "Deaths": 17
      },
      {
        "Day": 6,
        "state": "RJ",
        "Deaths": 18
      },
      {
        "Day": 7,
        "state": "RJ",
        "Deaths": 23
      },
      {
        "Day": 8,
        "state": "RJ",
        "Deaths": 28
      },
      {
        "Day": 9,
        "state": "RJ",
        "Deaths": 41
      },
      {
        "Day": 10,
        "state": "RJ",
        "Deaths": 47
      },
      {
        "Day": 11,
        "state": "RJ",
        "Deaths": 58
      },
      {
        "Day": 12,
        "state": "RJ",
        "Deaths": 64
      },
      {
        "Day": 13,
        "state": "RJ",
        "Deaths": 71
      },
      {
        "Day": 14,
        "state": "RJ",
        "Deaths": 89
      },
      {
        "Day": 15,
        "state": "RJ",
        "Deaths": 106
      },
      {
        "Day": 16,
        "state": "RJ",
        "Deaths": 122
      },
      {
        "Day": 17,
        "state": "RJ",
        "Deaths": 147
      },
      {
        "Day": 18,
        "state": "RJ",
        "Deaths": 147
      },
      {
        "Day": 0,
        "state": "RN",
        "Deaths": 6
      },
      {
        "Day": 1,
        "state": "RN",
        "Deaths": 7
      },
      {
        "Day": 2,
        "state": "RN",
        "Deaths": 7
      },
      {
        "Day": 3,
        "state": "RN",
        "Deaths": 8
      },
      {
        "Day": 4,
        "state": "RN",
        "Deaths": 11
      },
      {
        "Day": 5,
        "state": "RN",
        "Deaths": 11
      },
      {
        "Day": 6,
        "state": "RN",
        "Deaths": 11
      },
      {
        "Day": 7,
        "state": "RN",
        "Deaths": 11
      },
      {
        "Day": 0,
        "state": "RS",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "RS",
        "Deaths": 5
      },
      {
        "Day": 2,
        "state": "RS",
        "Deaths": 6
      },
      {
        "Day": 3,
        "state": "RS",
        "Deaths": 7
      },
      {
        "Day": 4,
        "state": "RS",
        "Deaths": 7
      },
      {
        "Day": 5,
        "state": "RS",
        "Deaths": 8
      },
      {
        "Day": 6,
        "state": "RS",
        "Deaths": 8
      },
      {
        "Day": 7,
        "state": "RS",
        "Deaths": 10
      },
      {
        "Day": 8,
        "state": "RS",
        "Deaths": 14
      },
      {
        "Day": 9,
        "state": "RS",
        "Deaths": 15
      },
      {
        "Day": 10,
        "state": "RS",
        "Deaths": 15
      },
      {
        "Day": 0,
        "state": "SC",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "SC",
        "Deaths": 5
      },
      {
        "Day": 2,
        "state": "SC",
        "Deaths": 10
      },
      {
        "Day": 3,
        "state": "SC",
        "Deaths": 10
      },
      {
        "Day": 4,
        "state": "SC",
        "Deaths": 11
      },
      {
        "Day": 5,
        "state": "SC",
        "Deaths": 15
      },
      {
        "Day": 6,
        "state": "SC",
        "Deaths": 17
      },
      {
        "Day": 7,
        "state": "SC",
        "Deaths": 18
      },
      {
        "Day": 8,
        "state": "SC",
        "Deaths": 18
      },
      {
        "Day": 9,
        "state": "SC",
        "Deaths": 21
      },
      {
        "Day": 0,
        "state": "SP",
        "Deaths": 5
      },
      {
        "Day": 1,
        "state": "SP",
        "Deaths": 9
      },
      {
        "Day": 2,
        "state": "SP",
        "Deaths": 15
      },
      {
        "Day": 3,
        "state": "SP",
        "Deaths": 22
      },
      {
        "Day": 4,
        "state": "SP",
        "Deaths": 30
      },
      {
        "Day": 5,
        "state": "SP",
        "Deaths": 40
      },
      {
        "Day": 6,
        "state": "SP",
        "Deaths": 48
      },
      {
        "Day": 7,
        "state": "SP",
        "Deaths": 58
      },
      {
        "Day": 8,
        "state": "SP",
        "Deaths": 68
      },
      {
        "Day": 9,
        "state": "SP",
        "Deaths": 84
      },
      {
        "Day": 10,
        "state": "SP",
        "Deaths": 98
      },
      {
        "Day": 11,
        "state": "SP",
        "Deaths": 113
      },
      {
        "Day": 12,
        "state": "SP",
        "Deaths": 136
      },
      {
        "Day": 13,
        "state": "SP",
        "Deaths": 164
      },
      {
        "Day": 14,
        "state": "SP",
        "Deaths": 188
      },
      {
        "Day": 15,
        "state": "SP",
        "Deaths": 219
      },
      {
        "Day": 16,
        "state": "SP",
        "Deaths": 260
      },
      {
        "Day": 17,
        "state": "SP",
        "Deaths": 275
      },
      {
        "Day": 18,
        "state": "SP",
        "Deaths": 304
      },
      {
        "Day": 19,
        "state": "SP",
        "Deaths": 371
      },
      {
        "Day": 20,
        "state": "SP",
        "Deaths": 428
      },
      {
        "Day": 21,
        "state": "SP",
        "Deaths": 496
      },
      {
        "Day": 22,
        "state": "SP",
        "Deaths": 540
      },
      {
        "Day": 23,
        "state": "SP",
        "Deaths": 560
      }
    ]
  }
};
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
O único tratamento nos dados originais foi o preenchimento de dados faltantes, provavelmente devido a falta de disponibilidade do dado pela secretaria em um determinado dia, porém é algo que não acontece com frequência. Os dados pendentes foram preenchidos com o mesmo total de casos de mortes válido antes daquele dia para aquele estado. Normalmente estes dados faltantes ocorrem nos dias mais recentes portanto para fins de visualização não foram considerados os últimos 3 dias, para permitir a obtenção completa dos dados antes de serem apresentados. Como o intuito deste gráfico é mostrar a tendência é importante termos os dados completos para não tirarmos conclusões precipitadas.

## Referências

* [Brasil.io] (https://brasil.io/dataset/covid19/caso)
* [Our World in Data] (https://ourworldindata.org/grapher/covid-confirmed-deaths-since-5th-death) 
* [DataCamp Live Coding: Covid-19 Exploratory Data Analysis] (https://www.facebook.com/726282547396228/videos/861466570947781/)
* [Altair: Interactive Plots on the Web] (https://matthewkudija.com/blog/2018/06/22/altair-interactive/)

---

- *O notebook original para geração desta visualização pode ser acessado aqui: [Jupyter Notebook](https://github.com/fehann/covid19brazil/blob/master/Covid19EstadosBrasileiros.ipynb) that was used to generate these examples.*
- *Cuidem da saúde e da familia, colaborando vamos sair desta situação o mais breve possível.*
