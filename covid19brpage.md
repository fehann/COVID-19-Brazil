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

```python
import altair as alt
from vega_datasets import data

cars = data.cars.url

# define selection
click = alt.selection_multi(encodings=['color'])

# scatter plots of points
scatter = alt.Chart(cars).mark_circle().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    size=alt.Size('Cylinders:O',
        scale=alt.Scale(range=(20,100))
    ),
    color=alt.Color('Origin:N', legend=None),
    tooltip=['Name:N','Horsepower:Q','Miles_per_Gallon:Q',
             'Cylinders:O','Origin:N'],
).transform_filter(
    click
).interactive()

# legend
legend = alt.Chart(cars).mark_rect().encode(
    y=alt.Y('Origin:N', axis=alt.Axis(title='Select Origin')),
    color=alt.condition(click, 'Origin:N', 
                        alt.value('lightgray'), legend=None),
    size=alt.value(250)
).properties(
    selection=click
)

chart = (scatter | legend)
chart.save('cars-clickable-legend.html')
```

For about 3x the amount of code we get a lot more information and ease of exploring this data. By adding encodings for origin of manufacture (color) and size (number of cylinders) we can view more dimensions of the dataset. With the `.interactive()` method we can scroll on the chart to zoom in and out as well as pan around. By adding a "legend" (actually another chart with interactivity) we can click to highlight one or multiple origins while hiding the others.  

<div id="vis0"></div>
<script type="text/javascript">
var spec0 = {"config": {"view": {"width": 400, "height": 300}}, "hconcat": [{"data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"}, "mark": "circle", "encoding": {"color": {"type": "nominal", "field": "Origin", "legend": null}, "size": {"type": "ordinal", "field": "Cylinders", "scale": {"range": [20, 100]}}, "tooltip": [{"type": "nominal", "field": "Name"}, {"type": "quantitative", "field": "Horsepower"}, {"type": "quantitative", "field": "Miles_per_Gallon"}, {"type": "ordinal", "field": "Cylinders"}, {"type": "nominal", "field": "Origin"}], "x": {"type": "quantitative", "field": "Horsepower"}, "y": {"type": "quantitative", "field": "Miles_per_Gallon"}}, "selection": {"selector005": {"type": "interval", "bind": "scales", "encodings": ["x", "y"]}}, "transform": [{"filter": {"selection": "selector004"}}]}, {"data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"}, "mark": "rect", "encoding": {"color": {"condition": {"type": "nominal", "field": "Origin", "legend": null, "selection": "selector004"}, "value": "lightgray"}, "size": {"value": 250}, "y": {"type": "nominal", "axis": {"title": "Select Origin"}, "field": "Origin"}}, "selection": {"selector004": {"type": "multi", "encodings": ["color"]}}}], "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt0 = {"mode": "vega-lite"};

function showError(el0, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el0 = document.getElementById('vis0');
vegaEmbed("#vis0", spec0, embed_opt0)
.catch(error => showError(el0, error));
</script>


## Stocks Example

This next example visualizes stocks data over time with a helpful multiline tooltip (original examples [here](https://altair-viz.github.io/gallery/multi_series_line.html) and [here](https://altair-viz.github.io/gallery/multiline_tooltip.html)). 

```python
import altair as alt
# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['date'], empty='none')

# The basic line
line = alt.Chart().mark_line(interpolate='basis').encode(
    alt.X('date:T', axis=alt.Axis(title='')),
    alt.Y('price:Q', axis=alt.Axis(title='',format='$f')),
    color='symbol:N'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart().mark_point().encode(
    x='date:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'price:Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart().mark_rule(color='gray').encode(
    x='date:T',
).transform_filter(
    nearest
)

# Put the five layers into a chart and bind the data
stockChart = alt.layer(line, selectors, points, rules, text,
                       data='https://raw.githubusercontent.com/altair-viz/vega_datasets/master/vega_datasets/_data/stocks.csv', 
                       width=600, height=300,title='Stock History')
stockChart.save('stocks.html')
```

By layering a line chart, selection based on the points nearest our mouseover, and text/points/line to visualize the selected data we now have a visually appealing way to explore this stock history.


<div id="vis1"></div>
<script type="text/javascript">
var spec = {"config": {"view": {"width": 400, "height": 300}}, "layer": [{"mark": {"type": "line", "interpolate": "basis"}, "encoding": {"color": {"type": "nominal", "field": "symbol"}, "x": {"type": "temporal", "axis": {"title": ""}, "field": "date"}, "y": {"type": "quantitative", "axis": {"format": "$f", "title": ""}, "field": "price"}}}, {"mark": "point", "encoding": {"opacity": {"value": 0}, "x": {"type": "temporal", "field": "date"}}, "selection": {"selector006": {"type": "single", "nearest": true, "on": "mouseover", "fields": ["date"], "empty": "none"}}}, {"mark": "point", "encoding": {"color": {"type": "nominal", "field": "symbol"}, "opacity": {"condition": {"value": 1, "selection": "selector006"}, "value": 0}, "x": {"type": "temporal", "axis": {"title": ""}, "field": "date"}, "y": {"type": "quantitative", "axis": {"format": "$f", "title": ""}, "field": "price"}}}, {"mark": {"type": "rule", "color": "gray"}, "encoding": {"x": {"type": "temporal", "field": "date"}}, "transform": [{"filter": {"selection": "selector006"}}]}, {"mark": {"type": "text", "align": "left", "dx": 5, "dy": -5}, "encoding": {"color": {"type": "nominal", "field": "symbol"}, "text": {"condition": {"type": "quantitative", "field": "price", "selection": "selector006"}, "value": " "}, "x": {"type": "temporal", "axis": {"title": ""}, "field": "date"}, "y": {"type": "quantitative", "axis": {"format": "$f", "title": ""}, "field": "price"}}}], "data": {"url": "https://raw.githubusercontent.com/altair-viz/vega_datasets/master/vega_datasets/_data/stocks.csv"}, "height": 300, "title": "Stock History", "width": 600, "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt = {"mode": "vega-lite"};

function showError(el, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el = document.getElementById('vis');
vegaEmbed("#vis1", spec, embed_opt)
.catch(error => showError(el, error));
</script>



## Airports Example

Altair also supports [geographic projections](https://altair-viz.github.io/gallery/world_projections.html) to visualize geospatial data. 

```python
import altair as alt
from vega_datasets import data

states = alt.topo_feature(data.us_10m.url, feature='states')
airports = data.airports.url

# US states background
background = alt.Chart(states).mark_geoshape(
	fill='lightgray',
	stroke='white',
	).properties(
	width=800,
	height=500
	).project('albersUsa')

# airport positions on background
points = alt.Chart(airports).mark_circle().encode(
	longitude='longitude:Q',
	latitude='latitude:Q',
	size=alt.value(15),
	color=alt.value('#3377B3'),
	tooltip=['iata:N','name:N','city:N','state:N','latitude:Q','longitude:Q'],
	)

chart = (background + points)
chart.save('airports.html')
chart
```

In this example we extend the simple [airports example](https://altair-viz.github.io/gallery/airports.html) to include tooltips with additional information about the airport you hover over. (Another cool example to replicate in Altair is visualizing flights between each city in [this example](http://vega.github.io/vega-tutorials/airports/)).

<div id="vis2"></div>
<script type="text/javascript">
var spec2 = {"config": {"view": {"width": 400, "height": 300}}, "layer": [{"data": {"url": "https://vega.github.io/vega-datasets/data/us-10m.json", "format": {"feature": "states", "type": "topojson"}}, "mark": {"type": "geoshape", "fill": "lightgray", "stroke": "white"}, "height": 500, "projection": {"type": "albersUsa"}, "width": 800}, {"data": {"url": "https://vega.github.io/vega-datasets/data/airports.csv"}, "mark": "circle", "encoding": {"color": {"value": "#3377B3"}, "latitude": {"type": "quantitative", "field": "latitude"}, "longitude": {"type": "quantitative", "field": "longitude"}, "size": {"value": 15}, "tooltip": [{"type": "nominal", "field": "iata"}, {"type": "nominal", "field": "name"}, {"type": "nominal", "field": "city"}, {"type": "nominal", "field": "state"}, {"type": "quantitative", "field": "latitude"}, {"type": "quantitative", "field": "longitude"}]}}], "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt2 = {"mode": "vega-lite"};

function showError(el2, error){
el2.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el2 = document.getElementById('vis2');
vegaEmbed("#vis2", spec2, embed_opt2)
.catch(error => showError(el2, error));
</script>



## Birdstrikes Example

At this point you are probably thinking that these building blocks Altair provides are easy stepping stones to a full web dashboard. This example (based off the [Seattle weather example](https://altair-viz.github.io/gallery/seattle_weather_interactive.html)) shows how you can use selection in one chart to filter data in antoher. 


```python
import altair as alt 
from vega_datasets import data

color = alt.Color('Wildlife__Species:N')

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])

# Top panel is scatter plot of temperature vs time
points = alt.Chart().mark_circle().encode(
    alt.X('yearmonthdate(Flight_Date):T', axis=alt.Axis(title='Date')),
    alt.Y('Speed_IAS_in_knots:Q',
        axis=alt.Axis(title='Indicated Airspeed (kts)'),
    ),
    color=alt.condition(brush, color, alt.value('lightgray')),
    tooltip=['Airport__Name:N','Aircraft__Make_Model:N','Flight_Date:T',
            'When__Phase_of_flight:N','Wildlife__Species:N','Speed_IAS_in_knots:Q'],
).properties(
    width=600,
    height=300
).add_selection(
    brush
).transform_filter(
    click
)

# Bottom panel is a bar chart of species
bars = alt.Chart().mark_bar().encode(
    alt.Y('count()', scale=alt.Scale(type='log')),
    alt.X('Wildlife__Species:N', sort=alt.SortField(field='sort_order', 
            op='count', order='descending')),
    color=alt.condition(click, color, alt.value('lightgray')),
).transform_filter(
    brush
).properties(
    width=600,
).add_selection(
    click
)

alt.vconcat(points, bars,
    data=data.birdstrikes.url,
    title="Aircraft Birdstrikes: 1990-2003"
).save('birdstrikes.html')
```

By selecting one (click) or multiple (shift-click) species in the bar chart at the bottom, the scatter plot on top will update to show only those data points. You can also select a section on the time axis of the scatter plot and see how the distribution of species varies (note that we add the `yearmonthdate(Flight_Date)` property to enable this selection—thanks to Greg Schivley for [pointing this out](https://twitter.com/gschivley/status/1010239788581040130)). It's easy to see how adding more of these building blocks could produce a nice dashboard. 

<div id="vis3"></div>
<script type="text/javascript">
var spec3 = {"config": {"view": {"width": 400, "height": 300}}, "vconcat": [{"mark": "circle", "encoding": {"color": {"condition": {"type": "nominal", "field": "Wildlife__Species", "selection": "selector002"}, "value": "lightgray"}, "tooltip": [{"type": "nominal", "field": "Airport__Name"}, {"type": "nominal", "field": "Aircraft__Make_Model"}, {"type": "temporal", "field": "Flight_Date"}, {"type": "nominal", "field": "When__Phase_of_flight"}, {"type": "nominal", "field": "Wildlife__Species"}, {"type": "quantitative", "field": "Speed_IAS_in_knots"}], "x": {"type": "temporal", "axis": {"title": "Date"}, "field": "Flight_Date", "timeUnit": "yearmonthdate"}, "y": {"type": "quantitative", "axis": {"title": "Indicated Airspeed (kts)"}, "field": "Speed_IAS_in_knots"}}, "height": 300, "selection": {"selector002": {"type": "interval", "encodings": ["x"]}}, "transform": [{"filter": {"selection": "selector003"}}], "width": 600}, {"mark": "bar", "encoding": {"color": {"condition": {"type": "nominal", "field": "Wildlife__Species", "selection": "selector003"}, "value": "lightgray"}, "x": {"type": "nominal", "field": "Wildlife__Species", "sort": {"op": "count", "field": "sort_order", "order": "descending"}}, "y": {"type": "quantitative", "aggregate": "count", "scale": {"type": "log"}}}, "selection": {"selector003": {"type": "multi", "encodings": ["color"]}}, "transform": [{"filter": {"selection": "selector002"}}], "width": 600}], "data": {"url": "https://vega.github.io/vega-datasets/data/birdstrikes.json"}, "title": "Aircraft Birdstrikes: 1990-2003", "$schema": "https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt3 = {"mode": "vega-lite"};

function showError(el3, error){
el3.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el3 = document.getElementById('vis3');
vegaEmbed("#vis3", spec3, embed_opt3)
.catch(error => showError(el3, error));
</script>


Looking back at the examples above, we have seen some helpful capabilities built into Altair:
- Use [selectors](https://altair-viz.github.io/user_guide/selections.html) (`alt.selection_single`, `alt.selection_multi`, `alt.selection_interval`) to highlight data interactively.
- [Combine](https://altair-viz.github.io/user_guide/compound_charts.html) charts by layering or concatenation to show multiple views of the data.
- [Export](https://altair-viz.github.io/user_guide/saving_charts.html) charts in a variety of formats, including HTML for sharing on the web.



# Sharing Interactive Altair Charts on the Web

I was initially drawn to Altair because of this ease of use offered by the declarative approach to visualization. The further ability to easily generate and share interactive visualizations on the web makes it even more useful.

The simplest way to share an Altair plot on the web is to simply [export](https://altair-viz.github.io/user_guide/saving_charts.html) as html using `.save('chartName.html')`. This HTML file includes the Vega, Vega-Lite, and vegaEmbed scripts, a JSON specification of your chart, and the JavaScript needed for interactivity. This makes it easy to share a single chart. 

This blog is generated with Pelican, and as you can see above includes multiple interactive charts written in Altair. Below I walk through the process for including interactive Altair charts with Pelican.

## Pelican Template

Since we need to load some styling and the Vega, Vega-Lite, and vegaEmbed scripts on any page that includes an Altair chart, we will add these to the article template in `theme/templates/article.html`.

```html
{% if 'vega' in article.include %}
<style>
.vega-actions a {
	margin-right: 12px;
	color: #757575;
	font-weight: normal;
	font-size: 13px;
}
.error {
	color: red;
}
</style>
<script src="https://cdn.jsdelivr.net/npm//vega@3.3.1"></script>
<script src="https://cdn.jsdelivr.net/npm//vega-lite@2.4.3"></script>
<script src="https://cdn.jsdelivr.net/npm//vega-embed@3.11"></script>
{% endif %}
```

Now, whenever we add the `include: vega` tag at the top of an article's markdown file, these items will be included.


## Add a Single Plot

To add a single plot to an article, we open the `chartName.html` file we exported from Altair and copy the below portion which defines a `<div>` for our chart and contains the JSON specification and JavaScript for the chart. Note that when placing this into a markdown document we need to un-indent so Pelican can generate the page properly. 

```html
<div id="vis"></div>
<script type="text/javascript">
var spec = {"config":{"view":{"width":400,"height":300}},"data":{"url":"https://vega.github.io/vega-datasets/data/cars.json","format":{"type":"json"}},"mark":"point","encoding":{"x":{"type":"quantitative","field":"Horsepower"},"y":{"type":"quantitative","field":"Miles_per_Gallon"}},"$schema":"https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt = {"mode": "vega-lite"};

function showError(el, error){
el.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el = document.getElementById('vis1');
vegaEmbed("#vis", spec, embed_opt)
.catch(error => showError(el, error));
</script>
```

## Add Multiple Plots

As shown above it is entirely possible to add multiple visualizations to a single page, but you'll need to rename some variables to make them unique and allow the subsequent charts to render. I simply incremented the required variables (`vis`, `spec`, `el`, and `embed_opt`) so they are unique.

```html
<div id="vis2"></div>
<script type="text/javascript">
var spec2 = {"config":{"view":{"width":400,"height":300}},"data":{"url":"https://vega.github.io/vega-datasets/data/cars.json","format":{"type":"json"}},"mark":"point","encoding":{"x":{"type":"quantitative","field":"Horsepower"},"y":{"type":"quantitative","field":"Miles_per_Gallon"}},"$schema":"https://vega.github.io/schema/vega-lite/v2.4.3.json"};
var embed_opt2 = {"mode": "vega-lite"};

function showError(el2, error){
el2.innerHTML = ('<div class="error">'
+ '<p>JavaScript Error: ' + error.message + '</p>'
+ "<p>This usually means there's a typo in your chart specification. "
+ "See the javascript console for the full traceback.</p>"
+ '</div>');
throw error;
}
const el2 = document.getElementById('vis2');
vegaEmbed("#vis2", spec2, embed_opt2)
.catch(error => showError(el2, error));
</script>
```

Set up in this manner, generating your Pelican site will pull in the required external scripts, style, and then display your interactive visualizations. You can view the full [markdown file](https://raw.githubusercontent.com/mkudija/blog/master/content/articles/2018-06-11-altair-interactive.md) that generated the [HTML - ADD LINK]() of this post to see how it all fits together. 

# Closing Thoughts
A successful visualization is all about finding the right tool for the job. I'm increasingly convinced that if you want to quickly interact with your data or share it online Altair is a great option. I'm excited to learn more about Altair as more features are added. Thanks to Jake VanderPlas, Brian Granger, and all those who have contributed to Altair and the technologies it is built on.


# Resources:
- [Altair Docs](https://altair-viz.github.io/index.html)
- [Altair Tutorials](https://github.com/altair-viz/altair-tutorial/tree/master/notebooks)
- Example data to play with: [vega-datasets](https://github.com/vega/vega-datasets/tree/gh-pages/data)
- Jim Vallandingham's [Altair write-up](http://vallandingham.me/altair_intro.html)
- pbpython's [Altair write-up](http://pbpython.com/altair-intro.html)
- Jake VanderPlas' PyCon 2018 tutorial:
<div class="video-container">
        <iframe width="750" height="500" src="https://www.youtube.com/embed/ms29ZPUKxbU" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</div>



---

- *You can view the original [Jupyter Notebook](https://github.com/mkudija/General-Examples/blob/master/Altair/Altair-interactive.ipynb) that was used to generate these examples.*
- *All code examples in this notebook use Altair 2.1.0*
