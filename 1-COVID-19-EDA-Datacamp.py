#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Exploratory Data Analysis

# ## Context and introductory notes

# ### Reasons to give this tutorial and reasons to not

# This tutorial's purpose is to introduce people to the [2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19) and how to explore it using some foundational packages in the Scientific Python Data Science stack.
# 
# It is not intended to encourage people to create & publish their own data visualizations. In fact, as [this thoughtful essay](https://medium.com/nightingale/ten-considerations-before-you-create-another-chart-about-covid-19-27d3bd691be8) makes clear, in many cases it is irresponsible to publish amateur visualizations, which at best will dilute those that experts with domain expertise are publishing. We won't be making any predictions or doing any statistical modelling.
# 

# Firstly, why are we looking at the dataset from Johns Hopkins (JHU)? I recently asked twitter, which has wonderful epidemiology and data communities, "Which COVID-19 datasets are best to look at and why?"
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">data folk: which <a href="https://twitter.com/hashtag/Covid_19?src=hash&amp;ref_src=twsrc%5Etfw">#Covid_19</a> datasets should we be looking at (and directing people towards) and why?</p>&mdash; Hugo Bowne-Anderson (@hugobowne) <a href="https://twitter.com/hugobowne/status/1247013362988240896?ref_src=twsrc%5Etfw">April 6, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# There were many thoughtful responses and I encourage you to look through them. [Ellie Murray](https://scholar.harvard.edu/eleanormurray/home), an epidemiologist and Assistant Professor at the Boston University School of Public Health, responded
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">What purposes are you directing people towards data for? All the data we have are incomplete, so the goal of the data should inform which data to use</p>&mdash; Ellie Murray (@EpiEllie) <a href="https://twitter.com/EpiEllie/status/1247321239292706817?ref_src=twsrc%5Etfw">April 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# to which I replied
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Great question. I&#39;m a data science educator interested in directing people more generally to the best resources &amp; ways to think about them so that they have a stronger sense of what&#39;s actually happening in such a confusing time, e.g. my tweet below 1/ <a href="https://t.co/6lGPbDAZL5">https://t.co/6lGPbDAZL5</a></p>&mdash; Hugo Bowne-Anderson (@hugobowne) <a href="https://twitter.com/hugobowne/status/1247322357863034880?ref_src=twsrc%5Etfw">April 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# This is the tweet I was referencing
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">even how to just think about the data generating process -- e.g. number of reported cases a function of number of tests, willingness of govts to reports, in addition to number of actual cases. there&#39;s also censoring, lag, &amp; much more. cc <a href="https://twitter.com/ericmjl?ref_src=twsrc%5Etfw">@ericmjl</a> <a href="https://twitter.com/jsbois?ref_src=twsrc%5Etfw">@jsbois</a></p>&mdash; Hugo Bowne-Anderson (@hugobowne) <a href="https://twitter.com/hugobowne/status/1247321297987620864?ref_src=twsrc%5Etfw">April 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# Ellie replied
# 
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">In that case, I agree with the other responses: the Johns Hopkins data is probably the best general purpose dataset for education.</p>&mdash; Ellie Murray (@EpiEllie) <a href="https://twitter.com/EpiEllie/status/1247322941039300608?ref_src=twsrc%5Etfw">April 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# Once again, check out out the thread for further details, but the main reasons cited for using the JHU data are
# 
# - JHU is already a trusted and respected institution,
# - They cite many sources, which are themselves reputable,
# - The data is updated daily, and
# - It is provided in an easily digestible format (.csv in a github repository).
# 
# I also want to flag that, after all the responses that came in, I thought twice about whether to conduct this tutorial. The main reasons are summarized by Ellie's tweets here:
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">I definitely understand the desire of data-minded people to dig into learning about the covid data, but misunderstandings can add to the chaos &amp; complicate pandemic response. 1/2</p>&mdash; Ellie Murray (@EpiEllie) <a href="https://twitter.com/EpiEllie/status/1247324458479693824?ref_src=twsrc%5Etfw">April 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">My advice to learners is to use data from a historic epidemic—maybe swine flu. Then you also have the chance to see how well your predictions actually match with the epidemic trajectory, and there are more likely many resources to help understand the data. 2/2</p>&mdash; Ellie Murray (@EpiEllie) <a href="https://twitter.com/EpiEllie/status/1247324778014412811?ref_src=twsrc%5Etfw">April 7, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# I love the idea of looking at historical datasets and hope to do this in the future. The reason I've decided to continue with this tutorial is that I feel that, as long as we take our results with **very, very many grains of salt**, it will help us 
# 
# - to interrogate the world as it currently is, 
# - to understand many of the biases in modern data collection, data analysis, and data reporting,
# - to develop more of a shared language to discuss it, even as non-experts, and
# - to learn about some of the contemporary tooling and data-analytic concepts that help us to work with data.
# 
# That all having been said, please do listen to the domain experts, the epidemiologists.

# ***
# ### Biases in data collection, data analysis, and data reporting
# 
# What type of biases am I talking about? A key example to keep in mind is when interpreting plots, numbers, and reports of the *known* number of cases of COVID-19, **know** that this is a function of many things that are *not* the total number of cases, such as **the number of available tests**. The limiting case is when there are zero tests, there are zero known cases; then if many tests become available, there'll seem to be a huge spike in number of cases, even if there hasn't been such a spike. 
# 
# Nate Silver's thread here gives a concrete example in Washington State:
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">THREAD:<br><br>Washington state is a good example of the importance of accounting for the number of tests when reporting COVID-19 case counts. Remember I mentioned a couple of days ago how their number of cases in WA had begun to stabilize? Well, guess what happened...</p>&mdash; Nate Silver (@NateSilver538) <a href="https://twitter.com/NateSilver538/status/1241113755016138755?ref_src=twsrc%5Etfw">March 20, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# and he also has an interesting article linked to in this tweet here:
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Hey y&#39;all. I have a deep dive today on how the number of *known coronavirus cases* isn&#39;t really a good way to know what&#39;s happening with the disease. Unless you know something about testing, anyway. Hope you&#39;ll check it out.<a href="https://t.co/VK7rCgBNMc">https://t.co/VK7rCgBNMc</a></p>&mdash; Nate Silver (@NateSilver538) <a href="https://twitter.com/NateSilver538/status/1246487881297920001?ref_src=twsrc%5Etfw">April 4, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# The number of reported known cases is **also a function of any given government's willingness (or lack thereof) to report their actual findings**. We can think both of these in relation to NNT's conception of [Wittgenstein's ruler](https://twitter.com/DellAnnaLuca/status/1244555177807380480):
# 
# > “Wittgenstein’s ruler: Unless you have confidence in the ruler’s reliability, if you use a ruler to measure a table you may also be using the table to measure the ruler.”
# 
# 
# 

# ***
# We'll be visualizing number of reported confirmed cases, deaths, and recoveries around the world. Note that there are interesting ways to report these numbers that aren't quite visualization per se. Ryan Struyck of CNN, for example, has been leveraging the affordances of tweets and twitter do display such data compellingly:
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Reported US coronavirus cases<br><br>3/17: 6,135<br>3/18: 8,760<br>3/19: 13,229<br>3/20: 18,763<br>3/21: 25,740<br>3/22: 34,276<br>3/23: 42,663<br>3/24: 52,976<br>3/25: 65,273<br>3/26: 82,135<br>3/27: 101,295<br>3/28: 121,176<br>3/29: 139,773<br>3/30: 160,377<br>3/31: 185,469<br>4/1: 211,740<br>4/2: 245,070<br>4/3: 277,953<br>Now: 311,544</p>&mdash; Ryan Struyk (@ryanstruyk) <a href="https://twitter.com/ryanstruyk/status/1246624017278263296?ref_src=twsrc%5Etfw">April 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

# Raymond Hettinger, one of my Pythonic heroes, tweeted in a similar vein:
# 
# <blockquote class="twitter-tweet"><p lang="en" dir="ltr">US covid-19 case count growth:<br><br>100 to 1,000 in 8 days<br>1,000 to 10,000 in 9 days<br>10,000 to 100,000 in 9 days<br><br>What is your best guess for 1,000,000?</p>&mdash; Raymond Hettinger (@raymondh) <a href="https://twitter.com/raymondh/status/1243643686602211328?ref_src=twsrc%5Etfw">March 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
# 
# From Raymond's tweet, it becomes clear why we will want to plot the growth curves with a logarithmic y-axis: so that the data is not all packed into a small region of the visualization. 
# 
# **ESSENTIAL POINT THAT WE'LL ALSO MAKE LATER:** A logarithm scale is good for visualization **BUT** remember, in the thoughtful words of [Justin Bois](http://bois.caltech.edu/), "on the ground, in the hospitals, we live with the linear scale. The flattening of the US curve, for example is more evident on the log scale, but the growth is still rapid on a linear scale, which is what we feel."

# I also want to remind people that exploratory data analysis and data visualization is about discovering things that exist and that are happening in the world. In this case, we are plotting data of **people** who are sick and dying **right now** so throughout the tutorial I'd encourage us all to have the patience and respect required in such a time.

# Before starting to look at the data, let's look at [the repository containing it](https://github.com/CSSEGISandData/COVID-19) to get a feel for the context.

# **Summary:** We've
# - discussed reasons to give this tutorial and provided warnings about doing so
# - discussed biases in data collection, data analyses, and data reporting,
# - had a look at the github repository containing the JHU COVID-19 dataset.

# ## Exploratory data analysis and visualization using Python

# ### Imports and data

# Let's import the necessary packages from the SciPy stack and get [the data](https://github.com/CSSEGISandData/COVID-19).

# In[1]:


# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Set style & figures inline
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Data urls
base_url = 'https://raw.githubusercontent.com/hugobowne/COVID-19-EDA-tutorial/master/csse_covid_19_data/csse_covid_19_time_series/'
confirmed_cases_data_url = base_url + 'time_series_covid19_confirmed_global.csv'
death_cases_data_url = base_url + 'time_series_covid19_deaths_global.csv'
recovery_cases_data_url = base_url+ 'time_series_covid19_recovered_global.csv'
# Import datasets as pandas dataframes
raw_data_confirmed = pd.read_csv(confirmed_cases_data_url)
raw_data_deaths = pd.read_csv(death_cases_data_url)
raw_data_recovered = pd.read_csv(recovery_cases_data_url)


# ### Confirmed cases of COVID-19

# We'll first check out the confirmed cases data by looking at the head of the dataframe:
# 

# In[5]:


raw_data_confirmed.head(n=10)


# **Discuss:** What do you see here?
# We can also see a lot about the data by using the `.info()` and `.describe()` dataframe methods:

# In[7]:


raw_data_confirmed.info()


# In[8]:


raw_data_confirmed.describe()


# **Discuss:** What do the above tell us?

# ### Number of confirmed cases by country

# Look at the head (or tail) of our dataframe again and notice that each row is the data for a particular *province* or *state* of a given country:

# In[ ]:


___


# We want the numbers for each country, though. So the way to think about this is, for each country, we want to take all the rows (*regions/provinces*) that correspond to that country and add up the numbers for each. To put this in data-analytic-speak, we want to **group by** the country column and sum up all the values for the other columns.
# 
# This is a common pattern in data analysis that we humans have been using for centuries. Interestingly, it was only formalized in 2011 by Hadley Wickham in his seminal paper [The Split-Apply-Combine Strategy for Data
# Analysis](https://www.jstatsoft.org/article/view/v040i01). The pattern we're discussing is now called Split-Apply-Combine and, in the case at hand, we
# 
# - Split the data into new datasets for each country,
# - Apply the function of "sum" for each new dataset (that is, we add/sum up the values for each column) to sum over territories/provinces/states for each country, and
# - Combine these datasets into a new dataframe.
# 
# The `pandas` API has the `groupby` method, which allows us to do this.
# 
# **Side note:** For more on split-apply-combine and `pandas` check out [my post here](https://www.datacamp.com/community/tutorials/pandas-split-apply-combine-groupby).

# In[11]:


# Group by region (also drop 'Lat', 'Long' as it doesn't make sense to sum them here)
confirmed_country = raw_data_confirmed.groupby(['Country/Region']).sum().drop(['Lat','Long'], axis = 1)
confirmed_country.head()


# So each row of our new dataframe `confirmed_country` is a time series of the number of confirmed cases for each country. Cool! 
# Now a dataframe has an associated object called an Index, which is essentially a set of unique indentifiers for each row. Let's check out the index of `confirmed_country`:

# In[13]:


confirmed_country.index


# It's indexed by `Country/Region`. That's all good **but** if we index by date **instead**, it will allow us to produce some visualizations almost immediately. This is a nice aspect of the `pandas` API: you can make basic visualizations with it and, if your index consists of DateTimes, it knows that you're plotting time series and plays nicely with them.
# To make the index the set of dates, notice that the column names are the dates. To turn column names into the index, we essentially want to make the columns the rows (and the rows the columns). This corresponds to taking the transpose of the dataframe:

# In[14]:


confirmed_country = confirmed_country.transpose()
confirmed_country.head()


# Let's have a look at our index to see whether it actually consists of DateTimes:

# In[15]:


confirmed_country.index


# Note that `dtype='object'`which means that these are strings, not DateTimes. We can use `pandas` to turn it into a DateTimeIndex:

# In[16]:


# Set index as DateTimeIndex
datetime_index = pd.DatetimeIndex(confirmed_country.index)
confirmed_country.set_index(datetime_index, inplace = True)
# Check out index
confirmed_country.index


# Now we have a DateTimeIndex and Countries for columns, we can use the dataframe plotting method to visualize the time series of confirmed number of cases by country. As there are so many coutries, we'll plot a subset of them:

# ### Plotting confirmed cases by country

# In[19]:


# Plot time series of several countries of interest
poi = ['China', 'US', 'Italy', 'France', 'Spain', 'Brazil']
confirmed_country[poi].plot(figsize=(20,10), linewidth = 5, colormap = 'brg', fontsize = 20)


# Let's label our axes and give the figure a title. We'll also thin the line and add points for the data so that the sampling is evident in our plots:

# In[20]:


# Plot time series of several countries of interest
confirmed_country[poi].plot(figsize=(20,10), linewidth = 2, marker = '2', colormap = 'brg', fontsize = 20)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Reported Confirmed cases count', fontsize=20);
plt.title('Reported Confirmed Cases Time Series', fontsize=20);


# Let's do this again but make the y-axis logarithmic:

# In[21]:


# Plot time series of several countries of interest
confirmed_country[poi].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy = True)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Reported Confirmed cases count', fontsize=20);
plt.title('Reported Confirmed Cases Time Series', fontsize=20);


# **Discuss:** Why do we plot with a log y-axis? How do we interpret the log plot?
# **Key points:** 
# - If a variable takes on values over several orders of magnitude (e.g. in the 10s, 100s, and 1000s), we use a log axes so that the data is not all crammed into a small region of the visualization.
# - If a curve is approximately linear on a log axis, then its approximately exponential growth and the gradient/slope of the line tells us about the exponent.
# 
# 
# **ESSENTIAL POINT:** A logarithm scale is good for visualization **BUT** remember, in the thoughtful words of [Justin Bois](http://bois.caltech.edu/), "on the ground, in the hospitals, we live with the linear scale. The flattening of the US curve, for example is more evident on the log scale, but the growth is still rapid on a linear scale, which is what we feel."

# **Summary:** We've 
# - looked at the JHU data repository and imported the data,
# - looked at the dataset containing the number of reported confirmed cases for each region,
# - wrangled the data to look at the number of reported confirmed cases by country,
# - plotted the number of reported confirmed cases by country (both log and semi-log),
# - discussed why log plots are important for visualization and that we need to remember that we, as humans, families, communities, and society, experience COVID-19 linearly.

# ### Number of reported deaths

# As we did above for `raw_data_confirmed`, let's check out the head and the info of the `raw_data_deaths` dataframe:

# In[22]:


raw_data_deaths.head()


# In[23]:


raw_data_deaths.info()


# It seems to be structured similarly to `raw_data_confirmed`. I have checked it out in detail and can confirm that it is! This is good data design as it means that users like can explore, munge, and visualize it in a fashion analogous to the above. Can you remember what we did? We
# 
# - Split-Apply-Combined it (and dropped 'Lat'/'Long'),
# - Transposed it,
# - Made the index a DateTimeIndex, and
# - Visualized it (linear and semi-log).
# 
# Let's now do the first three steps here for `raw_data_deaths` and see how we go:
# 
# 

# ### Number of reported deaths by country

# In[25]:


# Split-Apply-Combine
deaths_country = raw_data_deaths.groupby(['Country/Region']).sum().drop(['Lat','Long'], axis = 1)

# Transpose
deaths_country = deaths_country.transpose()

# Set index as DateTimeIndex
datetime_index = pd.DatetimeIndex(deaths_country.index)
deaths_country.set_index(datetime_index, inplace = True)

# Check out head
deaths_country.head()


# In[26]:


# Check out the index
deaths_country.index


# ### Plotting number of reported deaths by country 

# Let's now visualize the number of reported deaths:

# In[30]:


# Plot time series of several countries of interest
poi = ['China', 'US', 'Italy', 'France', 'Spain', 'Brazil']
deaths_country[poi].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Reported Deaths Time Series', fontsize=20);


# Now on a semi-log plot:

# In[29]:


# Plot time series of several countries of interest
poi = ['China', 'US', 'Italy', 'France', 'Spain', 'Brazil']
deaths_country[poi].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy = True)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Reported Deaths Time Series', fontsize=20);


# ### Aligning growth curves to start with day of number of known deaths ≥ 25

# To compare what's happening in different countries, we can align each country's growth curves to all start on the day when the number of known deaths ≥ 25, such as reported in the first figure [here](https://www.nytimes.com/interactive/2020/03/21/upshot/coronavirus-deaths-by-country.html).
# To achieve this, first off, let's set set all values less than 25 to NaN so that the associated data points don't get plotted at all when we visualize the data:

# In[33]:


# Loop over columns & set values < 25 to None
for col in deaths_country.columns:
    deaths_country.loc[(deaths_country[col] < 25), col] = None

# Check out tail
deaths_country.tail()


# Now let's plot as above to make sure we see what we think we should see:

# In[34]:


# Plot time series of several countries of interest
poi = ['China', 'US', 'Italy', 'France', 'Spain', 'Brazil']
deaths_country[poi].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20)
plt.xlabel('Date', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Reported Deaths Time Series', fontsize=20);


# The countries that have seen less than 25 total deaths will have columns of all NaNs now so let's drop these and then see how many columns we have left:

# In[35]:


# Drop columns that are all NaNs (i.e. countries that haven't yet reached 25 deaths)
deaths_country.dropna(axis = 1, how = "all", inplace = True)
deaths_country.info()


# As we're going to align the countries from the day they first had at least 25 deaths, we won't need the DateTimeIndex. In fact, we won't need the date at all. So we can 
# - Reset the Index, which will give us an ordinal index (which turns the date into a regular column) and
# - Drop the date column (which will be called 'index) after the reset.

# In[37]:


# reset index, drop date column
deaths_country_drop = deaths_country.reset_index().drop(['index'], axis = 1)
deaths_country_drop.head()


# Now it's time to shift each column so that the first entry is the first NaN value that it contains! To do this, we can use the `shift()` method on each column. How much do we shift each column, though? The magnitude of the shift is given by how many NaNs there are at the start of the column, which we can retrieve using the `first_valid_index()` method on the column **but** we want to shift **up**, which is negative in direction (by convention and perhaps intuition). SO let's do it.

# In[39]:


# shift
for col in deaths_country_drop.columns:
    deaths_country_drop[col] = deaths_country_drop[col].shift(-deaths_country_drop[col].first_valid_index())
# check out head
deaths_country_drop.head()


# **Side note:** instead of looping over columns, we could have applied a lambda function to the columns of the dataframe, as follows:

# In[ ]:


# shift using lambda function
#deaths_country = deaths_country.apply(lambda x: x.shift(-x.first_valid_index()))


# Now we get to plot our time series, first with linear axes, then semi-log:

# In[40]:


# Plot time series 
poi = ['China', 'US', 'Italy', 'France', 'Spain', 'Brazil']
deaths_country_drop[poi].plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20)
plt.xlabel('Days', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Total reported coronavirus deaths for places with at least 25 deaths', fontsize=20);


# In[42]:


# Plot semi log time series 
deaths_country_drop.plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy = True)
plt.xlabel('Days', fontsize=20);
plt.ylabel('Number of Reported Deaths', fontsize=20);
plt.title('Total reported coronavirus deaths for places with at least 25 deaths', fontsize=20);


# **Note:** although we have managed to plot what we wanted, the above plots are challenging to retrieve any meaningful information from. There are too many growth curves so that it's very crowded **and** too many colours look the same so it's difficult to tell which country is which from the legend. Below, we'll plot less curves and further down in the notebook we'll use the python package Altair to introduce interactivity into the plot in order to deal with this challenge.

# In[45]:


# Plot semi log time series 
ax = deaths_country_drop[poi].plot(figsize=(20,10), linewidth=2, marker='.', colormap = 'brg', fontsize=20, logy=True)
ax.legend(ncol=3, loc='upper right')
plt.xlabel('Days', fontsize=20);
plt.ylabel('Deaths Patients count', fontsize=20);
plt.title('Total reported coronavirus deaths for places with at least 25 deaths', fontsize=20);


# **Summary:** We've 
# - looked at the dataset containing the number of reported deaths for each region,
# - wrangled the data to look at the number of reported deaths by country,
# - plotted the number of reported deaths by country (both log and semi-log),
# - aligned growth curves to start with day of number of known deaths ≥ 25.

# ### Plotting number of recovered people

# The third dataset in the Hopkins repository is the number of recovered. We want to do similar data wrangling as in the two cases above so we *could* copy and paste our code again *but*, if you're writing the same code three times, it's likely time to write a function.

# In[ ]:


# Function for grouping countries by region
def group_by_country(raw_data):
    """Returns data for countries indexed by date"""
    # Group by
    data = ___
    # Transpose
    data = ___
    # Set index as DateTimeIndex
    datetime_index = ___
    data.set_index(datetime_index, inplace=True)
    return data


# In[ ]:


# Function to align growth curves
def align_curves(data, min_val):
    """Align growth curves  to start on the day when the number of known deaths = min_val"""
    # Loop over columns & set values < min_val to None
    for col in data.columns:
        ___
    # Drop columns with all NaNs
    ___
    # Reset index, drop date
    data = 
    # Shift each column to begin with first valid index
    for col in data.columns:
        data[col] = ___
    return data


# In[ ]:


# Function to plot time series
def plot_time_series(df, plot_title, x_label, y_label, logy=False):
    """Plot time series and make looks a bit nice"""
    ax = df.plot(figsize=(20,10), linewidth=2, marker='.', fontsize=20, logy=logy)
    ax.legend(ncol=3, loc='lower right')
    plt.xlabel(x_label, fontsize=20);
    plt.ylabel(y_label, fontsize=20);
    plt.title(plot_title, fontsize=20);


# For a sanity check, let's see these functions at work on the 'number of deaths' data:

# In[ ]:


___
___
___


# Now let's check use our functions to group, wrangle, and plot the recovered patients data:

# In[ ]:


# group by country and check out tail
recovered_country = ___
___


# In[ ]:


# align curves and check out head
recovered_country_drop = ___
___


# Plot time series:

# In[ ]:


___


# In[ ]:


___


# **Note:** once again,  the above plots are challenging to retrieve any meaningful information from. There are too many growth curves so that it's very crowded **and** too many colours look the same so it's difficult to tell which country is which from the legend. Let's plot less curves and in the next section we'll use the python package Altair to introduce interactivity into such a plot in order to deal with this challenge.

# In[ ]:


plot_time_series(recovered_country_drop[poi], 'Recovered Patients Time Series', 'Days', 'Recovered Patients count', True)


# **Summary:** We've 
# - looked at the dataset containing the number of reported recoveries for each region,
# - written function for grouping, wrangling, and plotting the data,
# - grouped, wrangled, and plotted the data for the number of reported recoveries.

# ## Interactive plots with altair

# We're now going to build some interactive data visualizations. I was recently inspired by [this one in the NYTimes](https://www.nytimes.com/interactive/2020/03/21/upshot/coronavirus-deaths-by-country.html), a chart of confirmed number of deaths by country for places with at least 25 deaths, similar to ours above, but with informative hover tools. [This one](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html) is also interesting.

# We're going to use a tool called [Altair](https://altair-viz.github.io/). I like Altair for several reasons, including precisely what they state on their website:
# 
# > With Altair, you can spend more time understanding your data and its meaning. Altair’s API is simple, friendly and consistent and built on top of the powerful [Vega-Lite](https://vega.github.io/vega-lite/) visualization grammar. This elegant simplicity produces beautiful and effective visualizations with a minimal amount of code.
# 
# Before jumping into Altair, let's reshape our `deaths_country` dataset. Notice that it's currently in **wide data format**, with a column for each country and a row for each "day" (where day 1 is the first day with over 25 confirmed deaths). This worked with the `pandas` plotting API for reasons discussed above.

# In[47]:


# Look at head
deaths_country_drop.head()


# For Altair, we'll want to convert the data into **long data format**. What this will do essentially have a row for each country/day pair so our columns will be 'Day', 'Country', and number of 'Deaths'. We do this using the dataframe method `.melt()` as follows:

# In[60]:


# create long data for deaths
deaths_long = deaths_country_drop.reset_index().melt(id_vars = 'index', value_name = 'Deaths').rename(columns={'index':'Day'})
deaths_long.head()


# We'll see the power of having long data when using Altair. Such transformations have been performed for a long time, however it wasn't until 2014 that Hadley Wickham formalized the language in his paper [Tidy Data](https://www.researchgate.net/publication/215990669_Tidy_data). Note that Wickham prefers to avoid the terms long and wide because, in his words, 'they are imprecise'. I generally agree but for our purposes here of giving the flavour, they suffice.
# 
# Now having transformed our data, let's import Altair and get a sense of its API.

# In[61]:


import altair as alt

# altair plot 
alt.Chart(deaths_long).mark_line().encode(
    x='Day',
    y='Deaths',
    color='Country/Region')



# It is nice to be able to build such an informative and elegant chart in four lines of code (which is also elegant). And, looking at the simplicity of the code we just wrote, we can see why it was great to have long data: a column for each variable allowed us to explicitly and easily tell Altair what we wanted on each axis and what we wanted for the colour.
# 
# As the [Altair documentation (which is great, by the way!) states](https://altair-viz.github.io/getting_started/overview.html),
# 
# > The key idea is that you are declaring links between *data columns* and *visual encoding channels*, such as the x-axis, y-axis, color, etc. The rest of the plot details are handled automatically. Building on this declarative plotting idea, a surprising range of simple to sophisticated plots and visualizations can be created using a relatively concise grammar.

# We can now customize the code to thicken the line width, to alter the opacity, and to make the chart larger:

# In[62]:


# altair plot 
alt.Chart(deaths_long).mark_line(strokeWidth = 4, opacity = 0.7).encode(
    x='Day',
    y='Deaths',
    color='Country/Region'
).properties(
    width = 800,
    height = 650
).interactive()


# We can also add a log y-axis. To do this, The long-form, we express the types using the long-form `alt.X('Day',...)`, which is, in the words of the [Altair documentation](https://altair-viz.github.io/user_guide/encoding.html)
# > useful when doing more fine-tuned adjustments to the encoding, such as binning, axis and scale properties, or more.
# 
# We'll also now add a hover tooltip so that, when we hover our cursor over any point on any of the lines, it will tell us the 'Country', the 'Day', and the number of 'Deaths'.

# In[63]:


# altair plot 
alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color='Country/Region',
    tooltip = ['Country/Region', 'Day','Deaths']
).properties(
    width=800,
    height=650
)


# It's great that we could add that useful hover tooltip with one line of code `tooltip=['Country/Region', 'Day','Deaths']`, particularly as it adds such information rich interaction to the chart.
# One useful aspect of the NYTimes chart was that, when you hovered over a particular curve, it made it stand out against the other. We're going to do something similar here: in the resulting chart, when you click on a curve, the others turn grey.
# 
# **Note:** When first attempting to build this chart, I discovered [here](https://github.com/altair-viz/altair/issues/1552) that "multiple conditional values in one encoding are not allowed by the Vega-Lite spec," which is what Altair uses. For this reason, we build the chart, then an overlay, and then combine them.

# In[64]:


# Selection tool
selection = alt.selection_single(fields=['Country/Region'])
# Color change when clicked
color = alt.condition(selection,
                    alt.Color('Country/Region:N'),
                    alt.value('lightgray'))


# Base altair plot 
base = alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color='Country/Region',
    tooltip=['Country/Region', 'Day','Deaths']
).properties(
    width=800,
    height=650
)

# Chart
chart = base.encode(
  color=alt.condition(selection, 'Country/Region:N', alt.value('lightgray'))
).add_selection(
  selection
)

# Overlay
overlay = base.encode(
    color='Country/Region',
  opacity=alt.value(0.5),
  tooltip=['Country/Region:N', 'Name:N']
).transform_filter(
  selection
)

# Sum em up!
chart + overlay


# It's not super easy to line up the legend with the curves on the chart so let's put the labels on the chart itself. Thanks to [Jake Vanderplas](http://vanderplas.com/) for this suggestion, and for the code.

# In[65]:


# drop NaNs
deaths_long = deaths_long.dropna()

# Selection tool
selection = alt.selection_single(fields=['Country/Region'])
# Color change when clicked
color = alt.condition(selection,
                    alt.Color('Country/Region:N'),
                    alt.value('lightgray'))


# Base altair plot 
base = alt.Chart(deaths_long).mark_line(strokeWidth=4, opacity=0.7).encode(
    x=alt.X('Day'),
    y=alt.Y('Deaths', scale=alt.Scale(type='log')),
    color=alt.Color('Country/Region', legend=None),
).properties(
    width=800,
    height=650
)

# Chart
chart = base.encode(
  color=alt.condition(selection, 'Country/Region:N', alt.value('lightgray'))
).add_selection(
  selection
)

# Overlay
overlay = base.encode(
  color='Country/Region',
  opacity=alt.value(0.5),
  tooltip=['Country/Region:N', 'Name:N']
).transform_filter(
  selection
)

# Text labels
text = base.mark_text(
    align='left',
    dx=5,
    size=10
).encode(
    x=alt.X('Day', aggregate='max',  axis=alt.Axis(title='Day')),
    y=alt.Y('Deaths', aggregate={'argmax': 'Day'}, axis=alt.Axis(title='Reported Deaths')),
    text='Country/Region',  
).transform_filter(
    selection
)

# Sum em up!
chart + overlay + text


# **Summary:** We've 
# - melted the data into long format,
# - used Altair to make interactive plots of increasing richness,
# - admired the elegance & simplicity of the Altair API and the visualizations produced.

# That's all for the time being. I'd be interested to see how you all can make these charts more information rich and comprehensible. I encourage you to raise ideas in issues on the issue tracker in [this github repository](https://github.com/hugobowne/COVID-19-EDA-tutorial) and then to make pull requests. A couple of ideas are
# - Adding lines to the above chart that show curves for deaths doubling each X days, as in the [first chart here](https://www.nytimes.com/interactive/2020/03/21/upshot/coronavirus-deaths-by-country.html),
# - Figuring out a way to make the chart less crowded with names by perhaps only showing 10 of them.
