## Answers to HW3 in R

## 1.

library(foreign)
library(stargazer)
griliches.data <- read.dta("E:\\Big Data\\GX 5004\\griliches.dta")

## a. through c. you've done repeatedly.  

## d.  
lm(lw~rns, data=griliches.data)  ## Wages were lower in the South on average at the time of the sample.
lm(lw~mrt, data=griliches.data)  ## Wages were higher for married young men on average at the time of the sample.  
lm(lw~smsa, data=griliches.data)  ## Wages were higher for urban young men on average at the time of the sample.
lm(lw~kww, data=griliches.data)  ## Wages were higher for young men with higher test scores on average at the time of the sample.
lm(lw~expr, data=griliches.data)  ## Wages were higher for young men with more experence on average at the time of the sample.
## In general, these correlations seem correct to me.

## e.
stargazer(lm(lw~s, data=griliches.data), title="Regression Results for Return to Schooling", type="text", ci.level=0.95, ci=TRUE)

## f.
griliches.model <- lm(lw~rns+mrt+smsa+med+iq+kww+age+s+expr, data=griliches.data)
stargazer(griliches.model, title="Griliches Model", type="text", ci.level=0.95, ci=TRUE)
## Note that the returns to schooling has been cut nearly in half, as has the so-called returns to marriage.  
## See Mroz (1999) for a discussion about the returns to marriage.

## g.
age2 <- griliches.data$age**2
griliches.data <- data.frame(griliches.data, age2)
griliches.model <- lm(lw~rns+mrt+smsa+med+iq+kww+age+age2+s+expr, data=griliches.data)
stargazer(griliches.model, title="Griliches Model", type="text", ci.level=0.95, ci=TRUE)
## A quadratic in age does not work very well in this model because the age of the young men is too low for the curvature to kick in.
## You can download a lot of wage data from the March Supplement of the Current Population Survey and examine curvative using it.

## h.  
##  We have discussed the consequences of violation of the assumption the Cov(X, e) = 0.  Now you see directly the ramifications.
##  In the naive bivariate model that relates wages to schooling, all of the other characteristics are omitted, which means they 
##  constitute the "error" term in such a regression equation.  But those omitted characteristics, in particular IQ, are correlated with 
##  schooling (as shown below).  When we omit them, we induce correlation between schooling and the error term, hence violating the 
##  assumption.  Note that the same thing happens with the relationship between wages and marital status.  
cor(x = griliches.data$iq, y = griliches.data$s)

rm(griliches.data, age2, griliches.model, lmws)  ## Dump stuff out.


## 2.
set.seed(2014929)  ## Set RNG for replication

## a.  
x1 <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
x2 <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
e <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
y <- 1 + x1 + x2 + e
cor(x1, x2)
lm <- lm(y~x1)
stargazer(lm, title="Regression Results When We Omit Uncorrelated but Relevant Variable", type="text", ci.level=0.95, ci=TRUE)
lm$coefficients[2]

## This is a powerful result: If we omit something that we know is relevant but uncorrelated with what we include, 
## we still recover an unbiased estimate of what we included in the model that was estimated, even though it is misspecified.

rm(x1, x2, e, y, lm)

## b.
z <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
v <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
w <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
e <- rnorm(10000, mean=0, sd=1)  ## R's command to draw from N(0,1)
x1 <- z + v
x2 <- -z + w
y <- 1 + x1 + x2 + e
cor(x1, x2)
lm <- lm(y~x1)
stargazer(lm, title="Regression Results When We Omit Correlated Relevant Variable", type="text", ci.level=0.95, ci=TRUE)
lm$coefficients[2]

## This is a powerfully disturbing result: If we omit something that is correlated with what we include, we know we are 
## violating the key assumption discussed in the Griliches example--and we have a direct measurement of its effect.
## It biases the X1 coefficent by -0.5.  

rm(e, v, w, x1, x2, y, z, lm)


## 3.  
## a.
union <- read.dta("E:\\Big Data\\GX 5004\\union.dta")
union <- union[order(union$idcode, union$year),]  ## Sorts the data by idcode and year.

head(union, 25)
## Note that the unit of observation in these data is a person-year.
## Note also that there can be transitions in union status (moving out of and into unions).
## Such transitions can be a powerful means of classification, which we will cover during time series analysis.
## For example, note that idcodes 1, 2, and 3 show such union-status transition.

## b.
table(union$year)  ## Get a sense of the distribution across years.

union.train <- subset(union, year<=78)  ## subset is the R command to partition dataframes, in this case into the training data
union.test <- subset(union, year>78)  ## subset into test data for classification.

union.logit <- glm(union ~ age+grade+smsa+south+black+year, data = union.train, family = "binomial")  ## R's logit command is invoked with generalized linear models
union.test$pred.logit <- predict(union.logit, newdata = union.test, type = "response")  ## R's predict command conveniently takes the training coefficients and applies them to the test data.

union.lm <- lm(union ~ age+grade+smsa+south+black+year, data = union.train)
union.test$pred.lm <- predict(union.lm, newdata = union.test, type = "response")

## You were not asked to do this, but examining a scatter plot of the two predictions is useful.
plot(union.test$pred.logit, union.test$pred.lm, pch=16, main="Comparison of Linear and Logit Predictions", col="darkblue", ylab="Linear Prediction", xlab="Logit Prediction", xlim=c(-.1,.5), ylim=c(-.1,.5))
## This plot highlights one of the shortcomings of linear probability models.  
## It may produce predicted values that are negative or greater than one.  
## This will never be true with the logit classifier.  

## c.
## Something like this appeared in my email classifier posted to the course website.
"TABLE 3c1: The Linear Classifier with 25% Threshold"
table(actual=union.test$union, pred=union.test$pred.lm>=0.25)

"TABLE 3c2: The Logit Classifier with 25% Threshold"
table(actual=union.test$union, pred=union.test$pred.logit>=0.25)

## d.
"TABLE 3d1: The Linear Classifier with 20% Threshold"
table(actual=union.test$union, pred=union.test$pred.lm>=0.2)
## Predicted is Row 1/Column TRUE.

"TABLE 3d2: The Logit Classifier with 20% Threshold"
table(actual=union.test$union, pred=union.test$pred.logit>=0.2)
## Predicted is Row 1/Column TRUE.

"TABLE 3d3: The Actual Number of Union Members"
table(union.test$union)
## Actual is Column 1.
