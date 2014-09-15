

DurationCalculator <- function(dataset,sex){
  median(dataset$tripduration[dataset$gender == sex])
}