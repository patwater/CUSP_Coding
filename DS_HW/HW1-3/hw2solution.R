## Answers to HW2 in R

## 1.

set.seed(672310)  ## Set the random number seed to ensure same sequence
x <- rnorm(10, mean=0, sd=1)  ## R's command to draw from N(0,1)
mean(x)  
var(x)
sd(x)
mean(x)/sd(x)  ## This ratio is the test statistic for classical hypothesis testing.  
## A small value directs us to fail to reject the null hypothesis that the mean is zero.

x <- rnorm(10000, mean=0, sd=1)
mean(x)
var(x)
sd(x)
mean(x)/sd(x)

x <- rnorm(1000000, mean=0, sd=1)
mean(x)
var(x)
sd(x)
mean(x)/sd(x)
hist(x, breaks=200, col="darkblue", main="Histogram Takes on N(0,1)", probability=T)
rm(x)

## 2.

library(foreign)
library(stargazer)
random <- read.csv("E:\\Big Data\\GX 5004\\random.csv", header=T)
attach(random)  ## I like to attach dataframes
head(random, 10)  ## Observations I drew
linear.model <- lm(y ~ x)
summary(linear.model)
## As expected, two independent draws do not appear to be related.  
## The coefficient on b1 is a t-value of well below two.
## As a result, we would fail to reject the null hypothesis of no relation.

stargazer(linear.model, title="Regression Results for Random Integers", type="text")
## One drawback with R is the quite primitive layout of regression results.  
## Stargazer is a useful R package that allows for a more visually appealing layout.
## Python's layout is much better.
detach(random)  ## Detach it
rm(random)  ## Delete the dataframe
rm(linear.model)

## 3.
## Wrangling data off the web is proving to be an important component of big data.
## One could go to Yahoo!Finance and download the relevant data into a spreadsheet,   
## then to be read into R or Python.  You already covered this in your summer bootcamp.
## In this answer, I'm going to use a package called Quandl that links to a fantastic 
## aggregator of economic and financial data.
## I will use IBM as my example.

library(xts)
library(Quandl)

IBM.Q <- Quandl("GOOG/NYSE_IBM", start_date="2005-09-16", type="xts")  ## IBM
NYSE.Q <- Quandl("YAHOO/INDEX_NYA", start_date="2005-09-16", type="xts")  ## NYSE

IBM <- IBM.Q[, "Close"]  ## Cleave off closing price
NYSE <- NYSE.Q[, "Close"]  ## Cleave off close

data <- merge(as.zoo(IBM), as.zoo(NYSE))  ## Merge into single time-series dataset
names <- c("IBM", "NYSE")
colnames(data) <- names

data.level <- as.xts(data)  ## Levels 
data.returns <- diff(log(data.level), lag=1)  ## Log returns
data.returns <- na.omit(data.returns)  ## Dump missing values

hist(data.returns$IBM, breaks=100, col="darkblue", probability=T, main="Histogram of IBM Daily Returns", xlab="Daily Returns")  ## Histogram of returns.  Do they look normally distributed?  Lots of work in finance depends on normally distributed returns.

plot.ts(y=data.returns$NYSE, x=data.returns$IBM, pch=16, col="darkblue", main="CAPM Data", xlab="Log Returns of NYSE", xlim=c(-.1,.1), ylab="Log Returns of IBM", ylim=c(-.1,.1))  ## time series plot in R  
abline(lm(data.returns$IBM ~ data.returns$NYSE), col="purple")  ## I added the best fit line so the graph looks similar to that presented in class for Apple.

ols.returns <- lm(data.returns$IBM ~ data.returns$NYSE)
summary(ols.returns)
stargazer(ols.returns, title="Regression Results for CAPM", type="text", ci.level=0.95, ci=TRUE)
##  Tell stargazer to generate 95% confidence intervals
##  In this case, the confidence interval on alpha includes 0.
##  Confidence interval on beta does not include 1.  

## 4.
library(foreign)  ## The R package foreign is quite adept at wrangling data from a variety of format types, including Stata, SAS, SPSS, etc.  
train.data <- read.dta("E:\\Big Data\\GX 5004\\train.dta")  ## Read in the training data
attach(train.data)  ## I like to attach data

## Summary Statistics
mean(d)
var(d)
sd(d)

mean(x1)
var(x1)
sd(x1)

cor(x1)

svm=lm(d~x1)  ## Fit your least squares model.  This is indeed a SVM.
stargazer(svm, title="Regression Results for SVM", type="text", ci.level=0.95, ci=TRUE)

attributes(svm)  ## R command to show you what the attributes are store in object svm, where the regression results "live".
svm$coefficients[2]  ## Confirm we have the correct coefficient.

## Recall that the predicted value is the new attribute value times the coefficient value.
svm$coefficients[2]*0.65  ## The new attribute is 0.65, so not spam.
svm$coefficients[2]*0.99  ## The new attribute is 0.99, so spam.

detach(train.data)

## 5.
## This is a challenging question.  
## 5a through 5d are straightforward.  
## 5e and 5f require some programming, but it demonstrates the power of Monte Carlo.

## 5b.
set.seed(1234567)  ## Set the random number seed to ensure I get the same draws.
e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
x <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
y <- 1+2*x+e  ## DGP for y

## 5c.
library(stargazer)  ## Load stargazer library to "nicely" summarize regression model findings.
linear.model <- lm(y ~ x)
stargazer(linear.model, title="Regression Results for DGP", type="text")  ## Summarize results.  Spot on.

## 5d.
for(i in 1:5) {
  e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  x <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  y <- 1+2*x+e  ## DGP for y
  linear.model <- lm(y ~ x)
  stargazer(linear.model, title="Regression Results for DGP", type="text")  ## Summarize results.  Spot on.
}

## 5e.
## This is the challenging part.  We want to loop over 1,000 linear models with the same DGP.
## We need to store the slope coefficient on each loop, however.

betas <- rep(0,1000)  ## Creates a real-valued vector of zeros of 1 by 1000
set.seed(9212014)

for(i in 1:1000) {
  e <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  x <- rnorm(1000, mean=0, sd=1)  ## R's command to draw from N(0,1)
  y <- 1+2*x+e  ## DGP for y
  linear.model <- lm(y ~ x)
  betas[i] <- linear.model$coefficients[2]
}

hist(betas, breaks=50, col="darkblue", main="Histogram of Slope Coefficients", freq=F, xlab="",  xlim=c(1.8,2.2))  ## Histogram for distribution of betas

exp.betas <- exp(betas)  ## Now exponentiate the vector.
hist(exp.betas, breaks=50, col="darkblue", main="Histogram of Exponentiation of Slope Coefficients", freq=F, xlab="",  xlim=c(6.5,8.5))  ## And graph.

## 5 shows two important things.
## First, if you were to repeat 5e with a large number of replications, you would empirically show the Law of Large Numbers, which drives classical hypothesis testing.
## Second, there may be circumstances in which you are interested in some nonlinear transformation of a coefficient from a linear model.
## The replications of exp(beta) give you the empirical distribution of this random variable that you can use to do hypothesis testiing.