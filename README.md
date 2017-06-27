# Translog Combinations Generator

This Python script, for a given list of strings (variables), will:

* Create two new lists:
  * One with all possible combinations without the product operator to serve as the variables name
  * One with the product operator that will serve as the declaration of the new variables
  
* It will then use those two lists to create the generate command for all combinations for Stata, as well as taking the natural log of each possible combination, as follows:

gen lk = ln(l*k) 
