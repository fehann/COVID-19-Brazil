# COVID19 Brazil

# Load libraries
install.packages("remotes")
install.packages("expss")
install.packages("zoo")
install.packages("directlabels")
install.packages("tidyverse")
install.packages("plotly")
remotes::install_github("liibre/coronabr")

library(coronabr)
library(tidyverse)
library(expss)
library(zoo)
library(directlabels)
library(plotly)


# Get data

dados <- get_corona_br(by_uf = TRUE)
str(dados)

plot_uf(dados)
ggplotly()


# Create table with date that 5th death occured

date5thdeath <- setNames(data.frame(matrix(ncol = 2, nrow = 27)), c("state", "date5thdeath"))
date5thdeath$state <- as.factor(unique(dados$state))
date5thdeath$date5thdeath <- as.Date(date5thdeath$date5thdeath)
rownames(date5thdeath) <- date5thdeath$state
date5thdeath
class(date5thdeath)

for(i in date5thdeath$state){
  df <- dados %>%
    filter(state == i) %>%
    mutate(fifthdeath = deaths/5)
  date5thdeath[i,2] <- vlookup(min(df[df$fifthdeath > 1,]$fifthdeath), df, result_column = 1, lookup_column = 12)
}

date5thdeath

dados2 <- merge(dados, date5thdeath, by = "state")

dados2 <- mutate(dados2, datesince5thdeath = as.numeric(date - date5thdeath))

# Visualização
dados2 %>%
  filter(datesince5thdeath > -1, !is.na(date5thdeath), between(datesince5thdeath, 0, max(na.omit(datesince5thdeath))-2)) %>% # disregard last 2 observations and any NAs
  plot_ly(x = ~datesince5thdeath, y = ~deaths, color = ~state, hoverinfo = "text", 
          hovertext = ~paste("Estado: ", state, "<br>",
                        "Mortes: ", deaths, "<br>",
                        "Data: ", date)) %>%
  add_lines() %>%
  add_markers(marker = list(size = 3)) %>%
  layout(xaxis = list(title = "Dias a partir da 5a morte no estado"),
         yaxis = list(title = "Mortes confirmadas (escala logarítmica)", type = "log"),
         title = "Total de mortes confirmadas pelo COVID-19 por estado brasileiro",
         showlegend = FALSE)
  

# Reference lines for time for cases to duplicate
plot_ly() %>%
  add_lines(x = c(0, 1), y = c(5, (5*2^(1/2)))) %>% # double every 2 days
  add_lines(x = c(0, 1), y = c(5, (5*2^(1/5)))) %>% # every 5 days
  add_lines(x = c(0, 1), y = c(5, (5*2^(1/10)))) %>% # every 10 days
  layout(yaxis = list(type = "log"),
         showlegend = FALSE)




