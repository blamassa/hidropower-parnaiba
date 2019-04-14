library(fitdistrplus)
library(tidyr)
library(ggplot2)

setwd('./temp/hidropower-parnaiba/eolica/')

data <- read.csv('paodeacucar_r.csv')
data <- drop_na(data)

x <- data[data$vel_m != 0,]$vel_m
x.norm <- x/max(x)

# Printar o Cullen and Frey graph
descdist(x)
# o resultado indica uma possivel distribuição de weibull. Vamos tentar uma normal tambem
fit.norm <- fitdist(x, "norm")
fit.gamma <- fitdist(x, "gamma")
fit.weibull <- fitdist(10*c(na.exclude(x)), 'weibull')

# Comparando
fit.weibull$aic
fit.gamma$aic
fit.norm$aic


# Plottinf ecdf
ll <- Map(f  = stat_function, colour = c('red', 'blue'),
          fun = list(ecdf(x), ecdf(rw)), geom = 'step')


ggplot(data = data.frame(x,rw), aes(x = x)) + ll
